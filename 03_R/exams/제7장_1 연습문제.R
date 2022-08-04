#################################
## <제7장-1 연습문제>
################################# 

# 01. 다음과 같은 단계를 통해서 테이블을 가져와서, SQL문을 이용하여 레코드를 조회하시오.

# [단계 1] 사원테이블(EMP)을 검색하여 결과를 EMP_DF 변수로 불러오기
query="SELECT * FROM emp"
emp_df=dbGetQuery(conn,query)
emp_df

# [단계 2] EMP_DF 변수를 대상으로 직책(job)별 급여의 평균을 막대차트로 시각화
# 파이프 연산자 활용
library(dplyr) # 파이프 연산자, group_by(), summarise() 이용
result = emp_df %>% group_by(JOB) %>% summarise(sal_age=mean(sal))
result
# A tibble: 5 x 2
# JOB       sal_age
# <chr>       <dbl>
# 1 ANALYST     2073.
# 2 CLERK       2073.
# 3 MANAGER     2073.
# 4 PRESIDENT   2073.
# 5 SALESMAN    2073.

query="SELECT job,avg(sal) FROM emp GROUP BY job"
emp_df2=dbGetQuery(conn,query)
emp_df2

# [단계 3] 막대차트를 대상으로 X축의 축눈금을 직책명으로 표시하기
# <7-1_연습문제1번_결과.png> 참고 
job_name=emp_df2$JOB
barplot(emp_df2$`AVG(SAL)`,col=rainbow(5),names.arg=job_name,
        xlab="직책",ylab="급여",main="직책별 급여 평균")

#  02. 'WARD' 사원의 상사(MGR)와 동일한 사원이름, 직책, 연봉을 출력하시오.
# [단계 1]  Oracle 서브쿼리 이용
query="SELECT ename,job,sal FROM emp WHERE mgr=(SELECT mgr FROM emp WHERE ename='WARD')"
ward_MGR=dbGetQuery(conn,query)
ward_MGR

rate=round(ward_MGR$SAL/sum(ward_MGR$SAL),3)*100  
chart_labels=paste(ward_MGR$ENAME,'\n',rate,'%')
chart_labels

# [단계 2] 차트 시각화 
# <7-1_연습문제2번_결과.png> 참고
pie(ward_MGR$SAL,
    col=rainbow(5),
    main="WARD 사원과 상사가 같은 사원들의 급여",
    labels=chart_labels)
