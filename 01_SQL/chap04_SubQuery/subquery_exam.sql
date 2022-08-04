select * from STUDENT; -- profno(교수번호), deptno01(주전공)
select * from PROFESSOR; -- profno(교수번호)

-- [문1] STUDENT 테이블 검색 결과(sub query)를 이용하여 STUDENT01 테이블 생성(main query) 
-- Sub(STUDENT), Main(STUDENT01)
CREATE TABLE student01  -- 사본 만들기
AS
SELECT * FROM student;  -- 원본
SELECT * FROM student01;  --student 테이블 복제본

-- [문2] 교수번호가 2001인 지도교수를 모시는 전체 학생 명부 출력
-- Sub query(PROFESSOR), Main query(STUDENT01)
SELECT * FROM student01 WHERE profno = (SELECT profno FROM professor WHERE profno = 2001);

-- [문3] 보너스를 받는 교수들의 이름, 직위, 급여, 보너스 출력
-- 조건) IN()함수 이용 : 다중 행 처리  
SELECT name,position,pay,bonus FROM professor WHERE bonus
IN(SELECT bonus FROM professor WHERE bonus is not null);
SELECT name,position,pay,bonus FROM professor WHERE bonus is not null or bonus > 0;

-- [문4] 301 학과(DEPTNO) 교수들 보다 더 많은 급여를 받는 교수들의 이름, 직위, 급여, 학과 출력
-- 조건) ALL()함수 이용 : 다중 행 처리 
SELECT name,position,pay,deptno FROM professor
WHERE pay > ALL(SELECT pay FROM professor
                                  WHERE deptno = 301);  -- 10명(220~290)

--[문5] 장바구니에 '우유'와 '빵'를 동시에 구입한 장바구니 ID 출력(subQuery 이용) 
-- AS 사용 불가능
-- main: 우유 구매자 조회, sub: 빵 구매자 조회
-- 동일한 테이블의 동일한 칼럼을 2개 이상의 조건으로 지정
select * from CART_PRODUCTS;
SELECT DISTINCT cart_id FROM cart_products
WHERE cart_id IN (SELECT cart_id FROM cart_products WHERE name = '빵') AND name = '우유'
ORDER BY cart_id;
/*
단일쿼리문으로 조건문 작성 시: 오류는 발생하지 않으나 검색 결과 없음
SELECT DISTINCT cart_id
FROM cart_products
WHERE name = '빵' AND name = '우유';
*/
/* 
 * <장바구니 ID>
 * 1001
 * 1003
 */