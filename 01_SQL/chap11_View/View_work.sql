-- View_work.sql

/*
뷰(View): 실제 물리적인 테이블을 보여주는 기능
용도: 물리적인 테이블의 서로 접근 권한 설정
*/
-- 1, 뷰의 기본 테이블(물리적 테이블) 생성
CREATE TABLE DEPT_COPY
AS
SELECT * FROM DEPT;

DROP TABLE emp_copy PURGE;  -- 만일 emp_copy가 존재하면 삭제하는 쿼리문

CREATE TABLE EMP_COPY
AS
SELECT * FROM EMP;

-- 2. 뷰(VIEW) 생성: 서브쿼리 이용
CREATE VIEW emp_view30  -- 30번 부서 이용
AS
SELECT empno,ename,deptno
FROM emp
WHERE deptno=30;  -- WITH READ ONLY: 읽기 전용 뷰
-- 권한이 없으면 오류 발생
/*
물리적 테이블: EMP
가상의 테이블: EMP_VIEW30
현재, SCOTT이라는 일반 사용자로 사용중인데, view 생성 권한이 있어야 하기 때문에 관리자 모드에서 권한을 부여해 주어야 함
- scott 사용자 VIEW 생성 권한 부여
SQL> conn system/1234  -- 관리자 모드 로그인
SQL> grant create view to scott;
*/
-- 뷰 확인: SELECT절 이용
SELECT * FROM emp_view30;  -- 내용 확인: 30번 사원 정보 알 수 없음
DESC emp_view30;  -- 구조 확인

-- 3. 뷰의 데이터 사전 뷰: USER_XXXX
-- 지금까지 사용자가 만든 뷰 목록 확인
SELECT * FROM user_views;

-- 4. 뷰 삭제
DROP VIEW emp_view30;

-- 5. 뷰의 사용 목적
/*
1) 복잡한 SQL문 사용시
2) 보안 목적: 접근 권한에 따른 정보 제공
*/
-- 1) 복잡한 SQL문 사용시
CREATE OR REPLACE VIEW join_view  -- 수정 가능한 뷰 생성 = 즉, 삭제하지 않고도 재생성 가능
AS
(SELECT s.name 학생명,s.deptno1 학과번호,p.name 교수명,p.profno 교수번호  -- 칼럼의 이름이 중복되면 오류 발생
FROM student s, professor p
WHERE s.profno = p.profno
              AND s.deptno1 = 101)
WITH READ ONLY;  -- 읽기 전용 뷰

SELECT * FROM join_view;  -- 간단한 문장으로 출력 가능

-- 2) 보안 목적: 접근 권한에 따른 정보 제공

-- (1) 영업사원 제공 뷰
CREATE OR REPLACE VIEW sales_view(사원번호,사원이름,성과급)
AS
(SELECT empno,ename,comm FROM emp
WHERE job = 'SALESMAN')
WITH READ ONLY;  -- 읽기 전용 뷰 추가 (자료 INSERT/UPDATE/DELETE 차단)
SELECT * FROM sales_view;  -- 뷰 내용 확인
SELECT * FROM sales_view WHERE comm>0;  -- WHERE절
DELETE FROM sales_view WHERE empno=7499;  -- 오류: 삭제는 불가능


-- (2) 일반 사원 제공 뷰
CREATE OR REPLACE VIEW clerk_view
AS
(SELECT empno,ename,hiredate,deptno FROM emp
WHERE job = 'CLERK')
WITH READ ONLY;
SELECT * FROM clerk_view;

SELECT * FROM USER_views;

-- 6. 뷰 생성이에 사용되는 다양한 옵션
CREATE OR REPLACE VIEW view_chk30
AS
SELECT empno, ename, sal, comm, deptno
FROM emp_copy
WHERE deptno=30 WITH CHECK OPTION;  -- 조건에 사용되는 칼럼값(deptno) 수정 방지
SELECT * FROM view_chk30;

-- 뷰 -> 물리적 테이블 수정
UPDATE view_chk30 SET deptno=20 WHERE sal>=1500;  -- 오류: WITH CHECK OPTION에 의해 수정 불가능
DELETE FROM view_chk30 WHERE deptno=30;

-- 7. 뷰에서 의사컬럼(ROWNUM) 이용: 급여수령자 TOP3
-- (1) 가장 많은 급여 수령자 순으로 뷰
CREATE OR REPLACE VIEW desc_sal_view
AS
SELECT empno,ename,sal,hiredate  -- 뷰를 만들때 의사컬럼(rownum)을 사용할 수 없음
FROM emp
ORDER BY sal DESC  -- 급여가 높은 순서대로 입력
WITH READ ONLY;
-- (2) 이미 만들어진 뷰를 토대로 상위 TOP3 급여수령자 추출
-- 왜 한번에 만들 수 없음?
SELECT * FROM desc_sal_view
WHERE rownum<=3;  -- 급여가 높은 순으로 입력된 것이기 때문에 rownum을 이용하여 추출 가능