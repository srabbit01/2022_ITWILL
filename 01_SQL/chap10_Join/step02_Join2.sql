-- step02_Join2.sql

-- 2. 논리적 조인
/*
카티션 조인(Cartesian Join)
- 공통 컬럼을 논리적(조건식)으로 테이블을 연결하는 방식
1) Cross Join: 조건 없이 테이블 연결 방식
2) Self Join: 동일 테이블 조인
3) Inner Join: 조건 있음, 조인 대상 테이블 모두 자료가 있는 경우
4) Outer Join: 조건 있음, 조인 대상 테이블 중 한쪽 테이블에 자료가 있는 경우
*/

-- 1) Cross Join: 조건 없음
SELECT * FROM emp,dept;  -- 모양(shape): 56(14X4)행 X 11(8+3)열
-- 행: 곱 / 열: 합
/*
ANSI Cross Join
SELECT * FROM 테이블1 CROSS JOIN 테이블명2;
*/

-- 2) Inner Join: 조건 있음
SELECT *
FROM emp,dept  -- 14x8, 4x4
WHERE emp.deptno = dept.deptno;  -- 조인 조건

/*
ANSI Inner Join
SELECT *
FROM table1 INNER JOIN table2
ON table1.column1 = table2.column2
*/
-- ON절 조건식 표현
SELECT ename,dname,emp.deptno
FROM emp INNER JOIN dept
ON emp.deptno=dept.deptno
WHERE ename = 'SCOTT';
-- USING 이요 표현
SELECT ename, dname, deptno  -- 공통 컬럼을 지정하기 때문에 출처를 지정하지 않음
FROM emp INNER JOIN dept
USING(deptno)
WHERE ename = 'SCOTT';

SELECT ENAME, DNAME
FROM EMP, DEPT
WHERE EMP.DEPTNO=DEPT.DEPTNO
AND ENAME='SCOTT';  -- 조인조건 AND 일반조건

-- 칼럼의 모호성 해결: 출처 명시
SELECT EMP.ENAME, DEPT.DNAME, EMP.DEPTNO
FROM EMP, DEPT
WHERE EMP.DEPTNO=DEPT.DEPTNO
AND ENAME='SCOTT';

-- 테이블 별칭 이용: 테이블의 별칭은 AS를 사용할 없음
SELECT E.ENAME, D.DNAME, E.DEPTNO, D.DEPTNO
FROM EMP E, DEPT D
WHERE E.DEPTNO = D.DEPTNO
AND E.ENAME='SCOTT';

-- 문제1) 뉴욕에서 근무하는 사원의 이름과 급여를 출력하시오.(EMP, DEPT 이용)
SELECT * FROM dept;
SELECT e.ename 사원이름,e. sal 급여
FROM emp e, dept d
WHERE e.deptno = d.deptno  -- 조인 조건
               AND loc='NEW YORK';  -- 일반 조건

-- 문제2) ACCOUNTING 부서소속 사원의 이름, 입사일, 근무지역을 출력하시오.
SELECT e.ename,e.hiredate,d.loc,d.dname  -- 출처 생략: 유일한 칼럼
FROM emp e,dept d
WHERE e.deptno=d.deptno  -- 조인 조건
              AND d.dname='ACCOUNTING';  -- 일반 조건

-- 문제3) 직급이 MANAGER인 사원의 이름, 부서명을 출력하시오.
SELECT * FROM emp;
SELECT e.ename,d.dname  -- 출처 생략; 유일한 컬럼
FROM emp e,dept d
WHERE e.deptno=d.deptno  -- 조인 조건
              AND e.job='MANAGER';  -- 일반 조건

-- 문제4) 교수번호(profno) 칼럼을 기준 조인하여 다음 그림과 같이 학생명, 학과, 교수명, 교수번호 칼럼을 조회하시오.
SELECT * FROM student;
SELECT s.name 학생명, s.deptno1 학과번호, p.name 교수명, p.profno 교수번호
FROM student s,professor p
WHERE s.profno=p.profno;  -- 조인조건

-- 문제5) <문제4>의 결과에서 101 학과만 검색되도록 하시오.
SELECT s.name 학생명, s.deptno1 학과번호, p.name 교수명, p.profno 교수번호
FROM student s,professor p
WHERE s.profno=p.profno  -- 조인 조건
               AND s.deptno1=101;  -- 일반 조건
               
-- 3) Outer Join
/*
조건이 있으며, 한쪽 테이블 자료가 있는 경우
자료 없는 테이블: (+)추가
기준 테이블: (+)없음
유형: LEFT OUTER JOIN, RIGHT OUTER JOIN
*/

-- (1) Left Outer Join: 왼쪽 테이블 기준
SELECT e1.ename 사원명, e2.ename 상사명
FROM emp e1, emp e2
WHERE e1.mgr = e2.empno(+);  -- NULL값을 가진 KING 추출됨

-- (2) Right Outer Join: 오른쪽 테이블 기준
SELECT * FROM student;  -- profno
SELECT * FROM professor;  -- profno
SELECT s.name 학생명,p.name 교수명
FROM student s, professor p
WHERE s.profno(+) = p.profno;  -- 교수 중 지도학생이 지정되지 않은 교수도 추출

-- * SELF JOIN: 동일한 테이블끼리 조인
SELECT e1.*,e2.*
FROM emp e1, emp e2;  -- 196(14*14) x 16(8+8)
-- SMITH 사원의 직속상사: 7902 = FORD
SELECT e1.ename 사원명,e2.ename 직속상사
FROM emp e1, emp e2
WHERE e1.mgr = e2.empno;  -- Inner 조인 조건

-- 문제7) EMP테이블과 DEPT테이블을 조인하여 사원이름과 부서번호와 부서명을 출력하시오.  DEPT테이블의 40번부서와 조인할 EMP테이블의 부서번호가 없지만,  아래 그림과 같이 40번부서의 이름도 출력되도록 쿼리문을 작성해보시오.
SELECT e.ename 사원명,d.deptno 부서번호,d.dname 부서명
FROM emp e, dept d
WHERE d.deptno = e.deptno(+)  -- 조인 조건  (주의: 40번 부서는 emp 테이블에 존재하지 않기 때문에 (+)를 추가)
ORDER BY d.deptno;

/*
ANSI Outer Join
SELECT *
FROM table1 [LEFT/RIGHT/FULL] OUTER  JOIN table2;
*/
-- 문제7) ANSI Left Outer Join
SELECT ename,deptno,dname
FROM emp LEFT OUTER JOIN dept
USING (deptno);  -- 조인 조건: 공통 칼럼
-- ANSI Right Outer Join: 지도학생이 없는 교수 7명 출력
SELECT student.name 학생명,profno 교수번호,professor.name 교수명
FROM student RIGHT OUTER JOIN professor
USING (profno);  -- 조인 조건: 공통 칼럼
-- ANSI Right Outer Join: 지도교수가 없는 학생 출력
SELECT student.name 학생명,profno 교수번호,professor.name 교수명
FROM professor RIGHT OUTER JOIN student
USING (profno);  -- 조인 조건: 공통 칼럼
-- ANSI Right Outer Join: 지도교수가 없는 학생과 지도학생이 없는 교수 모두 출력
SELECT student.name 학생명,profno 교수번호,professor.name 교수명
FROM professor FULL OUTER JOIN student
USING (profno);  -- 조인 조건: 공통 칼럼