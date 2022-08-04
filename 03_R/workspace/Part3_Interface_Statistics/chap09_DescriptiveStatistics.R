# chap09_Descriptive Statistics

################################################
## 기술통계(Descriptive Statistics)
################################################
# 기술통계 : 자료를 요약하는 기초적인 통계량, 변수의 특성 파악 및 모집단 유추
# 대푯값 : 평균(Mean), 합계(Sum), 중위수(Median), 최빈수(mode), 사분위수(quartile) 등
# 산포도 : 분산(Variance), 표준편차(Standard deviation), 최소값(Minimum), 최대값(Maximum), 범위(Range) 등 
# 비대칭도 : 왜도(Skewness), 첨도(Kurtosis)


# - 실습파일 가져오기
getwd()
setwd("E:/03. R/data")
data <- read.csv("descriptive.csv", header=TRUE)

head(data) # 데이터셋 확인
# data Mart
#---------------------------------------------------------------------------------
# resident   gender      age	  level	      cost	   type    	 survey	   pass
# 거주지역   성별       나이  학력수준     생활비  학교유형  만족도    합격여부
# 명목(1~3)  명목(1,2)  비율  서열(1,2,3)  비율    명목(1,2) 등간(5점) 명목(1,2)
#---------------------------------------------------------------------------------
# 인구통계학변수 : 거주지역, 성별, 나이, 학력수준

# 1. 척도별 기술통계량

# 1) 명목/서열 척도 변수의 기술통계량
# - 명목상 의미없는 수치로 표현된 변수 - 성별(gender)     
length(data$gender)
summary(data$gender) # 최소,최대,중위수,평균-의미없음
table(data$gender) # 각 성별 빈도수 - outlier 확인-> 0, 5

data <- subset(data,data$gender == 1 | data$gender == 2) # 성별 outlier 제거
x <- table(data$gender) # 성별에 대한 빈도수 저장
x # outlier 제거 확인
barplot(x) # 범주형(명목/서열척도) 시각화 -> 막대차트

prop.table(x) # 비율 계산 : 0< x <1 사이의 값
y <-  prop.table(x)
round(y*100, 2) #백분율 적용(소수점 2자리)


# 2) 등간척도 변수의 기술통계량
# - 속성의 간격이 일정한 변수(survey) 
survey <- data$survey
survey

summary(survey) # 만족도(5점 척도)인 경우 의미 있음 
x1<-table(survey) # 빈도수
x1

# 등간척도 시각화 -> 히스토그림
pie(x1)

# 3) 비율척도 변수의 기술통계량 : cost 변수   
summary(data$cost) # 요약통계량 
mean(data$cost) # NA
data$cost

# 데이터 정제 - 결측치 제거 및 outlier 제거
plot(data$cost)
data <- subset(data,data$cost >= 2 & data$cost <= 8) # 총점기준

# cost변수 추출 
cost <- data$cost
cost


###  2. 대푯값 
# 1) 평균(Mean)
mean(cost)
# 평균이 극단치에 영향을 받는 경우 -> 중위수(median) 대체

# 2) 중위수(Median) : 정렬 -> 중앙값
median(cost) # 5.4  

# 중앙 위치 계산
length(cost) # [1] 248 = (n/2+((n/2)+1))/2
idx= length(cost)/2

# 정령
cost_asc=sort(cost) # 오름차순 정렬  
(cost_asc[idx]+cost_asc[idx+1])/2 # 5.4


# 3) 최빈수(mode) : 연속형변수 hist() 이용  
hist(cost) # 가장 높은 봉의 계급

# <최빈수, 중위수, 평균의 관계: 단봉인 경우>
# 최빈수=중위수=평균: 왜대=0 좌우대칭
# 최빈수 > 중위수 > 평균: 왜도<0 오른쪽으로 기울어짐
# 최빈수 < 중위수 < 평균: 왜도<0 왼쪽으로 기울어짐

# 4) 합계(Sum) 
sum(cost)

# 5) 사분위수(quartile) 
quantile(cost, 1/4) # 1 사분위수 - 25%, 4.6
quantile(cost, 3/4) # 3 사분위수 - 75%, 6.2
quantile(cost)
# 0%  25%  50%  75% 100% 
# 2.1  4.6  5.4  6.2  7.9 
# 중위수 = 제2사분위수

# 이상치 처리
# IQR = Q3 - Q1
# Q1 - 1.5 * IQR ~ Q3 + 1.5 * IQR

# sort vs order : 정렬
# sort(): 정렬된 값을 반환 (벡터 자료 이용)
# order(): 정렬된 값의 색인 반환 (행렬 자료 이용)

sort(data$cost) # 오름차순 정렬
sort(data$cost,decreasing=T) # 내림차순 정렬

order(data$cost) # 값의 색인 확인 (오름차순 정렬)
data[17,] # 17행 -> 19행 이름: 앞부분 전처리 과정에서 2개의 행 제거되었기 때문
order(data$cost,decreasing=T) # 값의 색인 확인 (내림차순 정렬)

# [시험] cost 칼럼 기준으로 dataset 정렬 -> 상위 10행 추출
df=head(data[order(data$cost),],10)
names(df) # 열 이름
row.names(df) # 행 이름
row.names(df)=1:10
df
mean(df$cost) # 2.8

###  3. 산포도 
# 1) 분산(Variance)
var(x) # 분산 : 1.291597

