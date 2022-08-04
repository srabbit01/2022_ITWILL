-- 물리적 테이블 생성 
create table db_view_tab(
id varchar(15) primary key,
name varchar(25) not null,
email varchar(50),
regdate date not null
);

-- 레코드 추가 
insert into db_view_tab values('hong','홍길동','hong@naver.com',sysdate);
insert into db_view_tab values('lee','이순신','lee@naver.com',sysdate);
insert into db_view_tab values('admin','관리자','admin@naver.com',sysdate);
select * from db_view_tab;
commit work;

-- [문제1] 기본테이블(db_view_tab)을 이용하여 다음 조건에 맞게 일반 사용자만 조회할 수 있는 뷰를 생성하시오.
-- 조건1> 수정 가능한 읽기 전용 뷰
-- 조건2> 뷰 이름 : db_view
CREATE OR REPLACE VIEW db_view  -- 수정 가능 뷰
AS
(SELECT * FROM db_view_tab
WHERE id = 'admin')
WITH READ ONLY;  -- 읽기 전용 뷰

-- [문제2] 생성된 뷰(db_view) 내용을 확인하고, 뷰 데이터 사전으로 뷰 목록을 확인하시오.
SELECT * FROM db_view;
SELECT * FROM USER_VIEWS;

-- [문제3] 생성된 뷰(db_view)을 삭제하시오. 
DROP VIEW db_view;

-- [문제4] 다음과 같이 관리자용 view를 생성하시오.
CREATE OR REPLACE VIEW manager_view
AS
(SELECT empno 사번,ename 사원명,job 직책,deptno 부서번호
 FROM emp_copy WHERE job IN('SALESMAN','CLERK','ANALYST'))
 WITH CHECK OPTION;
SELECT * FROM manager_view;
/*
 *   조건1> 기본 테이블 : emp_copy
 *   조건2> view 이름 : manager_view
 *   조건3> 대상 칼럼 : 사번, 이름, 직책, 부서번호   
 *   조건4> 대상 레코드 : 직책(영업직, 사원, 분석자)
 *   조건5> 기본테이블 UPDATE와 INSERT 가능한 뷰 
 */
