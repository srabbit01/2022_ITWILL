/*
 * 주요 함수 
 * 작업 대상 테이블 : STUDENT, EMP, PROFESSOR 
 */

--Q1. STUDENT 테이블에서 JUMIN 칼럼을 사용하여 
-- 태어난 달이 8월인 사람의 이름과 생년월일 출력하기
-- 힌트 : substr() 함수 이용
SELECT name, birthday FROM student WHERE SUBSTR(jumin,3,2) = '08';

--Q2. EMP 테이블에서 입사일이 짝수인 사람들을 검색하기
-- 힌트 : mod() 함수 이용
SELECT * FROM emp WHERE MOD(SUBSTR(hiredate,7,2),2) = 0;

--Q3. Professor 테이블에서 교수명, 급여, 보너스, 연봉을 출력하기 
-- 조건) 연봉 = pay*12+bonus 으로 계산, bonus가 없으면 pay*12 처리
-- 힌트 : nvl2() 함수 이용
SELECT * FROM professor;
SELECT name,pay,bonus,NVL2(bonus,pay*12+bonus,pay*12) 연봉 FROM professor;

--Q4. Professor 테이블에서 교수명, 학과명을 출력하되 
--  deptno가 101번이면 ‘컴퓨터 공학과’, 102번이면 
-- ‘멀티미디어 공학과’, 103번이면 ‘소프트웨어 공학과’, 
-- 나머지는 ‘기타학과’로 출력하기
-- decode()함수 이용
SELECT name,DECODE(deptno,101,'컴퓨터 공학과',102,'멀티미디어 공학과',103,'소프트웨어 공학과','기타학과') FROM professor;

--Q5. 다음 SELECT문을 실행하면 'AA' 테이블의 제약조건에 관한 내역을 
-- 확인할 수 있다. 이때 제약조건을 나타내는 4개의 영문을 아래와 같이 
--  풀 네임(full name)으로 변경하여 출력하시오.
SELECT CONSTRAINT_NAME, DECODE(CONSTRAINT_TYPE,'P','PRIMARY KEY','U','UNIQUE KEY','C','CHECK OR NOT NULL','R','FOREIGN KEY'), SEARCH_CONDITION
FROM USER_CONSTRAINTS 
WHERE TABLE_NAME = 'AA';    
/*
 제약조건 -> 풀 네임 
  'P', -> 'PRIMARY KEY',
  'U' -> 'UNIQUE KEY',
  'C' -> 'CHECK OR NOT NULL',
  'R', -> 'FOREIGN KEY'
*/

-- 'AA' 테이블의 제약조건 확인 
SELECT CONSTRAINT_NAME, CONSTRAINT_TYPE, SEARCH_CONDITION
FROM USER_CONSTRAINTS 
WHERE TABLE_NAME = 'AA';    