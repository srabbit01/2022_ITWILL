-- select_work.sql

-- 1. 전체 검색(특정 컬럼 검색)
-- 1) * = 전체 컬럼을 대신
SELECT * FROM emp;

-- 2) 특정 컬럼 조회: 전체 레코드(열) 길이는 변하지 않으나 전체 컬럼(행) 길이는 특정 갯수로 변환
SELECT empno,ename,job FROM emp;
-- 특정 컬럼 조회 + 사칙 연산을 이용한 새로운 컬럼 추가 = 파생변수: 사원의 급여에 300 추가
-- 주의: 산술 표현식은 레코드가 숫자인 경우에만 사용 가능
-- 파생변수: 기존 컬럼에 계산을 통해 새로운 컬럼을 도출하는 것
SELECT ename,sal,sal+300 FROM emp;
-- 산술표현: + = 덧셈, - = 뺄셈, * = 곱셈, / = 나눗셈
-- 특정 컬럼 조회 + 사원의 급여 10% 인상
SELECT ename,sal,sal*1.1 FROM emp;

-- 3) null 처리
-- null값 = 값이 없는 상태 (0 혹은 공백과 다름)
-- null 처리전,
-- 연산 입력 값 중에 null값이 하나라도 있으면 null값 출력
-- 0의 경우 값이 산술 출력
SELECT empno,ename,sal,comm,sal+comm/100 FROM emp;
-- NVL(칼럼,대체값)으로 null값 대체
SELECT ename,sal,NVL(comm,0),sal*12+NVL(comm,0) FROM emp;

-- 4) 파생변수의 별칭 만들기: alias
-- 계산식에서 많이 이용
SELECT ename,sal,NVL(comm,0),sal*12+NVL(comm,0) AS 연봉 FROM emp;
-- 'AS'는 생략이 가능
SELECT ename,sal,NVL(comm,0),sal*12+NVL(comm,0) 연봉 FROM emp;
-- 별칭 사이에 띄어쓰기(공백)가 있는 경우, 쌍따옴표(" ")로 묶어야 함
SELECT ename,sal,NVL(comm,0),sal*12+NVL(comm,0) "사원 연봉" FROM emp;
-- 예제: emp 테이블에서 ename 이름으로 sal을 급여로 출력
SELECT ename AS 이름, sal AS 급여 FROM emp;

-- 5) 연결 연산자( ||): 두개의 컬럼을 연결
-- 주로 여러개의 컬럼을 하나의 문장 형식으로 연결할 때 사용
SELECT ename || ' ' || job AS "employees" FROM emp;
-- 두 컬럼 사이의 공백 크기는 홑따옴표 사이 공백을 늘림


-- 6) LITERAL(상수) VS STRING(문자열)
/*
공통적으로 문자 표현하나, 차이가 있음
LITERAL: '상수' = 레코드에 문자상수 입력 (홑따옴표로 묶기) = 자료 직접 입력 (레코드 추가)  혹은 특정 컬럼값 연결
STRING: "문자열" = 별칭 묶기 (쌍따옴표로 묶기)
*/
-- 특정 컬럼끼리 특정 문자 상수와 함께 결합
SELECT ename || ' ' || 'is a ' || ' ' ||  job AS "employees" FROM emp;

-- 7) DISTINCT: 성별, 직책 등 범주형(category)에 자주 사용
-- DISTINCT을 쓰지 않고 직책 불러오기: 중복을 허용하여 모든 직책들이 조회
SELECT job FROM emp;
-- DISTINCT을 이용하여 각 직책을 알아보기 (중복X) = 유일한 직책
SELECT DISTINCT job FROM emp;
-- 부서번호(= 범주형)와 직책 DISTINCT
-- 1차: 부서번호, 2차: 직책 순서대로 유일한 부서번호와 직책이 나옴
SELECT DISTINCT deptno, job FROM emp;


-- 2. 조건 검색 (특정 행 검색)

-- 1) 비교 연산자
-- 숫자 비교: 동등 및 대소비교 가능
SELECT empno,ename,job,sal FROM emp WHERE sal >= 3000;
-- 문자의 경우 대소 비교는 불가능하며, 같음/다름 비교만 가능
SELECT empno,ename,job,sal,deptno FROM emp WHERE job = 'MANAGER';  -- 3명
SELECT empno,ename,job,sal,deptno FROM emp WHERE job != 'MANAGER';  -- 11명
-- 주의: 문자상수(리터럴)는 대소문자를 구분함
SELECT empno,ename,job,sal,deptno FROM emp WHERE job = 'mANAGER';  -- 0명
/*
숫자 칼럼: 동등비교, 대소비교
문자 칼럼: 동등비교
*/

-- 날짜형 조건 지정
-- 오라클에서 날짜의 경우 홑따옴표 사이에 입력되지만, 숫자로 인식
SELECT empno,ename,job,sal,hiredate,deptno FROM emp
WHERE hiredate >= to_date('1982/01/01','yyyy/mm/dd');  -- 날짜 형식의 포맷으로 바꾼 것을 1982/01/01 이후에 입사한 사람들을 추출
-- 함수 = 기능이 이미 정해진 것
-- to_date(): 문자상수(리터럴)을 날짜형식(format)으로 변환하는 함수

-- 2) SQL 연산자

