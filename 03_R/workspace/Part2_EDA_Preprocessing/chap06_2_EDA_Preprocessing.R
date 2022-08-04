# chap06_2_EDA_Preprocessing

## 탐색적데이터분석과 전처리 


# 1. 탐색적 데이터 조회 

# 실습 데이터 읽어오기
getewd()
setwd("E:/03. R/data")
dataset <- read.csv("dataset.csv", header=TRUE) # 헤더가 있는 경우
# dataset.csv - 칼럼과 척도 관계 

# 1) 데이터 조회
# - 탐색적 데이터 분석을 위한 데이터 조회 

# (1) 데이터 셋 구조
names(dataset) # 변수명(컬럼)
attributes(dataset) # names(), class, row.names
str(dataset) # 데이터 구조보기
dim(dataset) # 차원보기 : 300 7
nrow(dataset) # 관측치 수 : 300
ncol(dataset)
length(dataset) # 칼럼수 : 7 

# (2) 데이터 셋 조회
# 전체 데이터 보기
dataset # print(dataset) 
View(dataset) # 뷰어창 출력
# 엑셀 시트와 같은 역할

# 칼럼명 포함 간단 보기 
head(dataset) 
tail(dataset) 

# (3) 칼럼 조회 
# 형식) dataframe$칼럼명   
age = dataset$age # 벡터형 반환
dataset$resident
length(dataset$age) # data 수-300개 
age[100]

# 형식) dataframe["칼럼명"] - $기호 대신 [""]기호 사용
dataset["gender"] # 데이터프레임 반환
dataset["price"]
age2 = dataset["age"]
dim(age2) # [1] 300   1 -> 행렬 형태
age2[100,1] # 43

# 형식) dataframe[색인] : 색인(index)으로 원소 위치 지정 
dataset[2] # 두번째 컬럼
dataset[6] # 여섯번째 컬럼
dataset[3,] # 3번째 관찰치(행) 전체
dataset[3]
dataset[,3] # 3번째 변수(열) 전체

# dataset에서 2개 이상 칼럼 조회
dataset[c("job","price")] # 문자형, 콜론(:)으로 연속형 범위 지정 불가능
dataset[c(2,6)] 

dataset[c(1,2,3)] 
dataset[c(1:3)] # 숫자형, 콜론(:)으로 연속형 범위 지정 가능
dataset[c(2,4:6,3,1)] 


# 2. 결측치(NA) 처리

# 1) 결측치 확인 
summary(dataset) # 7개 변수 전체
table(is.na(dataset)) 
# FALSE  TRUE 
# 1982   118 


# 2) 결측데이터 제거  
price2 <- na.omit(dataset$price)# 특정 칼럼 대상 제거
sum(price2) # 2362.9
length(dataset$price) # 300
length(price2) # 270 -> 30개 제거

dataset2=na.omit(dataset)
dim(dataset) # [1] 300   7
dim(dataset2) # [1] 209   7 -> 91개의 행 제거

# 3) 결측데이터 처리(0 or 상수 대체)
x <- dataset$price # price vector 생성 
x[1:30] # 5.1 4.2 4.7 3.5 5.0
dataset$price2 = ifelse( !is.na(x), x, 0) # 0으로 대체
dataset$price2[1:30]
dim(dataset) # [1] 300   8 # price2 변수 추가

# 4) 결측데이터 처리(평균 or 중위수 대체)
x <- dataset$price # price vector 생성 
x[1:30] # 5.1 4.2 4.7 3.5 5.0
dataset$price3 = ifelse(!is.na(x), x, round(mean(x, na.rm=TRUE), 2) ) # 평균으로 대체
dataset$price3[1:30]


# 3. 이상치 발견과 정제
# - 정상 범주에서 크게 벗어난 값 
# - 분석 결과에 왜곡

# 1) 범주형 변수 이상치 처리
# 범주의 개수가 많지 않아 이상치 감지가 쉬움
gender <- dataset$gender
gender

