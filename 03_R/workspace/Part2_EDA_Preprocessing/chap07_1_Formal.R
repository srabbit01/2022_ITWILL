# chap07_1_Formal

########################################
## Chapter07-1. 정형데이터 처리 
########################################
# DB 자료 활용: SQL문을 이용하여 DB 자료 불러오기 + R 패키지(시각화 도구, 분석 도구)


# 1. JDK & JRE 설치 : RJDBC 패키지를 사용하기 위해서는 java 설치
######################################
## JDK & JRE 설치 
######################################

# 2. 패키지 설치
#install.packages("rJava") # 기존 설치된 패키지 
install.packages("DBI") # DB 연동 인터페이스
install.packages("RJDBC") # R + DB 연동


# 3. 패키지 로딩
library(DBI)
Sys.setenv(JAVA_HOME='C:/Program Files/Java/jdk1.8.0_151') # 자바의 홈디렉토리와 경로가 일치하도록 함
library(rJava)
library(RJDBC) # rJava에 의존적


# 4. Oracle 연동   
######################## Oracle 11g ####################################
# 단계1: driver 객체 
# JDBC() 함수: rJDBC 패키지에서 지원
# 인수: driverClass='오라클 연동하는 드라이버(데이터베이스 연결 프로그램) 프로그램'
# classPath: 드라이버 경로
drv <- JDBC(driverClass="oracle.jdbc.driver.OracleDriver", # 패키지.OracleDriver() 
            classPath="C:/oraclexe/app/oracle/product/11.2.0/server/jdbc/lib/ojdbc6.jar")

# 단계2:  db연동(driver, url, user, password) 
# dbConnect:DB 연동 함수
# drv: 
# url: 연결하고자 하는 오라클의 url (ip//포트번호/DB이름)
# user: 사용자
# password: 비밀번호
conn <- dbConnect(drv=drv, 
                  url="jdbc:oracle:thin:@//127.0.0.1:1521/xe",
                  user="scott", 
                  password="tiger")
######################################################################

# 5. DB 사용

# 1) 전체 테이블 조회
query="select * from tab where tname='DB_TEST'"
dbGetQuery(conn,query)

# 2) 테이블 생성
query="CREATE TABLE db_test(sid int, pwd char(4),
       name varchar(25), age int)"
dbSendUpdate(conn,query)
dbGetQuery(conn,"SELECT * FROM DB_TEST")

# 3) 테이블 수정: dbSendUpdate() 테이블 생성/내용추가/내용수정 등

# (1) INSERT문: 레코드 추가
query="INSERT INTO DB_TEST VALUES(1001,'1234','홍길동',25)"
dbSendUpdate(conn,query)
dbGetQuery(conn,"SELECT * FROM db_test")

# (2) UPDATE문: 레코드 수정
query="UPDATE DB_TEST set name='김길동' WHERE sid=1001"
dbSendUpdate(conn,query)
dbGetQuery(conn,"SELECT * FROM db_test")

# (3) DELETE문: 레코드 삭제
dbSendUpdate(conn,"DELETE FROM DB_TEST WHERE sid=1001")
dbGetQuery(conn,"SELECT * FROM DB_TEST")

# 4) 테이블 삭제
dbSendUpdate(conn,"DROP TABLE DB_TEST PURGE")
dbGetQuery(conn,"SELECT * FROM tab WHERE TNAME='DB_TEST'")

# 5) 테이블 불러오기
emp = dbGetQuery(conn,"SELECT * FROM emp")
str(emp) # 14 obs(행). of  8 variables(열):
# 숫자형=숫자형, 문자형=문자형으로 읽음
# 주의: 날짜형은 DATE형이 아닌 문자형으로 읽어옴
job = emp$JOB # 사원의 직책 저장

# 유일한 직책
unique(job) # 중복되지 않는 범주 출력

# 통계함수
sal = emp$SAL
mean(sal)
sum(sal)

mean(emp$COMM,na.rm=T) # 결측치 외 값만 출력

summary(sal) # 요약통계 구하기

# 조건식
# 쿼리문이 길면 별도의 query 함수를 만드는 것이 좋음
query="SELECT * FROM emp WHERE sal>=2500 AND JOB='MANAGER'"
manager_2500=dbGetQuery(conn,query)

prof=dbGetQuery(conn,
           "SELECT name,pay FROM professor WHERE position='정교수'")
prof

prof_names=prof$NAME
barplot(prof$PAY,col=rainbow(5),names.arg=prof_names,
        xlab='교수명',ylab='급여',main='정교수 급여 현황')

# 서브쿼리 사용
# 부서 = 'SALES' 전체 사원의 이름, 급여, 직책 조회
# sub: dept, main: emp
dbGetQuery(conn,"SELECT * FROM dept")

query="SELECT * FROM emp
       WHERE deptno=(SELECT deptno FROM dept WHERE dname='SALES')"
sales=dbGetQuery(conn,query)

# table join
query="SELECT e.ename,e.job,d.dname,d.loc
       FROM EMP e,DEPT d
       WHERE e.deptno=d.deptno AND e.ename LIKE '%M%'"
join_df=dbGetQuery(conn,query)
join_df

# 집계함수 이용: 각 부서별 급여 평균, 합계 구하기
query="SELECT deptno,sum(sal) tot_sal,avg(sal) avg_sal
       FROM emp
       GROUP BY deptno
       ORDER BY deptno"
result=dbGetQuery(conn,query)
result
#   DEPTNO TOT_SAL  AVG_SAL
# 1     10    8750 2916.667
# 2     20   10875 2175.000
# 3     30    9400 1566.667

dept=dbGetQuery(conn,"SELECT * FROM dept")
dept

dept_names=dept$DNAME[1:3] # OPERATIONS는 없는 것
dept_names # "ACCOUNTING" "RESEARCH"   "SALES" 

avg_sal=round(result$AVG_SAL)
barplot(avg_sal,col=rainbow(5),
        main="부서별 평균 급여",
        names.arg=dept_names,
        xlab="부서명",
        ylab="평균 급여(단위: 천원)",
        ylim=c(0,3500))

# 6. DB 연결 종료
dbDisconnect(conn)
