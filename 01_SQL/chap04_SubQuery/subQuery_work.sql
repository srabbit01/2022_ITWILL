-- subQuery_work.sql

//*
서브쿼리: SELECT문에 포함된 또 하나의 SELECT문

- 용도: 단일 쿼리문으로 조회 등 작업이 불가능한 경우
  예1) 동일한 테이블: 1차 검색결과 -> 2차 작업(검색, 테이블 생성, 삽입, 수정, 삭제) = 검색 결과를 다른 용도로 사용하고자 할 때
  예2) 동일한 테이블의 동일한 컬럼: '우유'와 '빵'을 동시에 구매한 고객의 ID 출력 - 서로 다른 컬럼의 값은 동시에 조회 불가능, 단일 SELECT문에서는 커서가 돌아가지 X
 name = '우유' and name = '빵' 
  예3) 서로 다른 테이블 조인(JOIN): 사원 테이블 -> 부서 테이블 조회
  예4) 동일한 테이블: 집계된 통계를 이용하여 조회할 경우 ( 주의: 통계 계산과 조회를 동시에 할 수 없음)

-  형식: subquery 1차 실행 후, main query 2차 실행
  형식1) 예1
    main query  ->  2차 실행
    AS
    subquery;  ->  1차 실행
  형식2)
    main query 비교연산자 (subquery);
*/

-- 형식1)
 CREATE TABLE dept01   -- 2차: 테이블 생성   -- 기존에 없는 테이블의 입력을 해야 함
 AS
 SELECT * FROM dept;  -- 1차: 레코드 조회
 
--- 형식2) Main: 부서(dept), Sub(emp) -> 해당 사원이 어떤 부서에서 근무하는지 사원 테이블에 있으나, 부서에 대한 정보는 부서 테이블에 있음
SELECT * FROM dept WHERE deptno  = 
(SELECT deptno FROM emp WHERE ename = 'SCOTT');  -- SCOTT은 20번 부서에 일하며, 해당 부서의 이름/주소를 알기 위해 dept 재조회

-- 1. 단일행 서브쿼리
-- 형식) main query 비교 연산자 (sub query);
-- 전제 조건: 테이블1과 테이블2가 동일한 컬럼으로 연결되어 있는 경우

-- 실습1) SCOTT과 같은 부서에서 근무하는 사원의 이름과 부서 번호를 출력하는 SQL 문을 작성해 보시오. (EMP)
SELECT ename, deptno FROM emp
WHERE deptno = (SELECT deptno FROM emp WHERE ename = 'SCOTT');  -- 부서 번호: 20
/* 단일 쿼리문
SELECT ename deptno FROM emp WHERE deptno = 20;
*/

-- 실습2) SCOTT와 동일한 직속상관(MGR)을 가진 사원을 출력하는 SQL 문을 작성해 보시오. (EMP)
-- 찾고자 하는 사원의 이름이 변하는 경우, sub query를 사용하는 것이 유용 (변수O)
SELECT * FROM emp WHERE mgr = (SELECT mgr FROM emp WHERE ename = 'SCOTT');  --- mgr = 7566
/* SELECT * FROM emp WHERE mgr = 7566; */

-- 실습3) SCOTT의 급여와 동일하거나 더 많이 받는 사원 명과 급여를 출력하시오.(EMP)
SELECT ename,sal FROM emp WHERE sal >= (SELECT sal FROM emp WHERE ename = 'SCOTT') ORDER BY sal;  -- sal = 3000: 3명
/* SELECT ename, sal FROM emp WHERE sal >= 3000);*/
-- SCOTT보다 급여가 적은 사원
SELECT ename,sal FROM emp WHERE sal < (SELECT sal FROM emp WHERE ename = 'SCOTT');  -- 11명

-- 실습4) DALLAS에서 근무하는 사원의 이름, 부서 번호를 출력하시오. (서브쿼리 : DEPT01, 메인쿼리 : EMP)
SELECT ename, deptno FROM emp WHERE deptno = (SELECT deptno FROM dept01 WHERE loc = 'DALLAS');  -- 20

--실습5) SALES(영업부) 부서에서 근무하는 모든 사원의 이름과 급여를 출력하시오.(서브쿼리 : DEPT01, 메인쿼리 : EMP)
SELECT ename, sal FROM emp WHERE deptno = (SELECT deptno FROM dept01 WHERE dname = 'SALES');   -- 30

