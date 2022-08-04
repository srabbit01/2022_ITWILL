/*
  집합 함수(COUNT,MAX,MIN,SUM,AVG) 
  작업 대상 테이블 : EMP, STUDENT, PROFESSOR
*/

--Q1. PROFESSOR 테이블에서 POSITION의 수 출력하시오.
SELECT COUNT(DISTINCT position) FROM professor;  -- 3

--Q2. EMP 테이블에서 소속 부서별 최대 급여와 최소 급여를 구하시오.
SELECT deptno 부서번호,MAX(sal) 최대급여,MIN(sal) 최소급여 FROM emp GROUP BY deptno;

--Q3. EMP 테이블에서 전체 사원의 급여에 대한 분산과 표준편차를 구하시오.
SELECT ROUND(COUNT(sal),2) 급여사원수,ROUND(STDDEV(sal),2) 표준편차, ROUND(VARIANCE(sal),2) 분산 FROM emp;

-- Q4. EMP 테이블에서 각 부서별 사원수와 수당을 받는 사원수를 카운트 하시오.
SELECT deptno 부서번호,COUNT(*) 전체사원수,COUNT(comm) 수당사원수 FROM emp GROUP BY deptno;

--<출력 결과>
/*
부서번호     전체사원수     수당사원수
30        6        4  
20        5        0
10        3        0 
*/

-- Q5. 전체 사원의 수당(COMM)의 평균을 계산하시오.(단, 수당이 0원인 사원은 제외하고, 소숫점 이하는 절사)  
SELECT FLOOR(AVG(comm)) 평균수당 FROM emp WHERE comm > 0;  -- 773

--Q6. PROFESSOR 테이블에서 학과별 급여(pay) 평균이 400 이상인 레코드를 출력하시오.
SELECT * FROM professor;
SELECT deptno 학과번호,AVG(pay) 급여평균 FROM professor
GROUP BY deptno HAVING AVG(pay) >= 400;

--Q7. PROFESSOR 테이블에서 학과별,직위별 급여(pay)의 평균을 구하시오.
SELECT deptno 학과번호, ROUND(AVG(pay),2) 학과별급여평균 FROM professor GROUP BY deptno;
SELECT position 직위,ROUND(AVG(pay),2) 직위별급여평균 FROM professor GROUP BY position;
SELECT deptno 학과번호,position 직위, ROUND(AVG(pay),2) 급여평균 FROM professor
GROUP BY deptno,position   -- 1차: 학과별, 2차: 직위별
ORDER BY deptno,position;

--Q8. STUDENT 테이블에서 grade별로 weight, height의 평균값, 최댓값, 최솟값을 
-- 구한 결과에서 키의 평균이 170 이하인 레코드를 출력하시오.
SELECT grade 학년,ROUND(AVG(height),2) 키평균,ROUND(MAX(height),2) 키최대,ROUND(MIN(height),2) 키최소,ROUND(AVG(weight),2) 몸무게평균,ROUND(MAX(weight),2) 몸무게최대,ROUND(MIN(weight),2) 몸무게최소
FROM student
GROUP BY grade
HAVING AVG(height) <= 170;