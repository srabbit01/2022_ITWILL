# chap14_LinearRegression

######################################################
# 회귀분석(Regression Analysis)
######################################################
# - 특정 변수(독립변수:설명변수)가 다른 변수(종속변수:반응변수)에 어떠한 영향을 미치는가 분석

###################################
## 1. 단순회귀분석 
###################################
# - 독립변수와 종속변수가 1개인 경우

# 단순선형회귀 모델 생성  
# 형식) lm(formula= y ~ x 변수, data) 

# lm(formula=y변수~x변수,data=dataset): 선형회귀 모델 생성 변수

getwd()
setwd("E:/03. R/data")
product <- read.csv("product.csv", header=TRUE)
head(product) # 친밀도 적절성 만족도(등간척도 - 5점 척도)

str(product) # 'data.frame':  264 obs. of  3 variables:
y = product$'제품_만족도' # 종속변수
x = product$'제품_적절성' # 독립변수
mt=matrix(c(x,y),ncol=2,byrow=T)
df <- data.frame(x, y)

# 회귀모델 생성 
# lm() 함수: r의 기본함수 (선형회귀분석 함수)
# formula=식(y~x), data=데이터셋(출처)
result.lm <- lm(formula=y~x, data=df)
result.lm # 회귀계수 
# Coefficients: = 회귀계수 제공
# (Intercept)            x
#      0.7789       0.7393
# Intercept: 절편, x: 기울기

# 선형회귀방정식(1차방정식)
# Y = aX + b (a: 기울기, b: y절편)
X=4
a=0.7393
b=0.7789
Y=a*X+b
Y # 3.7361 = 예측치(적합치) = fit value

Y2=3 # 관측치(정답)
# 대부분 관측치와 예측치 간 오차(Error) 발생

# 오차(잔차)
Err=Y-Y2
Err # 0.7361: 오차의 부호 상관없음 # 오차는 절대값으로 표현
# 오차가 작을 수록 예측력 좋음

# 객체를 통해 호출 가능한 변수 확인
names(result.lm)
# coefficients: 회귀계수(절편과 기울기) 정보
result.lm$coefficients
# residuals: 오차(잔차) 정보
result.lm$residuals
# fitted.values: 적합치=예측치 (회귀방정식을 근거로 계산)
result.lm$fitted.values

# 회귀모델 예측: x=n 일떄 y=? 새로운 데이터 예측
predict(result.lm, data.frame(x=5)) # 4.475239

# (2) 선형회귀 분석 결과 보기
summary(result.lm)
# 회귀모델 분석 결과 요약
# <분석 절차>
# 1. 모델의 통계적 유의성 검정: 유의확률(p-value) 확인(f-검정 이용) -> p-value: < 2.2e-16 유의수준(0.05)보다 작으면 통계적으로 유의
# 2. 모델의 설명력: 수정된 R^2 (객관화된 결정계수값) 확인 -> Adjusted R-squared:  0.5865 < Multiple R-squared:  0.5881
#                                                            기준: 1에 수렴정도 (1에 가까울 수록 예측력 좋음) -> 약 60% 예측력 있음
#                                                            매우 높은 설명력을 가지는 것은 아니나, 60% 정도
# 3. x변수의 유의성 검정: Pr(>|t|) -> x가 y에 대한 영향력 확인 (인과관계 강도)
#                         -> t검정 통계량을 이용해 얻어진 p-value를 이용
#                         -> 영향력은 *이 많을 수록 영향력(인관관계 있음) 큼 (귀무가설 기각, 대립가석 채택)

# (3) 단순선형회귀 시각화
# x,y 산점도 그리기 
plot(formula=y ~ x, data=df,xlim=c(0,5), ylim=c(0,5))
# 회귀분석
result.lm <- lm(formula=y ~ x, data=df)
# 회귀선 
abline(result.lm, col='red')

# 제품의 적절성은 만족도에 강한 영향력을 미침

#########################
##  회귀계수 vs 결정계수
#########################
# - 회귀계수: x의 기울기
# - 결정계수: (R^2): 회귀모형에서 설명력을 나타내는 지표
# 결정계수 수식 = SSR(회귀계수 제곱의 합) / SST(전체 제곱의 합)

###################################
## 2. 다중회귀분석
###################################
# - 여러 개의 독립변수 -> 종속변수에 미치는 영향 분석
# 가설 : 음료수 제품의 적절성(x1)과 친밀도(x2)는 제품 만족도(y)에 정의 영향을 미친다.

