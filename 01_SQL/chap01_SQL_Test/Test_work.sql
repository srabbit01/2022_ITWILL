-- Test_work.sql

/*
13. EMP 테이블에서 20번 부서에 근무하는 사원의 사번, 이름, 부서번호를 조회하는 SQL문을 작성하시오.
사용 테이블명 : EMP 
 사용 컬럼명 : 사번(empno), 이름(ename),  부서번호(deptno) 
 */
SELECT empno 사번, ename 이름, deptno 부서번호
FROM emp
WHERE deptno = 20;

/*
14. professor 테이블에서 직위가 '정교수'이고 급여가 500이상인 교수만 조회하는 SQL문을 작성하시오.
 사용 테이블 : PROFESSOR   
 사용 컬럼명 : 직위(position), 급여(pay)
 */
SELECT *
FROM professor
WHERE position = '정교수' AND pay >= 500;

/*
15. student 테이블에서 키가 175 이상이고, 몸무게가 60 이상인 학생들의 이름, 학년, 키, 몸무게를 조회하는 SQL문을 작성하시오.
 사용 테이블명 : STUDENT
 사용 컬럼명 : 이름(name), 학년(grade), 키(height), 몸무게(weight)
 */
SELECT name 이름, grade 학년, height 키, weight 몸무게
FROM student
WHERE height >= 175 AND weight >= 160;

/*
16. '심슨' 교수를 지도교수로 모시는 전체 학생 명부를 조회하는 SQL문을 작성하시오.(서브쿼리 이용)
  사용 테이블명 : PROFESSOR,  STUDENT
  사용 컬럼명 : 교수이름(name), 교수번호(profno)
  */
SELECT *
FROM student
WHERE profno =  (SELECT profno FROM professor WHERE name = '심슨');

/*
18. EMP 테이블을 대상으로 사번(empno), 이름(ename), 급여(sal), 수당(comm), 부서번호(deptno)를 내용으로 갖는 테이블을 생성하시오. (단 테이블의 이름은 EMP_TABLE)
*/
DROP TABLE emp_table;
CREATE TABLE emp_table
AS
SELECT empno 사번, ename 이름, sal 급여, comm 수당, deptno 부서번호 FROM emp;

/*
19. 다음은 두 테이블의 정의서를 참고하여 문제를 풀이하시오.
*/
-- 1. 위 테이블 정의서를 보고 각 테이블을 생성하는 SQL문을 작성하시오. 
-- 1) DEPT_exam 테이블 생성
DROP TABLE DEPT_exam;
CREATE TABLE DEPT_exam(
deptno NUMBER PRIMARY KEY,
dname VARCHAR(10) NOT NULL,
loc VARCHAR(20));
-- 2) EMP_exam 테이블 생성
DROP TABLE EMP_exam;
CREATE TABLE EMP_exam(
empno NUMBER(4) PRIMARY KEY,
ename VARCHAR(20) NOT NULL,
pay NUMBER(8,2),
hiredate DATE,
job CHAR(10),
deptno NUMBER(2) NOT NULL,
FOREIGN KEY (deptno) REFERENCES DEPT_exam(deptno)
);
-- 2. 각 테이블에 레코드를 2개 이상 삽입하는 SQL문을 작성하시오. 
-- 1) DEPT_exam 레코드 삽입
INSERT INTO DEPT_exam VALUES(10,'영업부','서울시');
INSERT INTO DEPT_exam VALUES(20,'기획부','부산시');
-- 2) EMP_exam 레코드 삽입
INSERT INTO EMP_exam VALUES(1,'홍길동',350,'20/01/03','SALESMAN',10);
INSERT INTO EMP_exam VALUES(2,'전우치',500,'18/03/23','MANAGER',20);
-- 3. 조인된 키를 이용하여 사원명, 직책, 부서명, 부서위치를 조회하는 SQL문을 작성하시오.
SELECT e.ename 사원명, e.job 직책, d.dname 부서명, d.loc 부서위치
FROM EMP_exam e, DEPT_exam d;

COMMIT;