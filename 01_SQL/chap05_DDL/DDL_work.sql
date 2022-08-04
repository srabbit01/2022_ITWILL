-- DDL_work.sql

/*
데이터 정의어(DDL): 테이블 생성, 변경, 삭제
  - 자동 커밋(AUTO COMMIT): 작업 내용을 자동으로 데이터베이스에 반영하는 것 (DML의 경우, 자동으로 커밋 불가능) 
  - 별도의 COMMIT 명령어 수행 필요 없음
*/

-- 1. 테이블 생성

-- 1) 의사컬럼
-- ROWNUM: 레코드 순번 (레코드 입력 순서)
-- ROWID: 레코드 식별을 위한 해시값 제공 (해시값: 암호화된 코드로 값만으로 의미를 알 수 없음) = 중복되지 않는 유일한 값

-- 예1) 최초 레코드 순번 검색: 의사칼럼은 SELECT절, WHERE,ORDER BY절 모두 사용할 수 있음
SELECT ROWNUM, EMPNO, ENAME, ROWID
FROM EMP WHERE ROWNUM <=10 
ORDER BY rownum;  -- 내림차순 정렬

-- 예2) 5~10번째 입사자: 범위를 지정하여 ROWNUM으로 추출 -> 특정 위치는 검색 안됨
SELECT ROWNUM, EMPNO, ENAME, ROWID
FROM EMP WHERE ROWNUM >=5 AND ROWNUM <=10;  -- 문법적으로 오류가 없으나 검색이 되지 않음
-- 의사컬럼은 처음부터~는 연산이 가능하나, ~보다 크다 등 관계 연산은 불가능
-- So, 별칭 이용하여 범위 검색
-- 서브쿼리 + 의사컬럼의 별칭
SELECT mum, EMPNO, ENAME
FROM (SELECT emp.*,ROWNUM AS mum FROM emp)  -- 테이블 이름 대신 서브쿼리로 바꾸기
WHERE mum BETWEEN 5 AND 10;
/*
- emp.* = 테이블.전체컬럼 = 테이블이 가진 8개의 모든 컬럼을 메인쿼리에 넘겨주는 역할
- emp.칼럼명 = 테이블.특정칼럼명
- mum: ROWNUM의 별칭
- 주의: 서브쿼리에서 선택한 컬럼만 메인쿼리의 SELECT절에서 사용 가능
- 서브쿼리 칼럼 별칭: 메인쿼리의 SELECT, WHERE절에 사용
*/

-- 테이블 별칭 사용
-- 별칭: 실제 존재하는 이름을 대신하는 또 다른 이름
-- 테이블 별칭: SELECT, WHERE절에 사용
-- 별칭을 이용하여 두개의 테이블에서 내용을 가져올 수 있음
SELECT e.ename, d.deptno, d.dname
FROM emp e, dept d  -- 테이블 별칭
WHERE e.deptno = d.deptno;

-- 2) 실수형 테이블 생성
CREATE TABLE EMP01(
EMPNO NUMBER(4),
ENAME VARCHAR2(20),
SAL NUMBER(7, 2));   -- (전체,소숫점)

INSERT INTO emp01 VALUES(1,'hong',1234.1);  -- 정상
INSERT INTO emp01 VALUES(2,'lee',1234.123);  -- 정상: 소숫점 이하의 자릿수 초과 = 반올림 
INSERT INTO emp01 VALUES(3,'kang',123456.123);  -- 오류: 전체 자릿수를 초과하는 경우 - 8자리 필요
SELECT * FROM emp01;

-- 3) 서브 쿼리를 이용한 테이블 생성
CREATE TABLE EMP02  -- 사본: 원본의 자료+구조(스키마) 복제본
AS
SELECT * FROM EMP;  -- 원본
SELECT * FROM emp02;

-- 실습1) 특정 컬럼 대상으로 테이블 생성 가능
-- SELECT절에 원하는 컬럼을 넣으면 선택적으로 컬럼을 추출하여 복제할 수 있음
DROP TABLE emp03 cascade constraint;
CREATE TABLE emp03  -- 사본: 일부분의 자료+구조
AS
SELECT empno,ename FROM emp;  -- 원본

