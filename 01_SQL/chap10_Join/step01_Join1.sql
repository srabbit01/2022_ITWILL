-- step01_Join1.sql

-- 1. 물리적 조인
/*
물리적 조인(Join)
- 특정칼럼(외래키)을 이용하여 두개 이상의 테이블을 연결하는 DB 기법
<조인절차>
1. 기본키가 포함된 테이블(master table) 생성
2. 기본키가 포함된 테이블에 레코드 삽입
3. 외래키가 포함된 테이블(transaction table) 생성
4. 외래키가 포함된 테이블에 레코드 삽입

* 조인테이블삭제: 위 순서에 역순이다.
* 강제테이블삭제: drop table 테이블명cascade constraint;
*/

-- 1단계: 기본키가 포함된 테이블(원장 테이블) 생성
CREATE TABLE goods(  -- 상품 테이블
gcode NUMBER(2) PRIMARY KEY,
gname VARCHAR(30),
price INT
);
-- 2단계: 기본키가 포함된 테이블에 레코드 삽입
INSERT INTO goods VALUES(10,'사과',5000);
INSERT INTO goods VALUES(20,'복숭아',8000);
INSERT INTO goods VALUES(30,'포도',3000);
-- 3단계: 왜래키가 포함된 테이블(검색 테이블) 생성
-- 매일 거래가 일어나기 때문에 매일 테이블 수정 발생
CREATE TABLE sale(
gcode NUMBER(2) PRIMARY KEY,  -- 기본키인 동시에 외래키
sale_date DATE,
su NUMBER(3),
FOREIGN KEY(gcode) REFERENCES goods(gcode)  -- 외래키
);
-- 4단계: 외래키가 포함된 테이블에 레코드 삽입
INSERT INTO sale VALUES(10,sysdate,5);
INSERT INTO sale VALUES(20,sysdate,10);
INSERT INTO sale VALUES(30,sysdate,8);
INSERT INTO sale VALUES(40,sysdate,8);  -- 오류: 참조무결성 제약조건 위배
COMMIT;  -- DB 반영

-- 5단계: Join Key 이용
SELECT g.gcode,g.gname,g.price,s.sale_date,s.su
FROM goods g, sale s
WHERE g.gcode=s.gcode AND s.su>=8;  -- 조인조건 AND 일반 조건