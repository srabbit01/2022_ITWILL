-- Function_work.sql

/*
함수(Fuction)
- 의미: 특정 기능을 정의해 놓은 것으로 필요시 호풀
- 함수는 일정한 형식을 띰 (인수의 유형에 따라 세분화)
- SQL문에서 함수 사용 위치: SELECT절, WHERE절
- 형식: 함수명([인수1,인수2,...])
- 사용자가 직접 인수 입력
*/

-- 1. 숫자 함수

-- 1) ABS 함수: 절댓값 반환
SELECT -10,ABS(-10) FROM DUAL;  -- -10,10
-- DUAL: 연산 결과 테스트용 의사 테이블

-- 2) FLOOR 함수: 소숫점 이하 절사
SELECT 24.5678, FLOOR(34.5678) FROM DUAL;
SELECT  FLOOR(34.5678) FROM DUAL;  -- 34

-- 3) ROUND 함수: 소숫점 이하 반올림
SELECT 34.5678, ROUND(34.5678) FROM DUAL;
SELECT ROUND(34.5678) FROM DUAL;  --35
-- ROUND(대상,자릿수): 실수 위치
SELECT 34.5678, ROUND(34.5678, 2) FROM DUAL;
SELECT ROUND(34.5678, 2) FROM DUAL;  -- 34.57
-- ROUND(대상,-자릿수): 정수 위치
SELECT 34.5678, ROUND(34.5678, -1) FROM DUAL;
SELECT ROUND(34.5678, -1) FROM DUAL;  --30


-- 4) TRUNC 함수: 지정한 위치 절사
SELECT TRUNC(34.5678), TRUNC(34.5678, 2), TRUNC(34.5678, -1) FROM DUAL; -- 34, 34.56, 30

-- 5) MOD 함수: 나머지값 반환
SELECT MOD (27, 2), MOD (27, 5), MOD (27, 7) FROM DUAL;  -- 1, 2, 6
/*
- 짝수/홀수 판별
10/2 -> 0 (짝수)
11/2 -> 1 (홀수)
- 배수 판별
10/5 -> 0 (배수)
11/5 -> 1 (배수X)
*/

-- 실습1) 사번이 홀수인 사람들을 검색해 보십시오. (EMP 테이블)
SELECT * FROM emp WHERE MOD(empno,2) = 1;  -- 나머지가 1인 경우 (홀수)
SELECT * FROM emp WHERE MOD(empno,2) != 0;  -- 나머지가 0이 아닌 경우 (홀수)
SELECT * FROM emp WHERE MOD(empno,2) = 0;  -- 나머지가 0인 경우 (짝수)

-- 6) LOG 함수: 로그값 -> 지수값 
-- 유형: 자연로그(밑수 e, 2), 사용로그(밑수 10)
-- 자연로그: 밑수 2일때
SELECT log(2,8) FROM DUAL; -- 8 = 2^3  -- 2.9999 = 3에 근사한 값이 반환
-- 자연로그: 밑수 e일때
SELECT EXP(1) FROM DUAL;  -- e = 2.71828
SELECT LOG(EXP(1),8) FROM DUAL;  -- 8 = e^2.07944

-- 7) EXP 함수: 지수값 -> 로그값
SELECT EXP(1) FROM DUAL;
SELECT EXP(2.07944) FROM DUAL;  -- 7.99999 = 8

/*
로그 함수 vs 지수 함수 역함수 관계
f1(x): x -> y
f2(x): y -> x

로그함수: 지수값 반환, 완만한 변화(정규화)
지수함수: 로그값 반환, 급격한(지수적) 변화
*/
-- 정규화
SELECT LOG(2,1),LOG(2,100),LOG(2,100000) FROM DUAL; -- 0 , 6.64, 16.6
SELECT EXP(1),EXP(10),EXP(100) FROM DUAL;  -- 2.71, 22026, 26881171418161354484126255515800135877150000

-- 8) POWER 함수: 제곱
SELECT POWER(2,8) FROM DUAL;  -- 256

-- 9) SQRT 함수: 제곱근(루트)
SELECT SQRT(49) FROM DUAL;  -- 7


-- 2. 문자 처리 함수

-- 1) UPPER 함수: 대문자 변경
SELECT 'Welcome to Oracle', UPPER('Welcome to Oracle') FROM DUAL;

-- 2) LOWER 함수: 소문자 변경
SELECT 'Welcome to Oracle', LOWER('Welcome to Oracle') FROM DUAL;

-- 3) INITCAP 함수: 첫글자 대문자 변경
SELECT 'WELCOME TO ORACLE', INITCAP('WELCOME TO ORACLE') FROM DUAL;

-- 실습2) 다음과 같이 쿼리문을 구성하면 직급이 'manager'인 사원을 검색할까?
SELECT EMPNO, ENAME, JOB
FROM EMP
WHERE JOB='manager';

-- 4) LENGTH 함수: 문자열의 길이 반환
SELECT LENGTH('Oracle'), LENGTH('오라클') FROM DUAL;  -- 6, 3

-- 5) LENGTH 함수: 문자열의 바이트 수 반환
-- 영문자 1자 1byte, 한글 1자 3byte
SELECT LENGTHB('Oracle'), LENGTHB('오라클') FROM DUAL;  -- 6, 9

-- 6) SUBSTR 함수: 사용자가 지정한 부분 문자열 반환
-- SUBSTR(대상,시작위치,추출개수)
SELECT SUBSTR('Welcome to Oracle', 4, 3) FROM DUAL;  -- 왼쪽 기준: com
SELECT SUBSTR('Welcome to Oracle', -4, 3) FROM DUAL;  -- 오른쪽 기준: acl