-- 실습2) EMP 테이블을 복사하되 사원번호, 사원이름, 급여 컬럼으로 구성된 테이블을 생성하시오.(단 테이블의 이름은 EMP04) 
CREATE TABLE emp04
AS
SELECT deptno,ename,sal FROM emp;
SELECT * FROM emp04;

/*
특정 열: SELECT절 관련
특정 행: WHERE절 관련
*/

-- 조건에 만족하는 특정 행 테이블 생성
CREATE TABLE emp05  -- 특정 행: 10번 부서 사원만 추출
AS
SELECT * FROM emp WHERE deptno = 10;
SELECT * FROM emp05;

-- 실습3) 영업사원만 관리하는 테이블 만들기: 테이블명 sales
CREATE TABLE sales
AS
SELECT * FROM emp WHERE job = 'SALESMAN';
SELECT * FROM sales;

-- 테이블의 구조(스키마)만 복사하기
-- WHERE 1=0: 조건이 거짓이기 때문에 어떤 데이터도 복제되지 않음
CREATE TABLE emp06
AS
SELECT * FROM emp WHERE 1=0;
SELECT * FROM emp06;
-- 실습) dept 테이블과 동일한 구조의 테이블 형성
CREATE TABLE dept02
AS
SELECT * FROM dept WHERE 1=0;
SELECT * FROM dept02;
DESC dept02;  -- 테이블의 구조 확인
INSERT INTO dept02 values(10,'기획실','서울시');


-- 4. 테이블의 제약조건: 부벅절한 자료 입력 방지 (신뢰성 목적)

-- 1) 기본키(Primary Key): 테이블 당 1개만 지정 가능, 중복불가, null불가
-- (1) 컬럼 레벨 지정
CREATE TABLE test_tab1(
id NUMBER(2)  PRIMARY KEY,
name VARCHAR2(10));
-- (2) 테이블 레벨 지정
CREATE TABLE test_tab2(
id NUMBER(2),
name VARCHAR2(10),
PRIMARY KEY (id));

-- 2) 외래키(Foreign Key): A 테이블(Master Table)의 기본키를 B 테이블에서 참조하는 칼럼
-- (1) 마스터 테이블(=원잘 테이블) 생성: 분기/년 별로 수정 빈도가 낮은 테이블(거래 기본 정보 존재)
CREATE TABLE DEPT_TAB (
DEPTNO NUMBER(2) PRIMARY KEY,  -- 기본키
DNAME CHAR(14),
LOC CHAR(13));
-- (2) 기본 테이블 레코드 추가
INSERT INTO dept_tab VALUES(1,'기획부','서울시');
INSERT INTO dept_tab VALUES(2,'영업부','부산시');
-- (3) 디테일 테이블(=거래 테이블) 생성: 매일 등 수정 빈도가 높은 테이블(거래 정보 등 존재)
CREATE TABLE EMP_TAB (
EMPNO NUMBER(4) PRIMARY KEY,  -- 기본키
ENAME VARCHAR2(10),  -- 사원 이름
SAL NUMBER(7,2),  -- 급여
DEPTNO NUMBER(2) NOT NULL,  -- 부서번호: 외래키
FOREIGN KEY (DEPTNO) REFERENCES DEPT_TAB (DEPTNO));  -- 외래키 지정: 외래 케이블의 deptno를 사용하여 마스터 테이블 dept_tab의 deptno를 참조
-- (4) 외래 테이블 레코드 추가
-- 부서번호는 기본 테이블에 1과 2만 있기에 그 값만 참조 가능 (마스터 테이블에 없는 값을 입력 경우 참조 과정에서 오류 발생 = 참조 무결성 제약조건 위배)
INSERT INTO emp_tab VALUES(1001,' 홍길동',250,2);  -- 정상
INSERT INTO emp_tab VALUES(1002,' 이순신',350,1);   -- 정상
INSERT INTO emp_tab VALUES(1003,' 강호동',150,3);   -- 오류: 참조하는 컬럼 외의 값 입력 시, 오류 발생 = 참조 무결성 제약조건 위배

