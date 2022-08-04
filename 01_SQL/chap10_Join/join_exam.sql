-- 1. 고객 테이블 
create table user_data(
user_id int primary key,  -- 기본키: 고객ID(시별자), 구분자 -> 입력 변수는 의미 없음        
gender number(1) not null,  -- 성별: 1 또는 2(범주형)    
age number(3) not null,  -- 나이: 숫자형(연속형)   
house_type number(1) not null,  -- 주택유형(1~4 범주형)
resident varchar(10) not null,  -- 거주지역: 문자형 (일정한 기준으로 묶기 어려움) -> 입력 변수로 잘 사용하지 않음
job number(1) not null  -- 직업유형: (1~6 범주형)          
);
-- 변수로 지정 가능한 것은 입력값에 대해 출력이 어떻게 되는지 상관/인과관계 분석


-- 고객 id 자동번호생성기 
create sequence id_seq increment by 1 start with 1001;

-- 레코드 삽입 
insert into user_data values(id_seq.nextval, 1, 35,	1,	'전북', 	6);
insert into user_data values(id_seq.nextval, 2, 45,	3,	'경남', 	2);
insert into user_data values(id_seq.nextval, 1, 55,	3,	'경기', 	6);
insert into user_data values(id_seq.nextval, 1, 43,	3,	'대전', 	1);
insert into user_data values(id_seq.nextval, 2, 55,	4,	'경기', 	2);
insert into user_data values(id_seq.nextval, 1, 45,	1,	'대구', 	1);
insert into user_data values(id_seq.nextval, 2, 39,	4,	'경남', 	1);
insert into user_data values(id_seq.nextval, 1, 55,	2,	'경기', 	6);
insert into user_data values(id_seq.nextval, 1, 33,	4,	'인천', 	3);
insert into user_data values(id_seq.nextval, 2, 55,	3,	'서울', 	6);
select * from user_data;


-- 2. 지불 테이블 
create table pay_data(
user_id int not null,  --외래키: 고객ID
product_type number(1) not null,  -- 상품유형 (1~5 범주형)
pay_method varchar(20) not null,  -- 지불유형(1~4 범주형)
price int not null,  -- 구매비용: 숫자형(연속형)
foreign key(user_id)             
references User_data(user_id)
);

-- 레코드 삽입 
insert into pay_data values(1001, 1, '1.현금', 153000);
insert into pay_data values(1002, 2, '2.직불카드', 120000);
insert into pay_data values(1003, 3, '3.신용카드', 780000);
insert into pay_data values(1003, 4, '3.신용카드', 123000);
insert into pay_data values(1003, 5, '1.현금', 79000);
insert into pay_data values(1003, 1, '3.신용카드', 125000);
insert into pay_data values(1007, 2, '2.직불카드', 150000);
insert into pay_data values(1007, 3, '4.상품권', 78879);
select * from pay_data;


-- 3. 반품 테이블  
create table return_data(
user_id int not null,  -- 외래키: 고객ID
return_code number(1) not null,  -- 반품사유코드 (1~4 범주형)
foreign key(user_id) 
references User_data(user_id)    
);

-- 레코드 삽입 
insert into return_data values(1003, 1);
insert into return_data values(1003, 4);
insert into return_data values(1007, 1);
insert into return_data values(1009, 2);

select * from return_data;

commit work;


-- 지불 테이블과 반품 테이블이 고객 테이블을 탐조
-- 문1) 고객(user_data)테이블과 지불(pay_data)테이블을 inner join하여 다음과 같이 출력하시오.
-- 조건1) 고객ID(user_id), 성별(gender), 연령(age), 직업유형(job), 
--          상품유형(product_type), 지불방법(pay_method), 구매금액(price) 칼럼 출력  
-- 조건2) 고객ID 오름차순 정렬
SELECT u.user_id,gender,age,job,product_type,pay_method,price
FROM user_data u, pay_data p
WHERE u.user_id=p.user_id
ORDER BY u.user_id;

-- 문2) 문1)의 결과에서 성별이 '여자'이거나 지불방법이 '1.현금'인 경우만 출력하시오.
-- 남 : gender=1, 여 : gender=2
SELECT u.user_id,gender,age,job,product_type,pay_method,price
FROM user_data u, pay_data p
WHERE u.user_id=p.user_id
AND gender = 2 OR pay_method = '1.현금'
ORDER BY u.user_id;

-- 문3) 고객(user_data)테이블과 지불(pay_data)테이블을 left outer join하여 다음과 같이 출력하시오.
-- 조건) 고객ID, 성별, 나이, 상품유형, 지불방법 칼럼 출력   
SELECT user_id,gender,age,product_type,pay_method
FROM user_data LEFT OUTER JOIN pay_data
USING(user_id);

-- 문4) 고객(user_data)테이블과 반품(return_data)테이블을 이용하여 left outer join하여 다음과 같이 출력하시오.
-- 조건1) 고객ID, 성별, 나이, 거주지역, 반품코드 칼럼 출력   
-- 조건2) 반품한 고객만 출력
SELECT user_id,gender,age,resident,return_code
FROM user_data LEFT OUTER JOIN return_data
USING(user_id)
WHERE return_code IS NOT NULL;
