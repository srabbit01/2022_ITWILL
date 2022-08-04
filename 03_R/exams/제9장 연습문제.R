#################################
## <제9장 연습문제>
################################# 

#01. 다음 데이터 셋을 이용하여 각 단계별로 빈도분석과 기술통계 및 정규성을 검정하시오.

setwd("E:/03. R/data")
data <- read.csv("descriptive.csv", header=TRUE)
head(data) # 데이터셋 확인

# 단계1> 명목척도 변수인 학교유형(type), 합격여부(pass) 변수에 대해 빈도분석을 수행하고 
# 결과를 막대그래프와 파이차트로 시각화하기 
type=data$type
pass=data$pass
type=table(type)
pass=table(pass)

barplot(type)
barplot(pass)

pie(type)
pie(pass)

# 단계2> 비율척도 변수인 나이 변수에 대해 요약치(평균,표준편차)와 비대칭도(왜도와 첨도)
# 통계량을 구하고, 히스토그램으로 비대칭도 설명하기 
age=data$age
range(age)
mean(age)
sd(age)
skewness(age)
kurtosis(age) # 1.866
hist(age)
# 왜도가 0보다 조금 크기 때문에 오른쪽 방향으로 비대칭 꼬리가 생성
# 첨도가 3보다 작기 떄문에 표준정규분포보다 완만한 형태

# 단계3> 나이 변수에 대한 밀도분포곡선과 정규분포 곡선으로 정규분포 검정하기 
hist(age,freq=F)
lines(density(age),col='blue')

x=seq(35,80,0.1)
x
curve(dnorm(x,mean(age),sd(age)),col='red',add=T)

# 단계4> 나이 변수에 대한 정규성 검정으로 가설검정하기
shapiro.test(data$age)