# outlier 확인
table(gender) # 빈도수
pie(table(gender)) # 파이 차트

# gender 변수 정제(1,2)
dataset <- subset(dataset, gender==1 | gender==2) # subset(df,조건식)
dataset # gender변수 데이터 정제
length(dataset$gender) # 297개 - 3개 정제됨
pie(table(dataset$gender))


# 2) 연속형 변수 이상치 처리
dataset$price # 세부데이터 보기
# 정상 범주 파악이 어려움

# (1) 정상범주(2~8) 이용 이상치 처리 
length(dataset$price) #300개(NA포함)
plot(dataset$price) # 산점도 # 음수는 확실히 이상치(나올 수 없음)나 양수는 정상 범주 확인하기 어려움
summary(dataset$price) # 범위확인

# price변수 정제(2~8): 정상범주 -> subset 생성
dataset2 <- subset(dataset, price >= 2 & price <= 8)
length(dataset2$price) 
boxplot(dataset2$age) # 요약 통계 시각화

# (2) 상자그래프와 통계량 이용 이상치 처리
# 함수를 이용한 이상치 처리
boxplot(dataset$price)
# 일반적으로 정상범위에서 상하위 0.3% 이상치로 본다.
dim(dataset2)

# 상자그래프와 통계량 
boxplot(dataset$price)$stats # 정상범주 확인
# $stats: 박스 플롯이 가진 칼럼 호출
names(boxplot(dataset$price))

# 이상치 대체 : 하한값/상한값으로 대체 
dataset3 <- na.omit(dataset) # 결측치 제거 
#       [,1]
# [1,]  2.1 -> 하한값
# [2,]  4.4
# [3,]  5.4
# [4,]  6.3
# [5,]  7.9 -> 상한값

# 이상치 대체: 하한값/상한값으로 대체 (2.1~7.9를 정상 범주로 여김)
dataset3$price <- ifelse(dataset3$price < 2.1, 2.1, dataset3$price) # 하한값 대체 
dataset3$price <- ifelse(dataset3$price > 7.9, 7.9, dataset3$price) # 상한값 대체 
# 이상치 제거 가능하나, 상한값 이상은 상한값, 하한값 이하는 하한값으로 대체
dim(dataset3) # [1] 209   8
boxplot(dataset3$price) # 자료 손실 없이 이상치 처리

# (3) IQR(Inter Quartile Range)방식 이용 이상치 처리
# IQR = Q3 - Q1 
# 정상범위 : Q1 - 1.5 * IQR ~ Q3 + 1.5 * IQR = 하한값 ~ 상한값
# 사용자가 직접 통계적인 방법을 이용하여 처리
dataset4 <- na.omit(dataset) 
dim(dataset4) # [1] 209   9
names(dataset4)

# 4분위수 출력 함수: quantile(변수,%/100)
q1 = quantile(dataset4$price,1/4) # 제1사분위수: 25% -> 4.6
q3 = quantile(dataset4$price,3/4) # 제3사분위수: 75% -> 6.3

# 제1사분위수와 제3사분위수 사이의 범위
IQR = q3-q1 # 1,7
outlier_step = 1.5*IQR
# outlier step: 

minVal = q1 - 1.5 * IQR # 2.05
maxVal = q3 + 1.5 * IQR # 8.85
# 정상범위: 2.05 ~ 8.85

# 이상치 대체: minVal/maxVal으로 대체
dataset4$price <- ifelse(dataset4$price < minVal, minVal, dataset4$price) # 하한값 대체 
dataset4$price <- ifelse(dataset4$price > maxVal, maxVal, dataset4$price) # 상한값 대체 
boxplot(dataset4$price)

# subset vs ifelse
# subset: 이상치 제거 (입출력 결과 dataframe: 2차원)
# ifelse: 이상치 대체 (입출력 결과 vector: 1차원)

