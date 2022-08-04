-- 1. 보호동물 테이블 
create table ANIMAL_INS(
AID int primary key, -- 동물 ID
ATYPE varchar(20) not null, -- 동물 유형 
DATETIME date not null, -- 보호 시작일 
CONDITON varchar(30), -- 상태
NAME varchar(20) -- 동물 이름 
);

/*
테이블 삭제 및 재생성: 자동번호 생성기가 다시 원점부터 시작하게하기 위해 삭제했다가 생성해야 함
1. 테이블 삭제
DROP TABLE animal_ins PURGE;
2. 자동번소 생성기 삭제
DROP SEQUENCE ani_id;
3. 자동 번호 생성기 생성
CREATE SEQUENCE ani_id INCREMENT BY 1 START WITH 10001;
4. 테이블 생성
CREATE TABLE animal_ins;
5. 레코드 추가
*/


-- 입력 순서 지정 = 자동번호 생성기: 시작번호부터 1씩 증가
-- 구분자
create sequence ani_id increment by 1 start with 1001;  -- 1001~N (중복되지 않는 유일한 번호 생성)

-- nextval = 다음 값을 꺼내옴을 의미
insert into ANIMAL_INS values(ani_id.nextval, '강아지', sysdate,	'양호','푸들');
insert into ANIMAL_INS values(ani_id.nextval, '강아지', sysdate,	'부상','진도');
insert into ANIMAL_INS values(ani_id.nextval, '고양이', sysdate,'양호',	'러시안블루');
insert into ANIMAL_INS values(ani_id.nextval, '강아지', sysdate,	'부상', 	'달마티안');
insert into ANIMAL_INS values(ani_id.nextval, '고양이', sysdate,'양호', '봄베이');
insert into ANIMAL_INS values(ani_id.nextval, '고양이', sysdate,'부상', '메이쿤');
insert into ANIMAL_INS values(ani_id.nextval, '강아지', sysdate,	'양호', 	'차우차우');
insert into ANIMAL_INS values(ani_id.nextval, '고양이', sysdate,'부상', '버만');
insert into ANIMAL_INS values(ani_id.nextval, '강아지', sysdate,	'부상', 	'블록');
-- sysdate: 현재 시스템의 날짜 입력

select * from ANIMAL_INS;


-- [문1] 다음 조건으로 입양동물 테이블 작성하기
/*
 * 테이블명 : ANIMAL_OUTS
 * 칼럼명 : AID -> 자료형 : int, 제약조건 : 생략불가, 중복 불가
 * 칼럼명 : ATYPE -> 자료형 : 고정길이 문자(10자리), 제약조건 : 생략 불가
 * 칼럼명 : DATETIME -> 자료형 : 날짜형, 제약조건 : 생략 불가
 * 칼럼명 : NAME -> 자료형 : 가변길이 문자(최대 20자리), 제약조건 : 생략 가능  
 * 외래키 : AID 칼럼 -> ANIMAL_INS의 기본키 적용  
 */
 CREATE TABLE animal_outs(
 aid INT NOT NULL UNIQUE,  -- 외래키
 atype CHAR(10) NOT NULL,
 datetime DATE NOT NULL,
 name VARCHAR(20),
 FOREIGN KEY(aid) REFERENCES animal_ins(aid)  --외래키 지정
 );
 
-- ANIMAL_OUTS 테이블 레코드 추가 
insert into ANIMAL_OUTS values(1001, '강아지', '2020-10-03', '푸들');
insert into ANIMAL_OUTS values(1003, '고양이', '2020-12-10','러시안블루');
insert into ANIMAL_OUTS values(1004, '강아지', '2020-03-12', '달마티안');
insert into ANIMAL_OUTS values(1005, '고양이', '2020-12-25', '봄베이');
insert into ANIMAL_OUTS values(1006, '고양이', '2020-06-10', '메이쿤');

-- 9마리 중 5마리 입양됨
select * from ANIMAL_OUTS;


/*
 * [문2] TABLE 별칭 이용 
 * 관리자의 실수로 일부 동물의 입양일이 잘못 입력되었다. 보호 시작일 보다 
 * 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 다음 SQL문을 완성하시오.
 * (단, 보호 시작일이 빠른 순서로 정렬)
 */ 
SELECT  i.datetime indate,o.datetime outdate,i.aid,i.name
FROM animal_ins i, animal_outs o
WHERE i.aid = o.aid AND i.datetime > o.datetime;  -- 우선 입양된 동물 추출 후, 오입력한 내용 추출

/*
 * <조회 결과> 
 * 1001
 * 1003
 * 1004
 * 1005
 * 1006
 */

-- SQL문
SELECT I.AID, I.DATETIME   -- 별칭.칼럼명
FROM ANIMAL_INS I, ANIMAL_OUTS O  -- 테이블 별칭
WHERE I.aid = O.aid AND I.datetime > O.datetime;

/*
 * [문3] SUBQUERY 이용
 * 천재지변으로 인해 일부 데이터가 유실되었다. 입양을 간 기록은 있는데,
 * 보호소에 들어온 기록이 없는 동물의 ID와 이름을 ID순으로 조회하시오.  (서브쿼리 사용)
 *    - 유실된 테이블 : ANIMAL_INS2
 *    - 입양된 테이블 : ANIMAL_OUTS
 *    - 서브쿼리 이용: 순서 존재
 */
 -- 서브쿼리: 유실된 보호소 동물에서 ID 선택
 -- 메인쿼리: 입양 동물 테이블에서 유실된 보호소 동물에 포함 안된 ID 선택
 SELECT DISTINCT o.AID, o.NAME
 FROM ANIMAL_INS2 i, ANIMAL_OUTS o
 WHERE o.name NOT IN (SELECT name FROM animal_INS2)  -- 서브쿼리: 실행순서 O
 ORDER BY AID;

-- 테이블 별칭 이용 예: 동시에 실행
-- 8마리 동물 5번 출력
SELECT O.id
FROM ANIMAL_INS2 I, ANIMAL_OUTS O
WHERE O.aid NOT IN I.aid;
/*
 O        VS       I
 1001          1001  --> 1003,1004,1005,1006,...
 1003
 1004
 1005
 1006
*/
 
/*
 * <조회결과>
 * 1003
 * 1005
 * 1006
 */

-- 유실된 테이블 Table 생성 
CREATE TABLE ANIMAL_INS2 
AS 
SELECT * FROM ANIMAL_OUTS 
WHERE ATYPE = '강아지';

/*
 * [문4] SUBQUERY & ROWNUM 이용 
 * 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과
 * 보호 시작일을 조회하는 SQL문을 작성하시오.(단 결과는 보호 시작일 순으로 조회)
 * 힌트 : ROWNUM 사용
 * 사용 테이블 : ANIMAL_INS, ANIMAL_OUTS
 */
 -- id 기준
 --서브쿼리: 입양 간 동물 ID 조회
 -- 메인쿼리: 입양간 동물 ID를 제외한 가장 오래 보호소에 남겨진 동물 ID
SELECT rownum, aid, name, datetime
FROM animal_ins
WHERE aid NOT  IN (SELECT aid FROM animal_outs)
              AND ROWNUM < 4;
              
-- name 기준
-- 이름 기준이기에 IN의 리스트 안은 가나다 순으로 재정렬
SELECT rownum, aid, name, datetime
FROM animal_ins
WHERE name NOT  IN (SELECT name FROM animal_outs)  -- NAME으로 설정하면 이름수능로 재정렬되어 입력
              AND ROWNUM < 4;

/*
 * <조회결과>
 * 1002 
 * 1007 
 * 1008 
 */