-- 3) 유일키(Unique Key): 여러개 지정, 중복불가, null 허용
CREATE TABLE UNI_TAB1 (
DEPTNO NUMBER(2) UNIQUE,  -- 컬럼 level
DNAME CHAR(14),
LOC CHAR(13));
INSERT INTO uni_tab1 VALUES(1,'AAAA','BBBB');
INSERT INTO uni_tab1 VALUES(1,'AAAA','BBBB');  -- 오류: 중복때문
INSERT INTO uni_tab1(dname,loc) VALUES('AAAA','BBBB');  -- NULL 허용
INSERT INTO uni_tab1 VALUES('','AAAA','BBBB');  -- NULL 사용 = '' (홑따옴표 사이에 아무것도 넣지 않으면 NULL임을 의미)
SELECT * FROM uni_tab1;

-- 4) NOT NULL(NN): 오직 컬럼 level에서만 사용 가능
CREATE TABLE NN_TAB1 (
DEPTNO NUMBER(2) NOT NULL,
DNAME CHAR(14),
LOC CHAR(13));
INSERT INTO nn_tab1 VALUES (1,'기획부','서울시');  -- 정상
INSERT INTO nn_tab1(dname,loc) VALUES('영업부','부산시');  -- 오류 발생
INSERT INTO nn_tab1 (deptno,dname) VALUES(10,'행정부');  -- 정상: loc 생략
INSERT INTO nn_tab1 (deptno,loc) VALUES(5,'대구시'); -- 정상: dname 생략 
SELECT * FROM nn_tab1;
DELETE FROM nn_tab1 WHERE deptno = 1;

-- 5) 점검(CHECK): CHECK 조건식 (관계 연산자/논리 연산자/SQL 연산자 등 조건으로 이용)
-- 조건에 만족 = 삽입, 조건에 만족X = 차단
-- CHECK 다음에는 조건식이 반드시 딸려옴
CREATE TABLE CK_TAB (
DEPTNO NUMBER(2) NOT NULL CHECK (DEPTNO IN (10,20,30,40,50)),  -- 제약조건 2개: NOT NULL, CHECK
DNAME CHAR(14),
LOC CHAR(13));
INSERT INTO ck_tab VALUES(10,'AAAA','BBBB');  -- 정상: 레코드 삽입
INSERT INTO ck_tab VALUES(80,'AAAA','BBBB');  -- 오류: 체크 제약조건 위배


-- 5. 테이블의 구조 변경(ALTER TABLE 명령문)

-- 1) 칼럼 추가
SELECT * FROM emp01;  -- 테이블의 내용 확인
DESC emp01;  -- 테이블 구조 확인
ALTER TABLE emp01 ADD(job VARCHAR(9));  -- 추가된 컬럼: NULL 채워짐
-- 실습)
DESC dept02;
ALTER TABLE dept02 ADD(dmgr VARCHAR(10));

-- 2) 칼럼 수정: 자료형, 크기, 기본값 변경
-- 한글 1음절 = 영문 3음절이기 때문에 3배 크기의 byte 할당
ALTER TABLE emp01 MODIFY(job VARCHAR(30));  -- 크기 변경 (9 > 30)
-- 실습) DEPT02 테이블의 부서장(DMGR) 칼럼을 숫자 타입으로 변경하시오
ALTER TABLE dept02 MODIFY(dmgr int);

-- 3) 칼럼 삭제
ALTER TABLE EMP01 DROP COLUMN JOB; 
-- 실습) DEPT02 테이블의 부서장(DMGR) 칼럼을 삭제하시오
ALTER TABLE dept02 DROP COLUMN dmgr;

-- 4) 전체 레코드 제거(내용 지우기)
SELECT * FROM emp02;
TRUNCATE TABLE emp02;

-- 5) 테이블 이름 변rud
ALTER TABLE emp01 RENAME TO emp01_copy;


-- 7. 테이블 제거/임시파일
-- 임시파일: 테이블 제거시, 임시파일을 남겨 테이블 복원 기능 제공
-- PURGE : 테이블 임시파일도 제거 = 영구제거
-- 1) 전체 테이블 목록 보기
SELECT * FROM tab;  -- 의사 테이블: 실존하지 않으나 테이블의 목록 확인시 사용
SELECT tname FROM tab;  -- 전체 테이블명 조회
SELECT tname FROM tab WHERE tname LIKE  '%EMP%'; -- 테이블의 이름은 반드시 대문자로 조회
-- 2) 테이블 제거 + 임시파일 제거
DROP TABLE emp01_copy PURGE;
--3)  테이블만 제거 후, 임시파일 전체 제거
CREATE TABLE emp01
AS
SELECT * FROM emp;
DROP table emp01;
SELECT * FROM tab;  -- 의사테이블 = 전체 테이블 + 임시파일 제공