# 4. 코딩변경 
# - 데이터의 가독성, 척도 변경, 최초 코딩 내용 변경을 목적으로 수행

# 1) 가독성을 위한 코딩변경 
# 형식) dataframe$새칼럼명[부울린언식] <- 변경값   
dataset2$resident2[dataset2$resident == 1] <-'1.서울특별시'
dataset2$resident2[dataset2$resident == 2] <-'2.인천광역시'
dataset2$resident2[dataset2$resident == 3] <-'3.대전광역시'
dataset2$resident2[dataset2$resident == 4] <-'4.대구광역시'
dataset2$resident2[dataset2$resident == 5] <-'5.시구군'
dataset2[c("resident","resident2")] # 2개만 지정

# 직책의 유형별 변수 추가
dataset2$job2[dataset2$job == 1] <- '공무원'
dataset2$job2[dataset2$job == 2] <- '회사원'
dataset2$job2[dataset2$job == 3] <- '개인사업'
dim(dataset2) # [1] 209   11
dataset2[c('job','job2')]

# 2) 연속형 -> 범주형
# 형식) dataframe$새칼럼명[부울린언식] <- 변경값
dataset2$age2[dataset2$age <= 30] <-"청년층" # 1~30
dataset2$age2[dataset2$age > 30 & dataset2$age <=55] <-"중년층" # 31~55
dataset2$age2[dataset2$age > 55] <-"장년층" # 56~
dim(dataset2) # [1] 209  12
dataset2[c('age','age2')] # 생성된 두 변수만 비교
head(dataset2)

# 3) 역코딩 : 긍정순서(5~1)
# 5점 척도 
# 1.매우만족,  ...  5. 매우불만족 -> 6-1, 6-5 -> 5, 1

dataset2$survey
range(dataset2$survey) # 1~5

survey <- dataset2$survey
csurvey <- 6-survey # 역코딩: 상수 - 벡터 자료 (벡터의 수만큼 상수와 벡터 연산)
csurvey
survey  # 역코딩 결과와 비교
dataset2$survey <- csurvey # survery 수정
head(dataset2) # survey 결과 확인


# 5. 정제된 데이터 저장
getwd()
setwd("E:/03. R/data/data")

# (1) 정제된 데이터 저장
write.csv(dataset2,"cleanData.csv", quote=F, row.names=F) 

# (2) 정제된 데이터 불러오기 
new_data <- read.csv("cleanData.csv")
head(new_data)


# 6. 탐색적 분석을 위한 시각화 

# 데이터셋 불러오기
new_data <- read.csv("new_data.csv", header=TRUE)
new_data 
dim(new_data) #  231  15
str(new_data)

# 1) 명목척도(범주/서열) vs 명목척도(범주/서열) 
# - 거주지역과 성별 칼럼 시각화 
resident_gender <- table(new_data$resident2, new_data$gender2)
resident_gender # 교차분할표: 범주형 변수 분석
gender_resident <- table(new_data$gender2, new_data$resident2) # 행렬 위치가 바뀜
gender_resident

# - 성별에 따른 거주지역 분포 현황 
barplot(resident_gender, beside=T, horiz=T,
        col = rainbow(5),
        legend = row.names(resident_gender),
        main = '성별에 따른 거주지역 분포 현황') 
# row.names(resident_gender) # 행 이름 

# - 거주지역에 따른 성별 분포 현황 
# 행렬이 다르면 y축의 분포 다름(축과 범례의 위치 바뀜)
barplot(gender_resident,horiz=F)
barplot(gender_resident, beside=T, 
        col=rep(c(2, 4),5), horiz=T,
        legend=c("남자","여자"),
        main = '거주지역별 성별 분포 현황')  

# 2) x = 비율척도(연속) vs y = 명목척도(범주/서열)
# - 나이와 직업유형에 따른 시각화 
# install.packages("lattice")  # chap08
# 격자 단위 고급 시각화 패키지
library(lattice) # 격자 단위로 결과를 보고자 할 때, 사용
# 각 범주 별로 그래프 여러개 생성 (격자형으로 제시)

