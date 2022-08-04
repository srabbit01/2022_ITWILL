# chap11_Parameter_test 
# 모수(모평균,모분산)의 유의성 검정

############################################
### 1. Z검정 vs T검정 
############################################

## 1. Z분포/검정
# - 모집단 정규분포이고, 모집단의 분산(표준편차)이 알려진 경우
# - 모집단의 분산이 알려지지 않고, 표본의 크기가 충분히 큰 경우(n >= 30)
# - 표본으로 모평균 신뢰구간 추정/검정  

# [연구환경] 
# 우리나라 중학교2 남학생 평균키=168cm(모평균), 표준편차=3cm(모분산) 알려질 때 
# 표본 100명을 대상으로 95신뢰수준에서 모평균의 신뢰구간을 추정한다.

# 귀무가설(HO) : 모평균 168cm와 차이가 없다.

# 1) 표본 추출 : 모집단에서 100명 표본 추출  
x <- rnorm(100, mean=168, sd = 3) # 연속확률변수 x: N(168,3^2)
mean(x) # 평균: 평균과 근사한 샘플 생성
sd(x) # 표준편차: 표준편차와 근사한 샘플 생성
# 샘플의 수가 많을 수록, 모집단의 특성과 비슷(평균과 표준편차 거의 비슷)

# 2) 정규성 검정 : 대칭분포 확인
shapiro.test(x) # 정규성검정 : 기본 가정 충족 

# 3) Z검정 : 모평균 검정
# install.packages('BSDA')
library(BSDA)

# 가설검정 : 확률변수 x vs 모평균(168) 차이 검정
z.test(x, alternative = 'two.sided', mu=168, sigma.x = 3, conf.level = 0.95)
# z.test(x: 확률변수, alternative = 'two.sided': 양측검정, mu=168:모평균, sigma.x = 3:모표준편차, conf.level = 0.95:신뢰수준)

# z = -0.66897, p-value = 0.5035 : 검정통계량 -> 신뢰수준이 결정되면 자동으로 유의수준 결정
# alternative hypothesis: true mean is not equal to 168
# 95 percent confidence interval:
#  167.2113 168.3873 -> 95% 신뢰수준 하에 추정된 신뢰구간 (모평균이 나올 구간)
# sample estimates:
#  mean of x 
# 167.7993

# 가설검정 해석1) p-value > 알파: 채택 (통상적으로 p-value를 이용하여 채택)
# 가설검정 해석2) 확률변수 x 평균이 신뢰구간 안에 들어간 경우: 채택

# z 검정통계량 계산
# z 검정통계량 = (표본평균-모평균)/(모표준편차/루트(표본수))
x_bar=mean(x)
mu=168
sigma=3
n=100
z=(x_bar-mu)/(sigma/sqrt(n))
z # [1] -0.6689699
# z 검정통계량과 신뢰수준 간의 관계 +-1.96(신뢰수준 95%) : 95% 신뢰수준의 채택역에 들어오는지 확인

# 모평균의 신뢰구간 추정식 적용
x_bar=mean(x)
z_val=1.96 # 신뢰수준 z값
sigma=3
n=100

minval = x_bar - z_val*(sigma/sqrt(n))
maxval = x_bar + z_val*(sigma/sqrt(n))
minval; maxval

## 2. T분포/검정 
# - 모집단 정규분포이고, 모집단의 분산(표준편차)이 알려지지 않은 경우(n < 30)
# - 표본의 표준편차이용 모평균 신뢰구간 추정

# 우리나라 중2 남학생 평균키=168cm, 표준편차=3cm(표본표준편차) 알려질 때
# 표본 28명을 대상으로 95신뢰수준에서 모평균의 신뢰구간 추정한다.

# 귀무가설(HO) : 모평균 168cm와 차이가 없다.

# 1) 표본 추출 : 모집단에서 28명 표본 추출  
x <- rnorm(28, mean=168, sd = 3) # 연속확률변수 x
mean(x) # 평균
sd(x) # 표준편차

# 2) 정규성 검정 : 대칭분포 확인 
shapiro.test(x) # H0 : 정규분포와 차이가 없다.

# 3) T 검정 : 평균차이 검정  
t.test(x,alternative = 'two.sided',mu=168,conf.level = 0.95) # 확률변수 x vs 모평균(168) 차이 검정  
# sigma 속성 x: 모수 지정하지 않아 넣을 수 없음

# t = -0.68494, df = 27, p-value = 0.4992 : 알파값보다 작아 귀무가설 채택
# alternative hypothesis: true mean is not equal to 168
# 95 percent confidence interval:
#  166.5875 168.7055 # 신뢰구간에 모평균이 포함되지 않음: 귀무가설 채택
# sample estimates:
#  mean of x 
# 167.6465  # 신뢰구간으로 보았을 때, 채택 (이론상)

