#################################
## <제14장 연습문제>
################################# 

# 01. mpg의 엔진크기(displ)가 고속도록주행마일(hwy)에 어떤 영향을 미치는가?   
library(ggplot2)
data(mpg) # 자동차연비 
str(mpg)

# <조건1> 단순선형회귀모델 생성 
x=mpg$mpg
y=mpg$displ
df=data.frame(x,y)
df

result=lm(y~x,data=df)
result
# y절편: 580.88, 기울기: -17.43  

# <조건2> 회귀선 시각화 
plot(df$x,df$y,ylim=c(0,500),xlim=c(0,40))
abline(result,col='red')

# <조건3> 회귀분석 결과 해석 : 모델 유의성검정, 설명력, x변수 유의성 검정  
summary(result)
# 1): p-value: 9.38e-10 < 0.05 -> 통계적 유의
# 2) Adjusted R-squared:  0.709 -> 예측력 80%
# 3) 기울기 p-value: 9.38e-10 *** < 0.05: 인과관계 강함 (영향력 높음)

# 02. ggplot2패키지에서 제공하는 diamonds 데이터 셋을 대상으로 
library(ggplot2)
data(diamonds)
str(diamonds)
# 다이아몬드의 무게(carat), 너비(table), 깊이(depth) 변수 중
# 다이아몬드의 가격(price)에 영향을 미치는 관계를 다중회귀 분석을 
# 이용하여 다음과 같은 단계로 확인하시오.

# 단계1 : 컷의 품질(cut) 칼럼에서 'Good','Very Good','Fair' 만으로 서브셋 만들기 
dia_df <- subset(diamonds,subset=c(diamonds$cut=='GOOD'|diamonds$cut=='Very Good'|diamonds$cut=='Fair'))
dia_df=subset(diamonds,subset=cut%in%c('Good','Very Good','Fair'))
dia_df

# 단계2 : 다이아몬드 가격 결정에 가장 큰 영향을 미치는 변수는?
result=lm(price~carat+table+depth,data=dia_df)
result

# 단계3 : 다중회귀 분석 결과를 정(+)과 부(-) 관계로 해설
summary(result)
# 1) p-value: < 2.2e-16 -> 통계적으로 유의
# 2) Adjusted R-squared:  0.8349 -> 예측력 83% 
# 3) 각 독립변수의 영향력
# carat        7623.372     29.110  261.88   <2e-16 ***: 양(+)의 영향력
# table         -88.292      5.996  -14.72   <2e-16 ***: 음(-)의 영향력
# depth        -210.294      7.539  -27.89   <2e-16 ***: 양(+)의 영향력


# 03. mpg 데이터셋을 대상으로 엔진크기(displ), 연식(year), 실린더수(cyl), 
# 구동방식(drv) 변수 중에서 도시주행마일(cty)에 영향을 미치는 관계를 
# 다중회귀분석을 이용하여 다음과 같은 단계로 확인하시오.

library(ggplot2)
data(mpg) # 자동차연비 
str(mpg)

# 단계1 : subset 만들기 : displ, year, cyl, drv, cty
df <- subset(mpg,select=c( displ, year, cyl, drv, cty))
df

# 단계2 : drv 변수 -> 더미변수 생성 
# (단, 구동 방식 3가지("f" "4" "r") 중에서 "r"을 base로 지정)
# Levels: 선정 기준 -> 숫자먼저, 알파벳순
# r: 후진, 4: 4륜
str(df)
df$drv=factor(df$drv,levels=c("r","f","4"))
str(df)

# 단계3 : 다중선형회귀모델 생성 & 회귀계수 확인  
result=lm(cty~.,data=df)

# 단계4 : 종속변수를 기준으로 각 독립변수의 관계 해설
summary(result)
# (Intercept) -107.16510   64.62262  -1.658   0.0986 .  
# displ         -0.81629    0.34298  -2.380   0.0181 *  : 음(-)의 영향력
# year           0.06748    0.03229   2.090   0.0377 *  : 양(+)의 영향력
# cyl           -1.27214    0.24671  -5.156 5.46e-07 ***: 음(-)의 영향력
# ------
# drvf           0.26106    0.64461   0.405   0.6859    : 영향력 없음
# drv4          -2.20940    0.52624  -4.198 3.85e-05 ***: 영향력 있음


# 04. product 데이터셋을 이용하여 다중회귀분석을 이용한 기계학습 모델을 
# 다음과 같은 단계로 만들고 평가하시오.

# <사용할 변수> y변수 : 제품_만족도, x변수 : 제품_적절성, 제품_친밀도

getwd()
setwd("E:/03. R/data")
product <- read.csv("product.csv", header=TRUE)
str(product)

#  단계1 : 훈련데이터(train), 평가데이터(test)를 7 : 3 비율로 샘플링
samp=sample(x=nrow(product),size=0.7*nrow(product))
train=product[samp,]
test=product[-samp,]

#  단계2 : 훈련데이터 이용 회귀모델 생성 
result=lm(제품_만족도~제품_적절성+제품_친밀도,data=train)
result
summary(result)

#  단계3 : 평가데이터 이용 모델 예측치 생성 
y_pre=predict(result,test)
y_real=test$제품_만족도

#  단계4 : 모델 평가 방법 :  MSE, 결정계수(R^2) 
Err=y_pre-y_real
Err
# 1) MSE
MSE=mean(Err^2)
MSE # 0.3098675

# 2) 결정계수(R^2)
R2=cor(y_pre,y_real)^2
R2 # 0.5247283: 예측력 약 52%로 비교적 낮음
