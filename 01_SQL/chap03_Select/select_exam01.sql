-- <연습문제1>

-- [문1] 다음 문장에서 에러를 올바르게 수정하기(년봉은 별칭)
-- 잘못된 문장
SELECT empno,ename,sal X 12 년봉 FROM emp;
-- 수정된 문장
SELECT empno,ename,sal*12 년봉 FROM emp;

-- [문2] EMP 테이블의 구조를 확인하기(힌트 : DESC EMP -> command line에서 작업)
DESC emp;

-- [문3] EMP 테이블의 모든 내용을 조회하기
SELECT * FROM emp;

-- [문4] EMP 테이블에서 중복되지 않는 deptno 출력하기(힌트 : distinct)
SELECT DISTINCT deptno FROM emp;

-- [문5] EMP 테이블의 ename과 job를 연결하여 출력하기
SELECT ename || ' ' || job  FROM emp;

-- [문6] DEPT 테이블의 dname과 loc를 연결하여 "부서명과 위치" 별칭으로 출력하기
SELECT dname ||' -> '|| loc AS "부서명과 위치" FROM dept;

-- [문7] EMP 테이블의 job과 sal를 연결하여 "직책과 급여" 별칭으로 출력하기
SELECT job ||' '|| sal AS "직책과 급여" FROM emp;

-- [문8] gift 테이블을 대상으로 별칭을 사용하여 다음 <출력 형식>과 같이 출력하기 
SELECT gno 선물번호, gname AS 선물이름 FROM gift;
/* <출력 형식>
       선물번호      선물이름 
      1      참치세트
      2      샴푸세트   */ 