# 자유도: t분포표의 값 확인
# t검전통계량 임계값(t분포표: df, 알파)
# t=-2.7535(절대값) > 2.052 -> 기각

# 1) p-value 이용 가설검정 : p-value > 알파(0.05) -> 가설 채택   
# 가설채택: p-value < 알파(0.05)
# 가설기각: p-value > 알파(0.05)

# 2) T검정통계량 이용 가설검정   
# 가설 기각 : T검정통계량(절대값) > 임계값(t분포표 이용)   
# 가설 채택 : T검정통계량(절대값) < 임계값(t분포표 이용)   

# 3) 신뢰구간 이용 가설검정
# 가설기각: 신뢰구간에 모평균이 포함되지 않은 경우
# 가설채택: 신뢰구간에 모평균이 포함되는 경우

# t 검정통계량 계산
# t 검정통계량 = (표본평균-모평균)/(모표준편차/루트(표본수))
x_bar=mean(x)
mu=168
S=sd(x) # 표본표준편차
n=28
t=(x_bar-mu)/(S/sqrt(n))
t # [1] -0.6849398

# 모평균의 신뢰구간 추정식 적용
x_bar=mean(x)
t_val=2.052 # t분포표 이용(df,알파) -> 정규분포를 따르기 않기 때문에
S=sd(x)
n=28

minval = x_bar - z_val*(sigma/sqrt(n))
maxval = x_bar + z_val*(sigma/sqrt(n))
minval; maxval


############################################
### 2. 단일표본 T검정
############################################
# - 모집단의 모평균(𝜇)과 표본의 평균 간의 차이가 있는지를 검정

# 1. 실습파일 가져오기
setwd("c:/ITWILL/3_Rwork/data")
data <- read.csv("one_sample.csv", header=TRUE)
str(data) # 150
head(data)
x <- data$time
head(x)

# 2. 기술통계량 평균 계산
summary(x) # NA-41개
mean(x) # NA

x <- na.omit(x) # NA 제외 
mean(x)

# 3. 정규분포 검정
# 정규분포(바른 분포) : 확률변수 x에 대한 정규성 검정 
# 귀무가설(H0) : 정규분포와 차이가 없다.
shapiro.test(x) # 정규분포 검정 수행
# p-value = 0.7242

# 4. 가설검정 - 모수/비모수
# 정규분포(모수검정) -> t.test()
# 비정규분포(비모수검정) -> wilcox.test()

# 1) 양측검정 - 정제 데이터와 5.2시간 비교 (x=mu)
t.test(x, mu=5.2, alter="two.side", conf.level=0.95) 
# t=3.9461, df=108, p-value=0.0001417 -> 귀무가설 기각

# 2) 방향성이 있는 대립가설 검정 (x > mu)
t.test(x, mu=5.2, alter="greater", conf.level=0.95) 

# 3) 방향성이 있는 대립가설 검정 (x < mu)
t.test(x, mu=5.2, alter="less", conf.level=0.95) 


############################################
###  3. 독립표본 T검정
############################################
# - 서로 독립된 모집단으로 부터 추출된 두 표본의 평균 차이 검정

# 1. 실습파일 가져오기
data <- read.csv("two_sample.csv")
data 
head(data) #4개 변수 확인
summary(data) # score - NA's : 73개

# 2. 두 집단 subset 작성(데이터 정제,전처리)
# result <- subset(data, !is.na(score), c(method, score))
dataset <- data[c('method', 'score')]
table(dataset$method)

# 3. 데이터 분리
# 1) 교육방법 별로 분리
method1 <- subset(dataset, method==1)
method2 <- subset(dataset, method==2)

# 2) 교육방법에서 점수 추출
method1_score <- method1$score
method2_score <- method2$score

# 3) 기술통계량 
length(method1_score); # 150
length(method2_score); # 150
mean(method1_score,na.rm=T) # 5.556881
mean(method2_score,na.rm=T) # 5.80339

# 4. 등분산성 검정 : 두 집단의 분산 차이 검정
var.test(method1_score, method2_score) 
# 동질성 분포 : t.test()
# 비동질성 분포 : wilcox.test()

# 5. 가설검정 - 두집단 평균 차이검정
t.test(method1_score, method2_score, alter="two.sided", conf.int=TRUE, conf.level=0.95)
# t = -2.0547, df = 218.19, p-value = 0.0411 -> 귀무가설 기각 (유의수준과 큰 차이가 없어 결론 모호)

# 방향성이 있는 연구가설 검정 : 교육방법1 > 교육방법2
t.test(method1_score, method2_score, alter="greater", 
       conf.int=F, conf.level=0.95) # p-value = 0.9794(x)