-- 입사년도 -> 연도, 월 구문: 'yy/mm/dd'
SELECT SUBSTR(HIREDATE,1,2) 년도, SUBSTR(HIREDATE,4,2) 달 FROM emp;

-- 실습3) 9월에 입사한 사원을 출력하시오. (EMP 테이블)
SELECT * FROM emp WHERE SUBSTR(hiredate,4,2) = '09';
SELECT * FROM emp WHERE SUBSTR(hiredate,4,2) ='02';

-- 7) TRIM 함수: 앞/뒤 특정 문자 또는 공백 제거
-- 문자 제거
SELECT TRIM('a' FROM 'aaaaOracleaaaa') FROM DUAL;
-- 공백 제거
SELECT TRIM(' Oracle ') FROM DUAL;

-- 8) REPLACE 함수
-- 형식: REPLACE(칼럼명,'찾을문자','변환문자')
SELECT REPLACE('홍길동', '홍', '김') FROM DUAL;  -- 김길동

-- ex) 주민번호 뒷자리 마스킹(masking): 123456-*******
CREATE TABLE jumin_student
AS
SELECT * FROM student;
SELECT * FROM jumin_student;
-- 방법1
SELECT name, REPLACE(jumin,jnum,'*******')
FROM (SELECT student.*,SUBSTR(jumin,7,7) AS jnum FROM student)  -- 테이블 -> 서브쿼리 대체
ORDER BY name;
-- 서브쿼리의 칼럼과 별칭은 메인쿼리에서도 사용 가능
-- 방법2
UPDATE jumin_student SET jumin = REPLACE(jumin,SUBSTR(jumin,7,7),'*******');


-- 3. 날짜 함수

-- 1) SYSDATE 함수
SELECT SYSDATE FROM DUAL;
SELECT SYSDATE-1 어제, SYSDATE 오늘, SYSDATE+1 내일 FROM DUAL;

-- 2) MONTHS_BEWTEEN 함수
SELECT ename, SYSDATE, hiredate, round(MONTHS_BETWEEN(SYSDATE,HIREDATE)) "근무 개월수" FROM emp ORDER BY "근무 개월수";

-- 4. 형 변환 함수
/*
- TO_CHAR(): 날짜, 숫자 -> 양식(format)을 이용하여 문자형 변환
- TO_DATE(): 숫자, 문자 -> 양식(format)을 이용하여 날짜형 변환
- TO_NUMBER(): 날짜, 문자 -> 양식(format)을 이용하여 숫자형 변환
*/

-- 1) TO_CHAR()
SELECT SYSDATE,TO_CHAR(SYSDATE,'YYYY-MM-DD') FROM DUAL;
SELECT HIREDATE,TO_CHAR(HIREDATE,'YYYY/MM/DD') FROM emp;

-- 시간 관련 양식
SELECT TO_CHAR(SYSDATE,'YYYY/MM/DD, HH24:MI:SS') FROM DUAL;

-- 숫자 -> 문자형 변환
SELECT ename,sal,TO_CHAR(sal,'L999,999') FROM emp;  -- 1500 -> \1,500
 -- 시스템 언어 출처에 해당하는 국가의 화폐 단위 자동 출력
SELECT ename,sal,TO_CHAR(sal,'L000,000') FROM emp;  -- 1500 -> \001,500: 값이 부족하면 공백으로 채워짐

-- 2) TO_DATE 함수
SELECT ename,hiredate from emp
WHERE hiredate = TO_DATE(19810220,'YYYYMMDD');  -- 숫자 -> 날짜형

SELECT TRUNC(SYSDATE-TO_DATE('2008/01/01','YYYY/MM/DD'))
FROM DUAL;  -- 문자 -> 날짜형 변환

-- 3) TO_NUMBER 함수: 문자 -> 숫자형 변환
SELECT '20000' - '10000' FROM DUAL;  -- 내부에서 ASCII 코드로 변환하여 연산 가능
SELECT '20,000' - '10,000' FROM DUAL;  -- 오류: 문자로 취급되기 때문에 변환 필요
SELECT TO_NUMBER('20,000','99,999') - TO_NUMBER('10,000','99,999') FROM DUAL;  -- 10,000


-- 5. NULL 처리 함수
/*
NVL(대상,대체값)
NVL2(대상,NULL(X),NULL(O))
*/
-- NVL 함수 사용
SELECT name,sal*12+NVL(comm,0) 연봉 FROM emp;
-- NVL2 함수 사용
SELECT name,sal*12+NVL2(comm,comm,0) 연봉 FROM emp;
-- 수당의 결측치 -> 수당 평균 대체
SELECT AVG(comm) FROM emp;
SELECT ename,sal,NVL2(comm,comm,550) 연봉 FROM emp;
SELECT ename,sal,NVL2(comm,comm,AVG(comm)) 연봉 FROM emp;  -- 주의: 통계 함수와 일반 함수는 결합하여 쓸 수 없음

-- 6. DECODE 함수
/*
ENCODE <-> DECODE
ENCODE: 자연어, 인간어 -> 기계어 (암호화)
DECODE: 기계어 -> 자연어, 인간어(암호해독)
- DECODE는 특정 값을 해독해주는 역할을 함
*/
SELECT * FROM emp;
SELECT ename, job, deptno, DECODE(deptno,10,'기획실',20,'연구실','기타') 부서명 FROM emp;