-- (1) BETWEEN 연산자
-- A와 B 사이의 값을 가진 사람 추출
SELECT ename,job,sal,deptno
FROM emp
WHERE sal BETWEEN 1200 ANd 1500;
-- 비교연산 + 논리연산
-- 만일 두 조건이 충돌하면 왼쪽부터 우선이 됨
SELECT ename,job,sal,deptno
FROM emp
WHERE sal >= 1200 AND sal <= 1500;
/*
연산 우선순위
0. 괄호
1. 산술 연산자
2. 비교(관계) 연산자
3. 논리 연산자
만일 순위가 같으면 왼쪽의 우선순위가 더 높음
*/

--(2)  칼럼명 IN(목록) 연산자: 리스트(목록) 안의 값 중 하나만 일치하면 값 추출
SELECT empno,ename,job,sal,hiredate
FROM emp
WHERE empno IN (7902,7788,7566);
-- 부서 번호가 10번 혹은 30번인 사원 전부 추출
SELECT * FROM emp
WHERE deptno IN (10,30);

--(3)  LIKE 연산자: 주로 문자컬럼 대상
-- 오라클의 특수성으로 인해 날짜형도 문자로 인식되기에 날짜도 검색 가능
-- 포함문자 검색 = 와일드 카드 = % 혹은 _
-- _ 혹은 % = 어떤 문자로 시작/중간/끝임을 검색하는 경우: 만일 82%이면 82년도에 시작하는 무엇이든 추출 (월/일은 신경쓰지 X)
SELECT empno,ename,job,sal,hiredate,deptnno
FROM emp
WHERE hiredate LIKE '81%';
-- 성 검색
SELECT * FROM student WHERE name LIKE '서%';
-- 이름 검색: 처음이든 끝이든 중간에 '재' 들어간 사람 추출
SELECT * FROM student WHERE name LIKE '%재%';
SELECT * FROM student WHERE name LIKE '%수';
/* 한개 문자 대변 = '_' / 두개 이상의 문자 대변 = ' % ' */
-- 이름 중에 L_K 3개의 음절을 가진 사원 검색
SELECT * FROM emp WHERE ename LIKE '%L_K%';

-- (4)  IS NULL: 값이 없는 사람 찾기
SELECT empno,ename,job,sal,comm,deptno
FROM emp
WHERE comm IS NULL;

-- (5) IS NOT NULL: 값이 있는 사람 찾기
SELECT empno,ename,job,sal,comm,deptno
FROM emp
WHERE comm IS NOT NULL;

-- 3) 논리 연산자: AND, OR, NOT (우선순위: NOT > AND > OR)
-- 아래 SELECT문의 경우 sal >= 1100 실행, job = 'MANAGER 실행 후 마지막으로 논리연산자인 AND 실행
-- AND = 논리곱 = 그리고
SELECT empno,ename,job,sal,hitedate,deptno
FROM emp
WHERE sal >= 1100 AND job = 'MANAGER';
-- OR = 논리합 = 또는
SELECT empno,ename,job,sal,hitedate,deptno
FROM emp
WHERE sal >= 1100 OR job = 'MANAGER';
-- NOT = 부정 (참 <-> 거짓)
SELECT empno,ename,job,sal,hitedate,deptno
FROM emp
WHERE IN('MANAGER','CLERK','ANALYST');

-- 4) 우선순위: 괄호 > 비교 연산자 > NOT > AND > OR
-- 회사원 혹은 연봉이 1500 이상인 사장: 우선 AND 먼저 시작하고, OR 실행
SELECT empno,ename,job,sal
FROM emp
WHERE job = 'SALESMAN' OR JOB = 'PRESIDENT' AND sal > 1500;  -- 5개
-- 연봉이 1500 이상인 회사원 혹은 회장: 우선 OR 먼저 시작하고, AND 실행
SELECT empno,ename,job,sal
FROM emp
WHERE (job = 'SALESMAN' OR JOB = 'PRESIDENT') AND sal > 1500;  -- 2개


-- 3. 검색 레코드 정렬

-- 1) 날짜 컬럼 정렬
-- 날짜 순으로 정렬
-- ASC(오름차순) 생략: 입사 순서대로
SELECT hiredate,empno,ename,job,sal,deptno
FROM emp
ORDER BY hiredate; 
-- DESC(내림차순): 최근 입사 순서대로
SELECT hiredate,empno,ename,job,sal,deptno
FROM emp
ORDER BY hiredate DESC; 

-- 2) 숫자 칼럼 정렬
-- 급여 내림차순: 급여가 높은 순서
SELECT hiredate,empno,ename,job,sal,deptno
FROM emp
ORDER BY sal DESC;

-- 3) 수식,별칭,컬럼 순번 정렬
-- (1) 수식을 이용한 정렬
SELECT empno,ename,job,sal,sal*12 annsal FROM emp ORDER BY sal*12;
-- (2) 별칭을 이용한 정렬
SELECT empno,ename,job,sal,sal*12 annsal FROM emp ORDER BY annal;
-- (3) 순번을 이용한 정렬
SELECT empno,ename,job,sal,sal*12 annsal FROM emp ORDER BY 5;

-- 4) 두개 이상 칼럼 정렬
SELECT deptno,sal,empno,ename,job
FROM emp
ORDER BY deptno ASC, sal DESC;  -- 1차: 부서번호 오름, 2차: 급여 내림