# 방향성이 있는 연구가설 검정 : 교육방법1 < 교육방법2
t.test(method1_score, method2_score, alter="less", 
       conf.int=F, conf.level=0.95) # p-value = 0.02055 (o)

############################################
###  4. 분산분석 : 세 집단 이상 평균 차이 
############################################

######################
## 일원 배치 분산분석
######################
# 세 집단 이상 평균차이 검정 = 분산분석(집단별 분산의 차이) : 분산의 비율 차이  
# 용도 : 정규분포를 따르는 세 집단 이상의 분산에 대한 가설검정
# 독립변수 : 범주형(집단), 종속변수 : 숫자(등간/비율)


# 1. 파일 가져오기
getwd()
setwd("E:/03. R/data")
data <- read.csv("three_sample.csv")

# 2. 데이터 정제/전처리 - NA, outline 제거
data <- subset(data, subset=!is.na(score), select=c(method, score)) 
data # method, score

# (1) 차트이용 - ontlier 보기(데이터 분포 현황 분석)
plot(data$score) # 차트로 outlier 확인 : 50이상과 음수값
barplot(data$score) # 바 차트
mean(data$score) # 14.45

# (2) outlier 제거 - 평균(14) 이상 제거
length(data$score)#91
data2 <- subset(data, score <= 14) # 14이상 제거
length(data2$score) #88(3개 제거)

# (3) 정제된 데이터 보기 
x <- data2$score
boxplot(x)
plot(x)

# 3. 집단별 subset 작성
# method: 1:방법1, 2:방법2, 3:방법3
data2$method2[data2$method==1] <- "방법1" 
data2$method2[data2$method==2] <- "방법2"
data2$method2[data2$method==3] <- "방법3"

table(data2$method2) # 교육방법 별 빈도수 

# 4. 등분산성 검정 : 동질성 검정 
# bartlett.test(종속변수 ~ 독립변수) # 독립변수(세 집단)
bartlett.test(score ~ method2, data=data2)
str(data2)

# 귀무가설 : 집단 간 분포의 모양이 동질적이다.
# 해설 : 유의수준 0.05보다 크기 때문에 귀무가설을 기각할 수 없다. 

# 동질한 경우 : aov() - Analysis of Variance(분산분석)
# 동질하지 않은 경우 - kruskal.test()

# 5. 분산검정(집단이 2개 이상인 경우 분산분석이라고 함)
# aov(종속변수 ~ 독립변수, data=data set)

# 귀무가설 : 집단 간 평균에 차이가 없다.
result <- aov(score ~ method2, data=data2)

# aov()의 결과값은 summary()함수를 사용해야 p-value 확인 
result
summary(result) 

# 6. 사후검정
TukeyHSD(result)
# diff        lwr        upr     p adj
# 방법2-방법1  2.612903  1.9424342  3.2833723 0.0000000 -> 차이 있음
# 방법3-방법1  1.422903  0.7705979  2.0752085 0.0000040 -> 차이 있음
# 방법3-방법2 -1.190000 -1.8656509 -0.5143491 0.0001911 -> 차이 있음
# diff: 집단 간 차이(upr~lwr), p adj: 유의확률(0.05 미만이면 차이가 있음)

plot(TukeyHSD(result))
# 95% 신뢰구간 내에 0이 표함된 경우, 평균의 차이 없음
# 95% 신뢰구간 내에 0이 표함되지 않은 경우, 평균의 차이 있음

###############################################
## 그룹별 통계 : 분산분석 사후검정에서 이용 
###############################################
#install.packages('dplyr')
library(dplyr)

# 형식) 
# df %>% group_by('범주형변수')
#   %>% summarize(var_name = function(column_name))

# function : sum, mean, median, sd, var, min, max 등 
# 경고메시지 무시 

# 교육방법별 점수 평균 
data2 %>% group_by(method2) %>% summarize(avg = mean(score))

# method2   avg
#   <chr>   <dbl>
# 1 방법1    4.19
# 2 방법2    6.8 
# 3 방법3    5.61

#####################
## 비모수 검정: iris
#####################
names(iris)

# 1. 등분산성 검정
bartlett.test(Sepal.Length~Species,data=iris)
# p-value = 0.0003345 < 0.05 : 기본 가정 충족 X

# 2. 분산분석
result=kruskal.test(Sepal.Length~Species,data=iris)
str(iris)
#  p-value < 2.2e-16: 적어도 한 집단 이상 평균 차이가 있음
unique(iris$Species) # setosa     versicolor virginica 
# 별도의 사후검정 X
summary(result)
TukeyHSD(result)

# 3. 사후검정
iris %>% group_by(Species) %>% summarize(avg = mean(Sepal.Length))
# Species      avg
#    <fct>      <dbl>
# 1 setosa      5.01
# 2 versicolor  5.94
# 3 virginica   6.59

