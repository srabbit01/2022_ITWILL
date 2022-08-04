-- [1] SUBQUERY 이용 테이블 생성 
-- DEPT 테이블의 부서위치(LOC)가 'BOSTON'을 제외한 나머지 내용으로 DEPT_TEST 테이블을 생성하시오. 
DROP TABLE dept_test PURGE;
CREATE TABLE dept_test
AS
SELECT * FROM dept WHERE loc != 'BOSTON';

-- [2] SUBQUERY 이용 레코드 수정 
-- DEPT 테이블의 부서 번호 40번의 지역명을 이용하여 DEPT_TEST 테이블의 부서번호 30번 부서의 지역명을 변경하시오.
UPDATE dept_test
SET loc = (SELECT loc FROM dept_test WHERE deptno = 40)
WHERE deptno = 30;

-- [3] SUBQUERY 이용 레코드 수정 
-- DEPT 테이블의 부서 번호 20번의 부서명과 지역명을 이용하여 DEPT_TEST 테이블의 부서번호 10번의 부서명과 지역명을 변경하시오.
UPDATE dept_test
SET (dname,loc) = (SELECT dname,loc FROM dept_test WHERE deptno = 20)  -- RESEARCH, DALLAS
WHERE deptno = 10;
SELECT * FROM dept_test;

-- [4] SUBQUERY이용 테이블 만들기 
-- EMP 테이블에서 사번, 이름, 급여, 수당, 부서번호 칼럼의 내용으로 EMP_TEST 테이블을 생성하시오. 
CREATE TABLE emp_test
AS
SELECT empno,ename,sal,comm,deptno FROM emp;

-- [5] SUBQUERY이용 레코드 삭제 
-- 'RESEARCH'부서에서 근무하는 모든 사원을 삭제하시오. 
-- 서브쿼리 : DEPT_TEST 테이블
-- 메인쿼리 : EMP_TEST 테이블 

-- deptno = 20인 RESEARCH 부서 삭제
SELECT * FROM emp_test;
DELETE FROM emp_test
WHERE deptno IN(SELECT deptno FROM dept_test WHERE deptno=20);

-- 부서명이 같은 것이 여러개인 경우
SELECT * FROM emp_test;
DELETE FROM emp_test
WHERE deptno IN(SELECT deptno FROM dept_test WHERE dname = 'RESEARCH');

-- [6] SUBQUERY이용 레코드 삭제 
-- 사원의 이름이 'M'로 시작하는 모든 레코드를 삭제하시오. 
-- 서브쿼리 : EMP 테이블
-- 메인쿼리 : EMP_TEST 테이블 
DELETE FROM emp_test
WHERE ename IN(SELECT ename FROM emp WHERE ename  LIKE 'M%');

-- [7] SUBQUERY이용 테이블 만들기 
-- 동물 보호소 테이블에서  입양 간 동물을 제외하여 새 테이블을 생성하시오.
-- 동물 보호소 테이블 : ANIMAL_INS
-- 입양 동물 테이블 : ANIMAL_OUTS
-- 새 테이블 : ANIMAL_INS_FINAL
CREATE TABLE animal_ins_final
AS
SELECT * FROM animal_ins WHERE aid NOT IN(SELECT aid FROM animal_outs);  -- 입양 동물: 1001, 1003, 1004, 1005, 1006

SELECT * FROM animal_ins_final;  -- 4마리 동물(5마리 입양 간 동물 제외)

-- [8] SUBQUERY이용 레코드 삽입 
-- 입양 간 동물 중에서 2020년도 8월 이후에 입양 간 동물을 새 테이블에 삽입하시오.
-- 입양 동물 테이블 : ANIMAL_OUTS
-- 새 테이블 : ANIMAL_INS_FINA
-- <조건> 삽입할 칼럼의 내용이 없는 경우는 NULL 처리함 

-- 1. 날짜형식 적용 날짜 칼럼 조회  
-- to_char(변수,'출력양식'): 원하는 양식으로 만들어 조회
-- 원래는 년도 끝 두자리만 보이는데, '2020년'임을 확인하기 위해 양식 만들기
SELECT ANIMAL_OUTS.*, TO_CHAR(DATETIME, 'yyyy-mm-dd') FROM ANIMAL_OUTS;
-- 2020년 8월 이후에 입양된 동물: 3마리

-- 2. 레코드 삽입 : CONDITION 칼럼 NULL
SELECT * FROM animal_outs;
INSERT INTO animal_ins_final
SELECT * FROM animal_ins WHERE aid IN(SELECT aid FROM animal_outs WHERE TO_CHAR(DATETIME, 'yyyy-mm') > '2020-08');
-- ANIMALS_OUTS을 그대로 입력하는 경우
INSERT INTO aniaml_ins_final(aid,atype,datetime,name)  -- CONDITION을 NULL 처리
SELECT * FROM animal_outs WHERE datetime > '20/08/01';  -- 3마리 추가
-- 동물 3마리 추가

-- 3. 레코드 확인 
SELECT * FROM animal_ins_final;

-- [9] SUBQUERY이용 테이블 만들기 & 레코드 삭제  
-- student 테이블을 이용하여 student2 테이블을 만들고, student 테이블에서 
-- 주 전공(DEPTNO1)이 201인 학생 중 77년도 출생한 학생을 student2 테이블에서 삭제하시오. 

-- 1. 테이블 만들기 
CREATE TABLE student2
AS
SELECT * FROM student;

-- 2. 레코드 삭제 
DELETE FROM student2 WHERE deptno1 = 201 AND substr(birthday,1,2) = '77';

-- 3. 레코드 확인                  
SELECT * FROM student2;

-- [10] SUBQUERY이용 레코드 수정  
-- student 테이블을 이용하여 주전공이 102인 학생 중에서 부전공(DEPTNO2)이 NULL인 학생을
-- 조회하고, student2 테이블에서 해당 학생의 부전공을 최대 자릿수 만큼 9로 채워서 수정시오.

-- 1. 테이블의 칼럼 자릿수 확인 
SELECT * FROM student WHERE deptno1=102 AND deptno2 IS NULL;
DESC student2;  -- 최대 자릿수 9개 확인

-- 2. 레코드 수정 
UPDATE student2
SET deptno2 = 999
WHERE studno IN(SELECT studno FROM student WHERE deptno1 =102 AND deptno2 IS NULL);

-- 3. 레코드 확인 
SELECT * FROM student2 WHERE deptno1 =102;

COMMIT;