product <- read.csv("product.csv", header=TRUE)
head(product) # 친밀도 적절성 만족도(등간척도 - 5점 척도)


# 1) 적절성 + 친밀도 -> 만족도  
y = product$'제품_만족도' # 종속변수
x1 = product$'제품_친밀도' # 독립변수2
x2 = product$'제품_적절성' # 독립변수1

df <- data.frame(x1, x2, y)

result.lm <- lm(formula=y ~ x1 + x2, data=df)
#result.lm <- lm(formula=y ~ ., data=df)

# 계수 확인 
result.lm
# Coefficients:
# (Intercept)           x1           x2  
#    0.66731      0.09593      0.68522 

# 다중회귀분석 방정식
x1=3
x2=4
a1=0.09593
a2=0.68522  
b=0.66731      

y=a1*x1+a2*x2+b
y # 예측치: 3.69598
Y=3 # 관측치
Err=Y-y
Err # 오차: 0.69598 -> 0에 가까울 수록 좋음


summary(result.lm)

# 2) 102개 직업군 평판 dataset 이용 
install.packages("car") # 다중공선성 문제 확인  
library(car)

Prestige # car 제공 dataset

# 102개 직업군의 평판 : 교육수준,수입,여성비율,평판(프레스티지),센서스(인구수=직원수)
str(Prestige) 

# 종속변수: income(수입)
# 독립변수: education(교육수준), women(여성비율), prestige(평판) # 직업군 이름은 행의 명
row.names(Prestige) # 행의 명 추출출 (직업군 이름)

model1=lm(income~education+women+prestige,data=Prestige)

model1
# 여성의 비율이 적을 수록 연봉이 많음

summary(model1)
# education의 p-value: 0.347 > 0.05: 종속변수에 영향력이 없음
# education    177.199    187.632   0.944    0.347    : 영향력 없음
# women        -50.896      8.556  -5.948 4.19e-08 ***: 음(-)의 영향력
# prestige     141.435     29.910   4.729 7.58e-06 ***: 양(+)의 영향력

# 다중회귀분석 회귀선 시각화
# install.packages('psych')
library(psych)

newdata=Prestige[c(2,1,3:4)] # 열의 배열 조정
head(newdata)

pairs.panels(newdata)
pairs.panels(newdata,stars=T,lm=T,ci=T)
# stars=T: 상관계수 유의성
# lm=T: 회귀선
# ci=TRUE: 회귀선 신뢰구간
# 타원: 타원의 푝이 좁을 수록 상관성 높음

##################
## 3. 변수 선택법
##################
# stepwise: 전진선택법, 후진선택법, 단계선택법
# 전진선택법: 변수 한 개씩 추가 (절편만 포함시킨 model + 독립변수 1개씩 추가)
# 후진제거법: 전체 변수에서 중요도가 낮은 독립변수 한개 씩 제거
# 단계선택법: 혼합법(전진선택법 + 후진제거법)

data(Prestige)
str(Prestige)
newdata=Prestige[-6]
dim(newdata) # 행 열 = [1] 102   5

model=lm(income~.,data=newdata)
model

model2=lm(income~1,data=newdata)
model2

summary(model)
# Adjusted R-squared:  0.6289 

library(MASS) # 기본 패키지 -> 별도 install 필요 x
# stepAIC(): 모델의 성능을 나타내는 지수값 제공
# 지수값이 낮아야 모델 성능이 좋음

stepAIC(model,direction='backward')
stepAIC(model,direction='both')
stepAIC(model2,direction='forward',scope=income~education+women+prestige)
stepAIC(model2,direction='both',scope=income~education+women+prestige)
?stepAIC
# Step:  AIC=1604.96
# income ~ women + prestige -> 가장 이상적인 모델 독립변수

new_model=lm(income ~ women + prestige,newdata)
new_model
summary(new_model)
# Adjusted R-squared:  0.6327  -> 설명력(예측력)이 높아진 것을 알 수 있음

###################################
# 4. 다중공선성
###################################
# - 독립변수 간의 강한 상관관계로 인해서 회귀분석의 결과를 신뢰할 수 없는 현상
# - 한 독립변수의 값이 증가할 때 다른 독립변수의 값이 증가하거나 감소하는 현상
# - 결정계수(R^2) : 회귀모형에서 설명력을 보여주는 지표
# R^2 = SSR / SST 
# 전체제곱합(SST) = sum((y - y예측치평균)^2)
# 회귀제곱합(SSR) = sum((y예측치 - y예측치평균)^2)

