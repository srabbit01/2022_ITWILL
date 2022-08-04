-- Sequence.sql

/*
Sequence(순서)
- 의미: 자동번호 생성기 (중복 불가, 생략 불가)
- 용도: 주로 기본키로 지정된 컬럼에 입력할 값을 생성하는 기능
- 예시: 사번, 학번, 게시글번호 등
*/

-- 1, 시퀀스 생성
CREATE SEQUENCE emp_seq
START WITH 1
INCREMENT BY 1
MAXVALUE 10000;

-- 2. 테이블 생성
DROP TABLE emp01 PURGE;
CREATE TABLE emp01(
empno number(4) PRIMARY KEY,
ename VARCHAR(20),
hiredate DATE
);

-- 3. 레코드 추가: 시퀀스 이용(객체 속성)
INSERT INTO emp01 VALUES(emp_seq.NEXTVAL,'JULA',SYSDATE);
INSERT INTO emp01 VALUES(emp_seq.NEXTVAL,'HONGKD',SYSDATE);

SELECT * FROM emp01;

-- 4. 데이터 사전 뷰: 시퀀스 정보 확인
SELECT * FROM USER_SEQUENCES;  -- 시퀀스 정보
SELECT * FROM USER_TABLES;  -- 테이블 정보

-- 5. 시퀀스 삭제
DROP SEQUENCE emp_seq;

-- <문제> DEPTNO 칼럼에 시퀀스 이용 레코드 삽입
CREATE SEQUENCE deptno_seq
START WITH 10  -- 시작값
INCREMENT BY 10  -- 증가값
MAXVALUE 60;   -- 최대값
DROP SEQUENCE deptno_seq;

DROP TABLE dept_example PURGE;
CREATE TABLE dept_example
AS
SELECT * FROM dept WHERE 1=0;

INSERT INTO  dept_example VALUES(deptno_seq.nextval,'인사과','서울');
INSERT INTO  dept_example VALUES(deptno_seq.nextval,'경리과','서울');
INSERT INTO  dept_example VALUES(deptno_seq.nextval,'총무과','대전');
INSERT INTO  dept_example VALUES(deptno_seq.nextval,'기술과','서울');
INSERT INTO  dept_example VALUES(deptno_seq.nextval,'기술과','인천');
INSERT INTO  dept_example VALUES(deptno_seq.nextval,'기술과','부산');  -- 정상

INSERT INTO  dept_example VALUES(deptno_seq.nextval,'기술과','대구');  -- 오류 발생: 60 이상의 값을 가지기 때문
SELECT * FROM dept_example;

-- 6. 시퀀스 수정: START WITH 수정 불가능
ALTER SEQUENCE deptno_seq MAXVALUE 10000;

-- 7. 문자열 + 시퀀스 숫자 결합
CREATE TABLE board(
dno CHAR(50) PRIMARY KEY,  -- 게시물 번호 (NO: 1001)
writer VARCHAR(30) NOT NULL,  -- 작성자
title VARCHAR(100) NOT NULL,  -- 제목
cont VARCHAR(1000) -- 내용(생략가능)
);
-- 시퀀스 생성
CREATE SEQUENCE bno_seq
START WITH 1001
INCREMENT BY 1;
-- 게시글 삽입: 게시물 번호 (NO: 1001)
INSERT INTO board VALUES('NO: '|| TO_CHAR(bno_seq.NEXTVAL),'홍길동','테스트1','방가방가');
INSERT INTO board VALUES('NO: '|| TO_CHAR(bno_seq.NEXTVAL),'유관순','테스트2','하이');
-- TO_CHAR(): 숫자형 -> 문자형 변환

SELECT * FROM board;