6.59-5.01 # virginica - setosa: 1.58

######################
## 이원 배치 분산분석: y ~ x1 + x2
######################

# avo(종속변수~독립변수1+독립변수2,data=datasert)

# [연구환경]
# 쇼핑몰 고객의 연령대, 시간대 별 구매현황 분석
# 종속변수: 구매 수량
# 독립변수1: 연령대(30,40,50)
# 독립변수2: 시간대(오전,오후)

# step1: 자료 생성
age=round(runif(100,min=20,max=49)) # 20~49세
time=round(runif(100,min=0,max=1)) # 오전(0),오후(1)
buy=round(runif(100,min=1,max=10)) # 1~10개 구매
data=data.frame(age=age,time=time,buy=buy)
str(data)
# $ age : num  42 37 28 33 26 23 46 21 48 31 ... -> 범주형
# $ time: num  0 1 0 1 0 1 1 0 0 0 ... -> 범주형
# $ buy : num  2 2 6 7 7 9 3 6 3 3 ...

# 연령대 레코딩: 20, 30, 40
data$age2[data$age<30]='20대'
data$age2[data$age>=30 & data$age<40]='30대'
data$age2[data$age>=40]='40대'

# 시간대 레코딩: 오전(0), 오후(1)
data$time2[data$time==0]='오전'
data$time2[data$time==1]='오후'
data

table(data$age2,data$time2)
#       오전 오후
# 20대   22   11
# 30대   17   20
# 40대   16   14

# 독립변수(숫자형) -> 요인형 변환
data$age2=as.factor(data$age2)
data$time2=as.factor(data$time2)
str(data)

# step2: 등분산성 결정
bartlett.test(buy~age2,data=data) # p-value = 0.9014
bartlett.test(buy~time2,data=data) # p-value = 0.6614

# step3: 이원배치 분산분석
model=aov(buy~age2+time2,data=data)

# step4: 모수 분산분석 결과 해석
summary(model)
#              Df Sum Sq Mean Sq F value Pr(>F)
# age2         2    0.8   0.392   0.063  0.939 -> 연력대 별 차이 없음
# time2        1    0.5   0.519   0.083  0.773 -> 시간대 별 차이 없음
# Residuals   96  597.2   6.221

# step5: 사후검정
TukeyHSD(model)
# $age2
#                diff       lwr      upr     p adj
# 30대-20대 -0.05896806 -1.480659 1.362723 0.9946395 -> 거의 100% 가설 채택
# 40대-20대  0.15454545 -1.343299 1.652390 0.9672992
# 40대-30대  0.21351351 -1.245267 1.672294 0.9353154

# $time2
#                diff       lwr       upr     p adj
# 오후-오전 -0.1426153 -1.137782 0.8525514 0.7766674

par(mfrow=c(1,2))
plot(TukeyHSD(model)) # 각 집단 별 2개의 그래프 생성


####################
###  5. 모분산 검정
####################
# 별도 패키지 필요
# install.packages('DescTools')
library(DescTools)
# 1. 화률변수 X 모분산 검정
x=rnorm(50,0,sd=1) # N(0,1^2)
x
x2=rnorm(50,0,sd=2) # N(0,2^2)
x2

# 1) 카이제곱 검정: 1개의 모집단 대상 (모분산 유의성 검정)
# - 모분산과 표본분산의 차이 검정
# - 모분산을 알고 있는 경우
VarTest(x,sigma.squared=1,conf.level=0.95)
# varTest(변수,sigma.squared=모분산,conf.level=신뢰구간)
# X-squared = 56.603, df = 49, p-value = 0.4248 > 0.05: 귀무가설 채택 (차이없음)

VarTest(x2,sigma.squared=2,conf.level=0.95)
# X-squared = 79.864, df = 49, p-value = 0.00701 < 0.05: 귀무가설 기각

# 2) F-검정: 2개의 모집단 대상 (두 모집단 간 분산 차이 검정)
VarTest(x,x2,conf.level=0.95)
# p-value = 0.0004056 < 0.05: 귀무가설 기각 (차이가 있음)
# p-value: 1에 가까울 수록 분산 차이 없음, 0에 가까울 수록 분산 차이 큼
# ratio of variances 
# 0.3543739  : 분산비율 (1에 가까울 수록 분산 차이 없음, 0에 가까울 수록 분산 차이 큼)

VarTest(x2,x2,conf.level=0.95) # 분산비 1 = 두 분산 간 차이 없음

# VarTest() vs var.test()

# 공통점: 등분산성 검정 (F검정으로 두 집단 간 분산 차이 검정)

# 분산 유의성 검정: VarTest() -> 한 집단의 모분산 검정
# 두 집단 간 등분산성 검정: var.test()