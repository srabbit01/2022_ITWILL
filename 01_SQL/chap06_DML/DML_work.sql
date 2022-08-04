-- DML_work.sql

/*
INSERT/UPDATE/DELETE: COMMIT 대상(db 반영)
ROLLBACK: INSERT/UPDATE/DELETE 명령 이전 상태 복원
SELECT문: COMMIT 대상이 아님(데이터 구조 변환 없음)
1) 단일 쿼리 이용법
2) 서브 쿼리 이용법
    INSERT/UPDATE/DELETE  -- 2차 실행: 메인쿼리
    SELECT절;  -- 1차 실행: 서브쿼리
  주의: AS 명령어 없음
*/

-- 실습 테이블 생성
DROP TABLE dept01 purge;
CREATE TABLE dept01  -- 구조 복제
AS
SELECT * FROM dept WHERE 0=1;


-- 1. 레코드 삽입: INSERT

-- 1) 단일 쿼리 이용
-- (1) 칼럼명 명시
INSERT INTO dept01(deptno,dname,loc) VALUES(10,'ACCOUNTING','NEW YORK'); 
-- (2) 칼럼명 생략
INSERT INTO dept01 VALUES(20,'RESEARCH','DALLAS');  -- 전체 칼럼에 레코드값 넣을 경우
SELECT * FROM dept01;

-- 문제1
-- 테이블 생성
CREATE TABLE sam01
AS
SELECT * FROM emp WHERE 1=0;
-- 테이블에 데이터 추가
INSERT INTO sam01(empno,ename,job,sal) VALUES(1000,'APPLE','POLICE',10000);
INSERT INTO sam01(empno,ename,job,sal) VALUES(1010,'BANANA','NURSE',15000);
INSERT INTO sam01(empno,ename,job,sal) VALUES(1020,'ORANGE','DOCTOR',25000);

-- NULL값 삽입
-- 암시적 NULL 입력
DESC dept01;
INSERT INTO dept01(deptno,dname) VALUES(30,'SALES');  -- LOC 생략 = NULL값 삽입
-- 명시적 NULL 입력: NULL 이용
INSERT INTO dept01 VALUES(40,'OPERATIONS',NULL);
-- 명시적 NULL 입력: ''
INSERT INTO dept01 VALUES(50,'','CHICAGO');
SELECT * FROM dept01;

-- 문제1
-- 테이블에 데이터 추가
INSERT INTO sam01(empno,ename,job,sal) VALUES(1030,'VERY','',25000);
INSERT INTO sam01(empno,ename,job,sal) VALUES(1040,'CAT','',2000);
SELECT * FROM sam01;

-- 2) 서브쿼리 이용
INSERT INTO dept02
SELECT * FROM dept;  -- 주의: AS 없음
-- 문제2
INSERT INTO sam01
SELECT * FROM emp WHERE deptno = 10;

-- 3) 다중 테이블 다중행 입력
-- (1) 테이블 준비: EMP_HIR, EMP, MGR
-- 사원 고용일 관리 테이블
CREATE TABLE emp_hir
AS
SELECT empno,ename,hiredate FROM emp WHERE 0=1;
-- 사원 직속 상사 관리 테이블
CREATE TABLE emp_mgr
AS
SELECT empno,ename,mgr FROM emp WHERE 0=1;
-- (2) 여러 테이블에 레코드 추가
INSERT ALL
INTO emp_hir VALUES(empno,ename,hiredate)
INTO emp_mgr VALUES(empno,ename,mgr)
SELECT empno,ename,hiredate,mgr FROM emp WHERE deptno=20;
-- (3) 삽입 확인
SELECT * FROM emp_hir;
SELECT * FROM emp_mgr;


-- 3. 레코드 수정: UPDATE

-- 1) 단일 쿼리 이용
SELECT * FROM emp01;
-- 전체 레코드 수정
UPDATE emp01 SET  deptno=30;
UPDATE emp01 SET sal = sal*1.1;
UPDATE emp01 SET hiredate = sysdate;

-- 특정행 대상으로 수정
UPDATE emp01 SET deptno = 30 WHERE deptno = 10;  -- 기존의 10번 부서가 30번으로 변경
UPDATE emp01 SET sal = sal*1.1 WHERE sal >= 3000;  -- 급여가 3000 이상인 사람 10% 연봉 인상
UPDATE emp01 SET hiredate = sysdate WHERE substr(hiredate,1,2) = '87';
-- substr(변수,시작위치,끝위치): 문자열/날짜 자르기
-- 문제2
UPDATE sam01 SET sal = sal-5000 WHERE sal>=10000;


-- 2개 이상의 칼럼 UPDATE
UPDATE emp01 SET deptno = 20, job = 'MANAGER'
WHERE ename = 'SCOTT';
UPDATE emp01 SET hiredate = sysdate, sal = 50, comm =4000
WHERE ename = 'SCOTT';
SELECT * FROM emp01 WHERE ename = 'SCOTT';

-- 2) 서브 쿼리를 이용한 레코드 수정
-- 10번 부서의 위치를 20번 부서의 위치로 변경
UPDATE dept01
SET loc = (SELECT loc FROM dept01 WHERE deptno=10) WHERE deptno=20;  -- 단일행
-- 단일 쿼리문
UPDATE dept01 SET loc = 'NEW YORK' WHERE deptno = 20;
-- 문제3
-- sam02 테이블 생성
CREATE TABLE sam02
AS
SELECT ename,sal,hiredate,deptno FROM emp;
-- DALLAS에 위치한 부서 소속 사원들의 급여를 1000 인상
UPDATE sam02 SET sal = sal + 1000 WHERE deptno = (SELECT deptno FROM dept WHERE loc = 'DALLAS');
SELECT * FROM sam02;

-- 다른 형식을 이용하여 수정
UPDATE dept01
SET (dname,loc) = (SELECT dname,loc
                                    FROM dept01
                                    WHERE DEPTNO = 10)  -- ACC, NEW YORK
WHERE deptno = 50;
-- 문제4
UPDATE sam02
SET (sal,hiredate) = (SELECT sal,hiredate FROM sam02 WHERE ename = 'KING');  -- 5000, 81/11/17
SELECT * FROM sam02;
-- WHERE절 없음: 모든 사원 수정


-- 4. 레코드 삭제: DELETE

-- 1) 단일 쿼리문 이용
DELETE FROM dept01
WHERE deptno = 30;
SELECT * FROM dept01;
DELETE FROM dept01;  -- 주의: 전체 행 삭제

-- 문제5: sam01 테이블에서 직책이 정해지지 않은 사원을 삭제하시오.
SELECT * FROM sam01;
DELETE FROM sam01 WHERE job IS NULL;

-- 2) 서브 쿼리문 이용
DELETE FROM emp01
WHERE deptno = (SELECT deptno FROM dept WHERE dname = 'SALES');  -- 부서번호:30
SELECT * FROM emp01;


-- DB 반영
COMMIT;