# 분산팽창요인(VIF) = 1 / 1 - R^2
# 결정계수(R)의 값이 1과 가까워지면 VIF값도 커져서 다중공선성 존재가능성 높다.
# - 생년월일과 나이를 독립변수로 갖는 경우
# - 해결방안 : 강한 상관관계를 갖는 독립변수 제거, PCA(차원축소)

# (1) 다중공선성 문제 확인
# install.packages('car')
library(car)
names(iris)
model <- lm(formula=Sepal.Length ~ Sepal.Width+Petal.Length+Petal.Width, data=iris)
vif(model)
# Sepal.Width Petal.Length  Petal.Width 
#   1.270815    15.097572    14.234335

sqrt(vif(model)); sqrt(vif(model)) > 2 # root(VIF)가 2 이상인 것은 다중공선성 문제 의심 

# (2) iris 변수 간의 상관계수 구하기
cor(iris[,-5]) # 변수간의 상관계수 보기(Species 제외) 
# 상관성이 높은 제거 대상 변수 탐색
# 상관계수가 0.9 이상인 것 문제 발생 가능성 높음

summary(model) # Adjusted R-squared:  0.8557 
# Residual standard error: 0.3145

### 어떤 변수를 제거해야 성능이 더 좋은 회귀모델을 만드는지 확인

# (3) 변수 제거(3번) -> 설명력 낮아짐 # 다중공선성 문제 해결
model2 <- lm(formula=Sepal.Length ~ Sepal.Width+Petal.Length, data=iris)
summary(model2) # Adjusted R-squared:  0.838 
# Residual standard error: 0.3333

# (4) 변수 제거(4번) -> 설명력 더 낮아짐 # 다중공선성 문제 해결
model3 <- lm(formula=Sepal.Length ~ Sepal.Width+Petal.Width, data=iris)
summary(model3) # Adjusted R-squared:  0.7033

### 즉, (3) 변수 3번 제거


####################################
## 5. 더미변수 사용 
####################################
# - 범주형 변수를 독립변수로 사용하기 위해서 더미변수 생성
# - 범주형 변수는 기울기 영향 없음(절편에만 영향을 미침)
# - 범주형 변수의 범주가 n개인 경우 n-1개 파생변수 생성
# ex) 혈액형 : A, B, O, AB

#               x1    x2    x3  
#         A      1     0     0
#         B      0     1     0
#         O      0     0     1
#         AB     0     0     0 (기준)

# Factor형 -> dummy 생성 역할 

# 의료비 예측
# - 의료보험 가입자 1,338명을 대상으로 한 데이터 셋으로 의료비 인상 예측 

# 1. 데이터 셋 가져오기 - insurance.csv
insurance <- read.csv('insurance.csv', header = T)
str(insurance) # sex, smoker 명목척도 -> Factor 형변환(숫자형 의미 적용) 
#'data.frame':	1338 obs. of  7 variables:
#$ age     : 나이 : int  19 18 28 33 32 31 46 37 37 60 ...
#$ sex     : 성별 :(x1) Factor w/ 2 levels "female","male": 1 2 2 2 2 1 1 1 2 1 ...
#$ bmi     : 비도만 지수 : num  27.9 33.8 33 22.7 28.9 ...
#$ children: 자녀수 : int  0 1 3 0 0 0 1 3 2 0 ...
#$ smoker  : 흡연 여부 :(x2) Factor w/ 2 levels "no","yes": 2 1 1 1 1 1 1 1 1 1 ...
#$ region  : 지역 Factor w/ 4 levels "northeast","northwest",..: 4 3 3 2 2 3 3 2 1 2 ...
#$ charges : 의료비(y) : num  16885

# 문자로 된 범주형 변수는 더미변수로 변경하여 사용
# 문자형은 문자형으로 읽어옴 (과거 3점대 이하는 csv 파일 문자형 -> 요인형으로 자동 변환)

# 2. 범주(집단)형 변수 확인 
# sex=1(female=0), smoker=1(no=0), levels=1(northeast=0)
insurance$sex # Levels: female(base=0) male=1
insurance$smoker # Levels: no(base=0) yes=1
insurance$region # Levels: northeast(base=0) northwest=1 southeast=2 southwest=3

# 요인형 변환
insurance$sex=as.factor(insurance$sex)
insurance$smoker=as.factor(insurance$smoker)
insurance$region=as.factor(insurance$region)
str(insurance)

