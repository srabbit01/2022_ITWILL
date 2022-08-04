-- step02_dataType.sql 
-- Oracle 주요 자료형 (data type)

create table student(
sid int primary key,            -- 학번 (정수형은 4바이트까지 입력 가능)
name varchar(25) not null,  -- 이름 
phone varchar(30) unique,  -- 전화번호
email char(50),                  -- 이메일 
enter_date date not null     -- 입학년도 
);

/*
 * Oracle 주요 자료형 
 *  1. number(n) : n 크기 만큼 숫자(실수) 저장
 *  2. int : 4바이트 정수 저장 
 *  3. varchar2(n) : n 크기 만큼 가변길이 문자 저장
 *  4. char(n) : n 크기 만큼 고정길이 문자 저장
 *  5. date : 날짜/시간 저장 - sysdate : system의 날짜/시간 저장 
 */
 -- 가변길이: 입력되는 데이터에 따라 저장공간을 가변적으로 맞춤
 -- 고정길이: 메모리 크기를 지정된 만큼 확보한 후 저장 (입력 크기 이외는 null)
-- not null: 필수 입력 (공백X)

/*
 * 제약조건 
 *  1. primary key : 해당 칼럼을 기본키로 지정(중복불가+null불가)
 *  2. not null : null값 허용 불가 
 *  3. unique : 중복 불가(null 허용)
 */
 
 -- 학생 정보 입력
INSERT INTO student values(202201,'홍길동','010-1111-1111','hong@naver.com',sysdate);  -- sysdate: 현재 시스템의 날짜/시간 정보를 입력하는 오라클 명령어
INSERT INTO student values(202202,'이순신','010-2222-2222','lee@naver.com',sysdate);
INSERT INTO student values(202203,'유관순','010-3333-3333','yoo@naver.com',sysdate);

SELECT * FROM student;

COMMIT;