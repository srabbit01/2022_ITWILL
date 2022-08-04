-- chap02_SQL_basic.
-- step01_sql_basic.sql
-- id: scott, pw: tiger

-- 'scott'의 권한으로 만든 현재 테이블의 목록 조회
SELECT * FROM tab; -- 'tab' = 오라클의 의사 테이블 (= 실제 존재하지 않는 데이블) : 전체 레코드 조회
-- SQL의 대개 명령어는 대문자, 입력어는 소문자로 표기 (권고)
-- 대소문자에 영향을 받지 않으나 구분하는 것이 용이

/*
  SQL(Structured Query Language) : 구조화된 질의 언어 
  - DDL, DML, DCL
  1. DDL : 데이터 정의어 -> DBA, USER(TABLE 생성, 구조변경, 삭제)
  2. DML : 데이터 조작어 -> USER(SELECT, INSERT, DELETE, UPDATE)
  3. DCL : 데이터 제어어 -> DBA(권한설정, 사용자 등록 등) 
*/

-- 1. DDL : 데이터 정의어

-- 1) Table 생성: CREATE TABLE
/*
 * create table 테이블명(
 *   칼럼명 데이터형 [제약조건],
 *   칼럼명 데이터형
 *   );
 */
 -- 테이블이 생성되지 전까지 수정이 가능함
 CREATE TABLE test2(  -- 이름의 경우 소문자로 할 것을 권고
 id VARCHAR(20) primary key,  -- VAR = Variable = 가변형 / CHAR = Character = 문자
passwd VARCHAR(50) not null,  -- VARCHAR(최대글자수) = 영어 기준
 name VARCHAR(25) not null  -- not null = 공백 허용 X = 반드시 입력해야 함
 );  -- = 스키마 = 테이블의 구조 = 외부에서 데이터가 들어왔을 때, 테이블 구조와 다른 데이터 제거 = 데이터의 '신뢰성' 증가
-- 데이터를 적재(저장)하는 것만이 목적인 일반적인 big data와 달리, 관계형 데이터 관리 시스템(= DBMS = 오라클 등)의 목적은 데이터의 신뢰성
 -- 테이블 전체 목록 조회
 SELECT * FROM tab;
 -- 특정 테이블 내용 조회
 SELECT *  FROM test2;
 
-- 2) Table 구조 변경: ALTER TABLE
-- (1) 테이블 이름 변경 
-- 형식) alter table 구테이블명 rename to 새테이블명;
ALTER TABLE test2 RENAME TO member;
-- (2) 테이블 칼럼 추가 
-- 형식) alter table 테이블명 add (칼럼명 자료형(n));
-- 가입일 컬럼 추가
ALTER TABLE member ADD(reg_date date); -- date: 년,월,일 (모두 넣을시 제약조건X)
--(3) 테이블 칼럼 수정 : 이름변경, type, 제약조건 수정 
-- 형식) alter table 테이블명 modify (칼럼명 자료형(n) 제약조건); 
-- Password 데이터형의 크기 조절
ALTER TABLE member MODIFY(passwd VARCHAR(25));
-- 기존 컬럼의 이름은 수정할 수 없기에, 반드시 테이블 삭제 후 추가를 통해 수정
-- (4) 테이블 칼럼 삭제 
-- 형식) alter table 테이블명 drop column  칼럼명;
ALTER TABLE member DROP COLUMN passwd;
SELECT * FROM member;

-- 3) Table 제거 
-- 형식) drop table 테이블명 purge;
-- 일반적으로 drop시, 기존 파일은 제거되나 임시파일이 남아 복원 가능
-- purge 속성 : 임시파일 제거 (purge 사용시, 임시파일도 제거되기에 복원 불가능)
DROP TABLE member PURGE;

-- 개인이 생성한 TABLE의 삭제가 가능하나, 타사용자가 생성한 TABLE의 삭제 권한은 없음

-- 2. DML : 데이터 조작어
create table depart(  -- 부서 테이블
dno number(4),  -- 부서 번호(10진수 4자리)
dname varchar(50),  -- 부서명 (영어 한글자 = 1바이트 / 한글 한글자 = 2~3바이트)
daddress varchar(100)  -- 부서 주소(위치)
);
SELECT * FROM depart;

-- 1) insert : 레코드 삽입
-- 형식) insert into 테이블명(칼럼명1, .. 칼럼명n) values(값1, ... 값n);  -- 컬럼명 수와 값 수가 같아야 함
INSERT INTO depart(dno,dname,daddress) values(1001,'기획실','서울시');  -- 주의: 문자는 반드시 홑따옴표(' ') 사이에 입력
-- 전체 컬럼 입력: 컬럼명 생략
INSERT INTO depart values(1002,'영업부','부산시');
-- 부분 칼럼 입력: 컬럼명 필수 입력
INSERT INTO depart(dno,dname) values(1003,'총무부');  -- 만일 값을 입력하지 않으면 NULL값이 들어감

-- 2) select : 레코드 검색
-- 형식) select 칼럼명 from 테이블명 [where 조건식];
-- 일반 사용자가 가장 많이 사용
-- 전체 컬럼 조회: 컬럼명 = *
SELECT * FROM depart;
-- 특정 컬럼 조회
SELECT dno,dname FROM depart;
-- 조건식을 이용한 특정 특징을 가진 값 추출 ( 관계 연산자 등)
SELECT * FROM depart WHERE dno >= 1002;  -- 숫자는 대소관계를 비교하여 특정 값 추출
SELECT * FROM depart WHERE daddress is null;  -- 해당 컬럼에 값이 주어지지 않은 값 추출 (주소가 없는 레코드 조회) 
SELECT * FROM depart WHERE daddress is not null;  -- 해당 컬럼에 값이 있는 값만 추출 (주소가 있는 레코드 조회)


SELECT * FROM depart;
SELECT dno,dname FROM depart;
SELECT * FROM depart WHERE dno >= 1002;  

-- 3) update : 레코드 수정
-- 형식) update 테이블명 set 칼럼명 = 값 where 조건식;
-- DB은 최신의 정보를 업로드해야 하기에 수정 기능은 매우 중요
UPDATE depart SET daddress = '대전시' WHERE dno = 1003;
-- WHERE 절 넣지 않으면 모든 컬럼값 변경

-- 4) delete : 레코드 삭제 
-- 형식) delete from 테이블명 where 조건식;
DELETE FROM depart WHERE dno = 1003;

-- 3. DCL : 데이터 제어어
-- 관리자만 제어할 수 있으며, 관리자 모드로만 사용 가능
-- SQL> conn system/1234;  -- 관리자 권한으로 로그인 예

-- 1) 권한 설정 : grant 권한, ... to user;
-- SQL> grant connect to scott;  -- 권한 설정 예

-- 2) 권한 해제 : revoke 권한, ... to user;
-- SQL> grant revoke to scott;  -- 권한 해제 예

-- 3) 일반 사용자 추가 : create user 계정 identified by 비밀번호;
-- SQL> create user scott identified by tiger;  -- 일반 사용자 추가 예

-- ** 작업 내용 DB 반영
COMMIT;