# 3. 회귀모델 생성 : 전체 더미변수 계수값 확인 
insurance2 <- insurance[, -c(5:6)] # 흡연, 지역 제외(charges 포함) 
head(insurance2) # age sex bmi children charges

model_ins <- lm(charges ~ ., data=insurance2)
model_ins # 절편과 기울기 보기 
# (Intercept)      age      sexmale          bmi     children  
# -7460.0        241.3       1321.7        326.8        533.2 
# 더미변수 모양: sexmale = 칼럼명+값(원소) -> 기울기는 base가 아닌 남성에 대한 기울기 생성
# base(female)은 절편으로 생성

# [해설] sexmale : 남자가 여자에 비해서 1321.7 의료비 증가
# 만약 더미변수의 base 변경 -> sexfemale= -1321.7

# (Intercept) : 여성(base)의 의료비 평균은 절편에 포함  
# 여성과 남성은 반대되기 떄문에 남성을 base로 두면 -1321.7이 됨


summary(model_ins)
# (Intercept) -7459.97    1773.72  -4.206 2.77e-05 ***
#   age           241.26      22.27  10.835  < 2e-16 ***
#   sexmale      1321.72     622.00   2.125   0.0338 *  
#   bmi           326.76      51.30   6.369 2.61e-10 ***
#   children      533.17     257.94   2.067   0.0389 * 

# 더미변수의 base 변경 -> sexfemale= -1321.7
x <- c('male', 'female')
# 요인형 변경과 동시에 base변경하기 위해 factor 변수 만들어야 함
str(insurance2)
insurance2$sex <- factor(insurance2$sex, levels =c('male','female'))
# 주의: 요인형 변환 + 분서 변환 -> factor() 이용

model_ins <- lm(charges ~ ., data=insurance2)
model_ins # 절편과 기울기 보기 
# (Intercept)          age    sexfemale          bmi     children  
# -6138.2        241.3      -1321.7        326.8        533.2
# [해설] sexfemale : 여자가 남자에 비해서 -1321.7 의료비 절감 
#  더미변수는 기울기에 영향없이, 절편에 영향을 미친다.

# 성별 더미변수(0/1)와 절편 관계
male=1*1321.7-6138.2
male # -4816.5
female=0*1321.7-6138.2
female # -6138.2
male-female # # 1321.7 여성에 비해 남정의 의료 보험비가 1321.7만큼 증가

###################################
# 4개 범주인 경우 
###################################
insurance4 <- insurance[,-c(2, 5)]
names(insurance4)
insurance4$region # Levels: northeast northwest southeast southwest

model_ins <- lm(charges ~ region+children, data=insurance4) # no(base)
model_ins # 절편과 기울기 보기
# (Intercept)  regionnorthwest  regionsoutheast  regionsouthwest  
# 13406.4           -988.8           1329.0          -1059.4 
# =northeast
# 각각의 범주에 대한 기울기 생성

table(insurance4$region)
#northeast(base) northwest southeast southwest 
#     324       325       364       325 
unique(insurance4$region)


##########################################
##  6. 선형회귀분석 잔차검정과 모형진단
##########################################

# 1. 변수 모델링  
# 2. 회귀모델 생성 
# 3. 모형의 잔차검정
#   1) 잔차의 선형성 검정
#   2) 잔차의 정규성 검정
#   3) 잔차의 등분산성 검정 
#   4) 잔차의 독립성(자기상관) 검정 
# 4. 다중공선성 검사 
# 5. 회귀모델 생성/ 평가 


names(iris)

# 1. 변수 모델링 : y:Sepal.Length <- x:Sepal.Width,Petal.Length,Petal.Width
formula = Sepal.Length ~ Sepal.Width + Petal.Length + Petal.Width


# 2. 회귀모델 생성 
model <- lm(formula = formula,  data=iris)
model
names(model)


# 3. 모형의 잔차검정
par(mfrow=c(1,1))
plot(model)
#Hit <Return> to see next plot: 잔차 vs 적합값 -> 잔차의 선형성 검정
#Hit <Return> to see next plot: Normal Q-Q -> 잔차의 정규성검정 
#Hit <Return> to see next plot: 척도 vs 위치 -> 잔차의 등분산성 검정 
#Hit <Return> to see next plot: 잔차 vs 지렛대값 -> 중심을 기준으로 고루 분포 

# (1) 잔차 선형성 검정
plot(model, which =  1) 

# (2) 잔차 정규성 검정
plot(model, which =  2) 
attributes(model) # coefficients(계수), residuals(잔차), fitted.values(적합값)
names(model)
# attributes와 names 비슷
res=residuals(model)
res=model$residuals # 잔차 추출 

