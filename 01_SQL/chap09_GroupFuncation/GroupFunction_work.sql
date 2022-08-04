-- GroupFunction_work.sql

/*
그룹 함수: 그룹별 통계(집계)를 구하는 함수
- 그룹: 집단 혹은 범주형을 의미
- 통계/집계 함수: 복수행(vector) 입력 -> 상수(scala) 출력 = 차원 축소
- 일반 숫자 함수 (한 개의 상수) VS 그룹 함수 (여러 개의 상수)
- 주의: SELECT절 혹은 WHERE절에서 일반 칼럼 함수와 그룹 함수는 함께 사용 불가
- 그룹 칼럼과 그룹 함수는 함께 사용 가능
*/

-- 1. 그룹 함수

-- 1) SUM 함수
SELECT SUM(sal) FROM emp;  -- 29025
SELECT SUM(comm) FROM emp;  -- NULL 자동 제외

-- 2) AVG 함수: 대표값(평균,중앙값,최빈값)
SELECT AVG(sal) FROM emp;  -- 2073 = SUM(sal) / N
SELECT AVG(comm) FROM emp;  -- 550 = SUM(comm) / N(NULL이 아닌 값의 개수)

-- 문제1: ‘SCOTT’사원이 소속된 부서의 급여 합계와 평균을 구하시오.(서브쿼리이용)
SELECT SUM(sal),AVG(sal) FROM emp  -- 10875, 2178
WHERE deptno = (SELECT deptno FROM emp WHERE ename = 'SCOTT');  -- 20

-- 3)  MIN, MAX 함수: 범위(range)
SELECT MAX(sal), MIN(sal) FROM emp;  -- 5000, 800
SELECT ename,MAX(sal),MIN(sal) FROM emp;  -- 오류: 일반 칼럼(함수)과 그룹 함수는 함께 사용 불가

-- 문제2) 가장 최근에 입사한 사원의 입사일과 입사한지 가장 오래된 사원의 입사일을 출력하는 쿼리문을 작성하시오. (MAX, MIN 함수이용)
SELECT MAX(hiredate) "최근 입사일",MIN(hiredate) "오래된 입사일" FROM emp; 

-- 4) COUNT 함수
SELECT COUNT(comm) FROM emp; -- 4: NULL 제외
SELECT COUNT(*),COUNT(comm) FROM emp;  -- 14, 4
SELECT COUNT(job) 업무수 FROM emp;  -- 14
SELECT COUNT(DISTINCT job) 업무수 FROM emp;  -- 업무의 개수(중복X): 5

-- 문제3) 30번 부서 소속 사원 중에서 커미션을 받는 사원의 수를 구하시오.
SELECT COUNT(*) 사원수 FROM emp WHERE deptno=30 AND comm>30;  -- 3명
-- 오답
SELECT COUNT(*) 사원수 FROM emp WHERE deptno = 30 AND comm IS NOT NULL;  -- 4명 = 0원 받는 사람 포함

-- 5) 산포도 함수: 분산/표준편차 = 평균에서 분산된 정도)
-- 분산과 표준편차가 작다는 의미: 각 변량이 평균에 밀집되어 있음
-- (1) 보너스 분산
SELECT VARIANCE(bonus) FROM professor;  -- 951.11
-- (2) 보너스 표준편차
SELECT STDDEV(bonus) FROM professor;  -- 30.84
-- (3) 분산 = 표준편차의 제곱(POWER)
SELECT POWER(STDDEV(bonus),2) FROM professor;  -- 951.11
-- (4) 표준편차 = 분산의 제곱근(SQRT)
SELECT SQRT(VARIANCE(bonus)) FROM professor;  -- 30.84
/*
모분산 = SUM((X - mu) ^ 2) / N = (전체 - 모평균)합의 제곱 / 모집단의 갯수 (mu: 모평균, N: 모집수)
표본(Sample)분산 = SUM((X - X') ^ 2) / n-1 (X': 표본평균, n: 표본수)
*/
-- (1) 변량의 평균
SELECT AVG(bonus) FROM professor;  -- 78
-- (2) (변량-평균)^2
SELECT POWER((bonus-78),2) FROM professor;
-- (3)  SUM((변량-평균)^2)
SELECT SUM(POWER((bonus-78),2)) FROM professor;  -- 8560
-- (4) 모분산 구하기
SELECT SUM(POWER((bonus-78),2))/COUNT(bonus) FROM professor;  -- 856
-- 위의 분산값과 다르기에 모분산이 아님을 알 수 있음
-- (5) 표본분산 구하기
SELECT SUM(POWER((bonus-78),2))/(COUNT(bonus)-1) FROM professor;  -- 951.11
-- 따라서, 위 분산값이 표본 분산임을 알 수 있음

-- 2. GROUP BY절
/*
GROUP BY 그룹 칼럼 (범주형)
- SELECT절에서 그룹 칼럼과 그룹 함수는 함께 사용할 수 있음
*/

-- 1) 그룹 칼럼은 SELECT절에서 사용 가능
SELECT deptno FROM emp
GROUP BY deptno;  -- 그룹 칼럼
-- 2) 그룹 칼럼과 그룹 함수 사용 가능
SELECT deptno 부서번호,ROUND(AVG(sal),2) 급여평균 FROM emp GROUP BY deptno ORDER BY 급여평균;
SELECT deptno 부서번호,MAX(sal) 최대급여,MIN(sal) 최소급여 FROM emp GROUP BY deptno;

-- 문제4) 부서별로 가장 급여를 많이 받는 사원의 정보(사원번호, 사원이름, 급여, 부서번호)를 출력하시오.(IN, MAX(),GROUP BY, subQuery이용)
SELECT * FROM emp;
SELECT empno 사원번호, ename 사원이름, sal 급여, deptno 부서번호
FROM emp
WHERE sal IN(SELECT MAX(sal) FROM emp GROUP BY deptno);  -- 다중행 SELECT

-- 3. HAVING 조건
/*
- 일반 조건절: WHERE 조건식
- GROUP BY문 조건절: HAVING 조건식
*/
SELECT deptno,AVG(sal) FROM emp
GROUP BY deptno
HAVING AVG(sal)>=2000;

SELECT deptno,MAX(sal),MIN(sal) FROM emp
GROUP BY deptno
HAVING MAX(sal)>2900;

-- 문제4) <문제4>의 결과에서 'SCOTT' 사원을 제외하고,  급여(SAL)를 내림차순으로 정렬하시오.
SELECT empno 사원번호, ename 사원이름, sal 급여, deptno 부서번호
FROM emp
WHERE sal IN(SELECT MAX(sal) FROM emp GROUP BY deptno)  -- 서브쿼리는 GROUP BY를 사용했기에 일반 칼럼 사용 불가?
              AND ename != 'SCOTT'
ORDER BY sal DESC;
-- 오류
SELECT empno 사원번호, ename 사원이름, sal 급여, deptno 부서번호
FROM emp
WHERE sal IN(SELECT MAX(sal) FROM emp GROUP BY deptno HAVING ename != 'SCOTT')
ORDER BY sal DESC;