-- 8. 데이터 사전과 데이터 사전뷰
-- 데이터 사전: DB에 저장된 중요 정보 (시스템 테이블)
-- 데이터 사전 뷰: 뷰를 통해 사전 확인

-- 사용자용 뷰: USER_XXXX
-- 관리자용 뷰: DBA_XXXX

-- 사용자 확인
SHOW USER;  -- SCOTT

-- 1) USER_TABLESL 테이블 목록 보기 뷰
-- 테이블 목록: 테이블 칼럼 수 등 테이블에 대한 상세 정보 제공
SELECT * FROM USER_TABLES
ORDER BY table_name;  -- 이름 순대로 정렬

-- 2) USER_RECYCLEBIN: 임시파일 목록 보기 뷰(VIEW)
SELECT * FROM USER_RECYCLEBIN;

-- 추가: 임시파일을 이용하여 삭제된 원본 테이블 복원하기
-- (1)TEST 데이터 생성
CREATE TABLE dept_test
AS
SELECT * FROM dept;
-- (2) 임시파일 생성
DROP TABLE dept_test;
-- (3) 임시파일 확인
SELECT * FROM USER_RECYCLEBIN;
-- (4) 테이블 복원: FLASHBACK TABLE 임시파일 TO BEFORE DROP;
FLASHBACK TABLE (SELECT object_name FROM USER_RECYCLEBIN WHERE original_name = 'DEPT_TEST') TO BEFORE DROP;
SELECT object_name FROM USER_RECYCLEBIN WHERE original_name = 'DEPT_TEST';
FLASHBACK TABLE "BIN$V2Zb4/6gTAijb9ST+l6M6g==$0" TO BEFORE DROP;
-- 성공했습니다
-- (5) 테이블 복원 확인
SELECT * FROM tab;

-- 3) USER_CONSTRIANTS: 테이블의 제약조건 확인
CREATE TABLE AA(
a INT PRIMARY KEY,  -- PK
b INT UNIQUE,  -- UU
c INT NOT NULL REFERENCES AA(a),  -- NN, FK
d CHAR CHECK (d IN ('a','b','c'))  -- CH
);
DESC AA;
SELECT * FROM USER_CONSTRAINTS WHERE TABLE_NAME = 'AA';
/*
C: NOT NULL 혹은 CHECK
P: Primary Key
U: Unique
R: Foreign Key (References)
*/

-- 4) USER_CONS_COLUMNS: 테이블 칼럼의 제약조건 확인
SELECT * FROM USER_CONS_COLUMNS WHERE TABLE_NAME = 'AA';  -- 제약조건에 관련된 칼럼 제공

-- 5) 테이블 조인(JOIN): 'CONSTRAINT_NAME'을 이용하여 USER_CONSTRAINS와 USER_CONS_COLUMNS 결합하기               
-- 등호만 사용하여 결합(JOIN)하기: 반드시 일치!
SELECT COL.CONSTRAINT_NAME, COL.COLUMN_NAME, CON.CONSTRAINT_TYPE, CON.SEARCH_CONDITION
FROM USER_CONSTRAINTS CON, USER_CONS_COLUMNS COL
WHERE CON.TABLE_NAME = 'AA'  -- 특정 테이블 지정
               AND CON.CONSTRAINT_NAME = COL.CONSTRAINT_NAME;
               
-- 주의: IN이면 이 중의 하나만 일치하면 되기에 일치가 X
SELECT COL.CONSTRAINT_NAME, CON.CONSTRAINT_NAME, COL.COLUMN_NAME, CON.CONSTRAINT_TYPE, CON.SEARCH_CONDITION
FROM USER_CONSTRAINTS CON, USER_CONS_COLUMNS COL
WHERE CON.CONSTRAINT_NAME IN(SELECT CONSTRAINT_NAME FROM USER_CONS_COLUMNS WHERE TABLE_NAME='AA');