res

shapiro.test(res) # 정규성 검정 - p-value = 0.9349 >= 0.05
# 귀무가설 : 정규성과 차이가 없다.

# 정규성 시각화  
hist(res, freq = F) 
qqnorm(res)

# (3) 등분산성 검정 
plot(model, which =  3)  # 잔차가 고르게 분포되어야 함

# (4) 잔차의 독립성(자기상관 검정 : Durbin-Watson) 
install.packages('lmtest')
library(lmtest) # 자기상관 진단 패키지 설치 
dwtest(model) # 더빈 왓슨 값
# p-value = 0.6013 > 0.05 : 관련성 없음 (독립적으로 잔차 생성)

# 잔차분석 결과에 따른 대응
# 1. 극단값 제거
# 2. 자료 부족 -> 새로운 데이터 추가
# 3. 종속변수(y) 변환 -> log(로그변환), 스케일링, 표준화 등을 이용하여 변환
# 잔차 검정을 모두 만족하기 힘듬

# 4. 다중공선성 검사 
library(car)
sqrt(vif(model)) > 2 # TRUE 
# 반드시 다중공선성 검사는 해야함

# 5. 모델 생성/평가 
formula = Sepal.Length ~ Sepal.Width + Petal.Length 
model <- lm(formula = formula,  data=iris)
summary(model) # 모델 평가


######################################
## 7. 기계학습(Machine learning)
######################################
# - 훈련셋으로 학습된 모델을 평가셋으로 평가하여 예측모델을 만드는 기법  

dim(iris) # 행 열 = 150   5
150*0.7 # 7:3 = 훈련 데이터: 105개, 평가 데이터: 45개

# (1) 훈련셋과 평가셋 분류
?sample
# sample() 함수: 훈련데이터와 평가 데이터 추출
# sample(x, size, replace = FALSE, prob = NULL)
# x: 모집단
# size=추출하고자 하는 x의 샘플링 개수
# replace: FALSE면 비복원(중복추출X) TRUE면 복원(중복추출) (기본: FALSE)
# prob: 확률(어떤 확률로 추출?) (기본: 생략)

# nrow(): 행 개수 추출
nrow(iris) # 105

set.seed(123)
x <- sample(x=nrow(iris),size=0.7*nrow(iris)) # 전체중 70%만 추출
x # 105개의 행번호 랜덤(임의) 추출

train <- iris[x, ] # 훈련셋 추출: 70%
test <- iris[-x, ] # 평가셋 추출: 30%
dim(train) # 105 5
dim(test) # 45 5

# (2) model 생성 : 훈련셋 이용 
lm_model <- lm(formula=Sepal.Length ~ Sepal.Width + Petal.Length, data=train)

summary(lm_model) # Adjusted R-squared:  0.8213: 통상적으로 0.8 이상이면 예측력이 좋은 것으로 판단

# (3) model 예측치 : 평가셋 이용 
predict(lm_model,data.frame(Sepal.Width=3,Petal.Length=4))

y_pred <- predict(object=lm_model, test) # test에는 훈련에 사용되는 독립변수가 반드시 포함 
# 자동으로 해당 독립변수 입력
# Sepal.Width + Petal.Length -> y_pred

y_true <- test$Sepal.Length # 관측치(정답)

# (4) model 평가 : 예측치와 관측치 이용 

# 1) 평균제곱오차(MSE) = mean(err ^ 2)
err <- y_pred - y_true
MSE = mean(err ^ 2) # 제곱(square): 부호 양수화(절대값 생성), 패널티 역할: 오차가 작으면 간소화, 오차가 크면 극대화
MSE # 0.1361803 -> 0 수렴정도 

# 2) 평균제곱오차제곱근(RMSE, Root MSE)
RMSE=sqrt(MSE)
RMSE # 0.3054779

# 3) 결정계수(R^2)
r2_score=cor(y_true,y_pred)^2
r2_score # 0.8752067 -> 1 수렴정도
# 정확도: 약 87%

# (5) 예측치와 관측치 시각화
plot(y_true,type='o',ann=F,col='blue')
par(new=T)
plot(y_pred,type='o',axes=F,ann=F,col='red')

legend('topleft',legend=c('관측치','예측치'),col=c('blue','red'),lty=1) # 범례추가

# 정반대의 경향을 보이면 해당 시점에서 예측력이 떨어지는 것으로 간주
# 원인 확인: 모델의 일반화가 낮기 떄문