# 직업유형에 따른 나이 분포 현황   
# 밀도분포곡선(고급 시각화)
# densityplot(y~x,data=데이터셋)
# 대부분 밀도 분포곡선을 제공하기 때문에 y변수는 없고, x만 입력
densityplot( ~ age, data=new_data, groups = job2,
             plot.points=T, auto.key = T)
# plot.points=T : 밀도, auto.key = T : 범례 

# 3) 비율(연속) vs 명목(범주/서열) vs 명목(범주/서열)
# - 구매비용(연속):x칼럼 , 성별(명목):조건, 직급(서열):그룹   

# densityplot(~x|격자생성변수(조건),data=데이터셋,groups=그룹)

# (1) 성별에 따른 직급별 구매비용 분석  
densityplot(~ price | factor(gender2), data=new_data, 
            groups = position2, plot.points=T, auto.key = T) 
# 조건(격자) : 성별, 그룹 : 직급 

# (2) 직급에 따른 성별 구매비용 분석  
densityplot(~ price | factor(position2), data=new_data, 
            groups = gender2, plot.points=T, auto.key = T) 
# 조건 : 직급(격자), 그룹 : 성별 


# 7.파생변수 생성 
# - 기존 변수로 새로운 변수 생성
# 1) 사칙연산
# 2) 1:1 -> 기존변수(1) -> 새로운 변수(1)
# 3) 1:n -> 기존변수(1) -> 새로운 변수(n)

setwd('E:/03. R/data')
user_data <- read.csv('user_data.csv', header = T)
# 고객 정보 기록 자료
head(user_data) # user_id age house_type resident job 

# 1) 1:1 파생변수 생성 : 기존 칼럼 1개 -> 새로운 칼럼 1개
# - 주택 유형 :  0, 아파트 유형 : 1(더미변수 생성) : 주택 유형 파악 가능
summary(user_data$house_type) # NA확인 - 없음 
table(user_data$house_type)

# dummy 생성 
# 1과 2는 0, 3과 4는 1로 지정
house_type2 <- ifelse(user_data$house_type == 1 | user_data$house_type == 2, 0, 1)
# 결과 확인
house_type2[1:10] 
# 파생변수 추가 
user_data$주거환경 <- house_type2
head(user_data)


# 2) 1:N 파생변수 생성 : 각 id(고객)에 대한 구매상품, 지불방법 나열 
# 변수 1개를 n개의 변수로 확장
pay_data <- read.csv('pay_data.csv', header = T)
head(pay_data,10) # user_id product_type pay_method  price
table(pay_data$product_type)

# install.packages('reshape2')
library(reshape2) # dcast() 함수 제공 

# (1) 고객별 상품 유형에 따른 구매금액 합계 파생변수 생성   
product_price <- dcast(pay_data, user_id ~ product_type, sum, na.rm=T) 
# 기존 변수 1개가 5개의 변수로 늘어남
head(product_price, 3) # 행(고객 id) 열(상품 타입), sum(price)

names(product_price) <- c('user_id','식료품(1)','생필품(2)','의류(3)','잡화(4)','기타(5)')
head(product_price, 3) # 칼럼명 수정 확인 

# (2) 파생변수 추가(data.frame 합치기) 
library(dplyr) # 패키지 로딩

user_pay_data <- left_join(user_data, product_price, by='user_id')
head(user_pay_data,10)

# (3) 총 구매금액 파생변수 생성(사칙연산 : 지급방법 이용) 
user_pay_data$총구매금액 <- user_pay_data$`식료품(1)` +user_pay_data$`생필품(2)`+user_pay_data$`의류(3)` +
  user_pay_data$`잡화(4)` + user_pay_data$`기타(5)`
head(user_pay_data)