-- 실습6) 평균 급여를 구하는 쿼리문을 서브 쿼리로 사용하여 평균 급여보다 더 많은 급여를 받는 사원이름과 급여 출력
-- AVG(): 평균 함수
-- sal = 인수 (테이블의 컬럼명)
SELECT ename,sal FROM emp WHERE sal > (SELECT avg(sal) FROM emp); -- 2073.214
-- 동일한 테이블: 집계된 통계를 이용하여 조회할 경우
-- 주의: 통계 계산과 조회를 동시에 할 수 없음
/*
SELECT ename,sal
FROM emp
WHERE sal > AVG(sal);
-- 주의: WHERE절에서 그룹함수(집계함수) 사용 불가
-- HAVING 절에서 그룹함수(집계함수) 사용 가능)
*/


-- 2. 다중행 연산자
-- 형식) main query IN/ANY/ALL (sub query);

-- 1) IN(목록)

-- 실습1): 급여가 3,000 이상 받는 사원이 소속된 부서가 10번, 20번이다. 여기서 서브 쿼리의 결과 중에서 하나라도 일치하면 참인 결과를 구하는 IN 연산자와 함께 사용
-- sub query는 IN(목록)의 목록 생성
SELECT ENAME, SAL, DEPTNO
FROM EMP
WHERE DEPTNO IN (SELECT DISTINCT DEPTNO
                                      FROM EMP
                                      WHERE SAL>=3000);  --- IN(20,10)

-- 실습2) 직급(JOB)이 MANAGER인 사람이 속한 부서의 부서 번호와 부서명과 지역을 출력하시오.(DEPT01과 EMP 테이블 이용)
SELECT deptno,dname,loc FROM dept01
WHERE deptno IN (SELECT DISTINCT deptno FROM emp
                                  WHERE job = 'MANAGER');  -- IN(10,20,30)
-- 단일 쿼리문
SELECT deptno,dname,loc FROM dept01 WHERE deptno IN (10,20,30);

-- 2) ALL(AND) 연산자: 검색 결과와 모든 값이 일치하는 경우 -> 크다의 경우 최댓값 기준, 작다의 경우 최솟값 기준

-- 실습1) 30번 소속 사원들 중에서 급여를 가장 많이 받는 사원보다 더 많은 급여를 받는 사람의 이름, 급여를 출력하는 쿼리문 (최댓값 기준)
-- 모든 조건을 만족해야 함
SELECT ENAME, SAL
FROM EMP
WHERE SAL > ALL(SELECT SAL FROM EMP
                                    WHERE DEPTNO =30);  -- sal: 90~2850 (2850 기준)
SELECT ENAME, SAL
FROM EMP
WHERE SAL < ALL(SELECT SAL FROM EMP
                                    WHERE DEPTNO =30);  -- sal: 90~2850 (90 기준)
-- 단일 쿼리문
SELECT ENAME, SAL
FROM EMP
WHERE SAL > 2850;
                                    
-- 실습2) 영업 사원들 보다 급여를 많이 받는 사원들의 이름과 급여와 직급(담당 업무)를 출력하되 영업 사원은 출력하지 않습니다.
SELECT ename,sal,job FROM emp
WHERE sal > ALL(SELECT sal FROM emp
                                  WHERE job = 'SALESMAN')
              AND job != 'SALESMAN';  --4명(1250~1600)
-- 단일 쿼리문
SELECT ENAME, SAL
FROM EMP
WHERE SAL > 1600;
              
-- 3) ANY(OR) 연산자: 검색 결과와 값들 중 하나만이라도 일치하는 경우 -> 크다의 경우 최솟값 기준, 작다의 경우 최댓값 기준

-- 실습1) 다음은 부서번호가 30번인 사원들의 급여 중 가장 작은 값(950)보다 많은 급여를 받는 사원의 이름, 급여를 출력하는 예제를 작성해 봅시다. 
SELECT ename,sal FROM emp
WHERE sal > ANY(SELECT sal FROM emp
                                WHERE deptno = 30);  -- 12명(950~2850)

-- 실습2) 영업 사원들의 최소 급여를 많이 받는 사원들의 이름과 급여와 직급(담당 업무)를 출력하되 영업 사원은 출력하지 않습니다. 
SELECT ename,sal,job FROM emp
WHERE sal > ANY(SELECT sal FROM emp
                                  WHERE job = 'SALESMAN')
              AND job != 'SALESMAN';  -- 7명(1250~1600)