# 분산 수식 
mu = mean(x)
n = length(x)
var = sum((x-mu)^2) / n
var # 1.291597

# 2) 표준편차(Standard deviation)
sd(x) # 표준편차는 분산의 제곱근
sqrt(var(x))

# 표준편차 -> 분산 
sd(x) ** 2

# 3) 최소값/최대값/범위 
min(x) # 최소값
max(x) # 최대값
range(x) # 범위(min ~ max)

###########################
### [시험] 표준값 vs 편차값
###########################
# 1) 표준값 = (x-평균)/표준편차
# - 동일한 척도(scale) 기준으로 가치 평가
# ex) 홍길동: 국어 70점 (반 평균: 59, 편차: 15), 수학: 70점 (반 평균: 51, 편차: 81)
kor=(70-59)/15
mat=(50-51)/18
kor; mat # [1] 국어: 0.7333333 [1] 수학: -0.05555556

# 2) 편차값 = 표준값 * 편차 + 평균
# - 표준값을 대상으로 가치 판단, 표준값 증명(Proof)
# 평균: 50, 표준편차: 10
kor_sd=kor*10+50
mat_sd=mat*10+50
kor_sd; mat_sd # [1] 57.33333 [1] 49.44444

### 4. 비대칭도 :  패키지 이용 
install.packages("moments")  # 왜도/첨도 위한 패키지 설치   
library(moments)

cost <- data$cost # 정제된 data
cost
# 1) 왜도 - 평균을 중심으로 기울어진 정도
skewness(cost) # -0.297234
# 0보다 크면 왼쪽 기울어짐(오른쪽방향 비대칭 꼬리) 
# 0보다 작으면 오른쪽 기울어짐(왼쪽방향 비대칭 꼬리)

# 2) 첨도 - 표준정규분포와 비교하여 얼마나 뽀족한가 측정 지표
kurtosis(cost) # 2.683438     
# 정규분포 첨도 = 3

# 3) 히스토그램 : 대칭성 
hist(cost)

######################################
## 밀도분포곡선과 표준정규분포 곡선
######################################
# 단계1. 히스토그램 확률밀도/표준정규분포 곡선 
hist(cost, freq = F) # (확률)밀도 추정 
lines(density(cost), col='blue') # PDF
# 밀도분포곡선 받아서 곡선 분포에 적합한 곡선 그림

# 단계2. 표준정규분포 곡선 
?dnorm # Normal Distribution
#평균 및 표준 편차를 이용하여 표준정규 분포의 확률 밀도 분포 계산 
x <- seq(0, 8, 0.1) # 0.1씩 벡터 생성 # 범위지정정
x
curve(scale(cost),col='red',add=T)
curve(dnorm(x, mean(cost), sd(cost)), col='red', add = T)
# 정규분포 추정 받아서 정규분포 그리는제 적합

# <왜도, 평균, 중위수, 최빈수 관계> ppt.26

# 단계3. QQ-plot
cost
summary(cost)
quantile(cost,0.25)
qqnorm(cost, main = 'cost QQ-plot')
qqline(cost, col='red')

# 단계4. 정규성 검정: 귀무가설=정규 분포와 차이가 없음
shapiro.test(cost)
# W = 0.98187, p-value = 0.002959 -> 정규 분포와 차이가 있음을 확인 가능
# p-value > 유의수준(알파:0.05): 채택
# p-value < 유의수준(알파:0.05): 기각 
# [해석] 정규분포와 차이가 있음


### 5. 기술통계 보고서 작성법
# - 빈도분석 : 논문에서 인구통계학적 특성 반영   

# 1) 거주지역 
data$resident2[data$resident == 1] <-"특별시"
data$resident2[data$resident >=2 & data$resident <=4] <-"광역시"
data$resident2[data$resident == 5] <-"시구군"

x<- table(data$resident2)
prop.table(x) # 비율 계산
y <-  prop.table(x)
round(y*100, 2) #백분율 적용(소수점 2자리)

# 2) 성별
data$gender2[data$gender== 1] <-"남자"
data$gender2[data$gender== 2] <-"여자"
x<- table(data$gender2)
prop.table(x) # 비율 계산
y <-  prop.table(x)
round(y*100, 2) #백분율 적용(소수점 2자리)

# 3) 나이
summary(data$age)# 40 ~ 69
data$age2[data$age <= 45] <-"중년층"
data$age2[data$age >=46 & data$age <=59] <-"장년층"
data$age2[data$age >= 60] <-"노년층"
x<- table(data$age2)
prop.table(x) # 비율 계산
y <-  prop.table(x)
round(y*100, 2) #백분율 적용(소수점 2자리)

# 4) 학력수준
data$level2[data$level== 1] <-"고졸"
data$level2[data$level== 2] <-"대졸"
data$level2[data$level== 3] <-"대학원졸"

x<- table(data$level2)
prop.table(x) # 비율 계산 
y <-  prop.table(x)
round(y*100, 2) #백분율 적용(소수점 2자리)

# 5) 합격여부
data$pass2[data$pass== 1] <-"합격"
data$pass2[data$pass== 2] <-"실패"
x<- table(data$pass2)
prop.table(x) # 비율 계산 : 0< x <1 사이의 값
y <-  prop.table(x)
round(y*100, 2) #백분율 적용(소수점 2자리)