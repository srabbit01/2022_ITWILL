#################################
## <제16장 연습문제>
################################# 

# 01. 타이타닉(titanic) 데이터 셋을 대상으로 7:3 비율로 학습데이터와 검정데이터로 각각 
# 샘플링한 후 각 단계별로 분류분석을 수행하시오.

getwd()
setwd("E:/03. R/data")
titanic = read.csv("titanic3.csv")
str(titanic) 
#titanic3 변수 설명 

#'data.frame': 1309 obs. of 14 variables:
#pclass : 1, 2, 3등석 정보를 각각 1, 2, 3으로 저장
#survived : 생존 여부. survived(생존=1), dead(사망=0)
#name : 이름(제외)
#sex : 성별. female(여성), male(남성)
#age : 나이
#sibsp : 함께 탑승한 형제 또는 배우자의 수
#parch : 함께 탑승한 부모 또는 자녀의 수
#ticket : 티켓 번호(제외)
#fare : 티켓 요금
#cabin : 선실 번호(제외)
#embarked : 탑승한 곳(제외) C(Cherbourg), Q(Queenstown), S(Southampton)
#boat     : (제외)Factor w/ 28 levels "","1","10","11",..: 13 4 1 1 1 14 3 1 28 1 ...
#body     : (제외)int  NA NA NA 135 NA NA NA NA NA 22 ...
#home.dest: (제외)


# 생존여부 factor형 변환 : 더미변수 생성 
titanic$survived <- factor(titanic$survived, levels = c(0, 1))

# 생존여부 빈도수 
table(titanic$survived)
#  0   1  -> 0:사망, 1:생존  
#809 500

# 생존여부 비율 
prop.table(table(titanic$survived))
#       0        1 
#0.618029 0.381971



# 단계1 : 변수7개 제외 서브셋 만들기 : name, ticket, cabin, embarked, boat, body, home.dest  
titanic <- subset(titanic,select=-c(name, ticket, cabin, embarked, boat, body, home.dest ))
str(titanic)

# 단계2 : 80% : 20% 데이터셋 분할하기 
# - 훈련셋 : titanic_train, 검정셋 : titanic_test    
samp=sample(x=nrow(titanic),0.8*nrow(titanic))
train=titanic[samp,]
test=titanic[-samp,]
  
# 단계3 : 분류모델 생성 : 종속변수 survived 변수, 독립변수 : 나머지 변수  
model <- rpart(survived~.,data=train)
model
  
# 단계4 : 의사결정트리 시각화 : 중요변수 2~3개를 기준으로 생존확률이 높은 경우 설명하기   
fancyRpartPlot(model)
# [해석] 성별이 여자이고, 23세 이하, 선실 2.5등석 이하인 경우 생존확률 높음
  
# 단계5 : 모델 검정/평가(0:Negative, 1:Positive) : 분류정확도, 정확률, 제현율, F1 score
pred=predict(model,newdata=test,type='class')
real=test$survived
tab=table(real,pred)

accuracy <-sum(diag(tab))/sum(tab)
accuracy # 0.8807339

precision <- tab[2,2]/sum(tab[,2]) # TP / (TP+FP): 예측치Yes->관측치Yes
precision # 0.5714286

recall <- tab[2,2]/sum(tab[2,]) # TP/ (TP+FN): 관측치Yes->예측치Yes
recall # 0.75

f1_score <-(recall*precision)*2/(precision+recall)
f1_score  # 0.6486486 
  
# 84 vs 12 -> f_score 이용

# 02. weather 데이터를 이용하여 다음과 같은 단계별로 의사결정 트리 방식으로 분류분석을 수행하시오. 

# 조건1) rpart() 함수 이용 분류모델 생성 
# 조건2) y변수 : RainTomorrow, x변수 : 1, 6, 8, 14번 변수 제외한 나머지 변수로 분류모델 생성 
# 조건3) 모델의 시각화를 통해서 y에 가장 영향을 미치는 x변수 확인 
# 조건4) 비가 올 확률이 50% 이상이면 ‘Yes Rain’, 50% 미만이면 ‘No Rain’으로 범주화

# 단계1 : 데이터 가져오기
library(rpart) # model 생성 
library(rpart.plot) # 분류트리 시각화 


weather = read.csv("weather.csv", header=TRUE) 
str(weather)
# 'data.frame':	366 obs. of  15 variables:

# chr형 변수 제외 : y = RainTomorrow
weather <- weather[-c(1, 6, 8, 14)]
str(weather)

# y변수 -> 더미변수 변환 
weather$RainTomorrow <- as.factor(weather$RainTomorrow)
table(weather$RainTomorrow)

# 단계2 : 데이터 샘플링: 70% 30%
samp=sample(x=nrow(weather),0.7*nrow(weather))
train=weather[samp,]
test=weather[-samp,]

# 단계3 : 분류모델 생성
model=rpart(RainTomorrow ~.,data=weather)

# 단계4 : 분류모델 시각화 - 중요변수 확인 
rpart.plot(model)
# [해석] 안개가 많고, 기압이 낮으면 비올 확률 높음

# 단계5 : 예측 확률 범주화('Yes Rain', 'No Rain')
pred=predict(model,newdata=test,type='prob')
pred
pred=ifelse(pred[,2]>=0.5,'Yes Rain','No Rain')

# 단계6 : 혼돈 matrix 생성 및 분류 정확도 구하기
tab=table(pred)
tab
# No Rain Yes Rain 
#      86       24

# 03. Boston 데이터셋을 대상으로 단계별로 회귀트리 모델을 생성하시오. 

# 단계1 : 데이터셋 가져오기 
library(MASS)
data("Boston")
str(Boston)
#$ crim   : 1인당 범죄율 num  0.00632 0.02731 0.02729 0.03237 0.06905 ...
#$ zn     : 25,000 평방피트 초과 거주지역 비율 num  18 0 0 0 0 0 12.5 12.5 12.5 12.5 ...
#$ indus  : 비소매상업지역 점유 토지 비율 num  2.31 7.07 7.07 2.18 2.18 2.18 7.87 7.87 7.87 7.87 ...
#$ chas   : 찰스강 더미변수(1: 강의 경계)int  0 0 0 0 0 0 0 0 0 0 ...
#$ nox    : 일산화질소 num  0.538 0.469 0.469 0.458 0.458 0.458 0.524 0.524 0.524 0.524 ...
#$ rm     : 평균 방의 개수 num  6.58 6.42 7.18 7 7.15 ...
#$ age    : 고택 비율 num  65.2 78.9 61.1 45.8 54.2 58.7 66.6 96.1 100 85.9 ...
#$ dis    : 직업센터 접근성 지수 num  4.09 4.97 4.97 6.06 6.06 ...
#$ rad    : 도로 접근성 지수 int  1 2 2 3 3 3 5 5 5 5 ...
#$ tax    : 재산세율 num  296 242 242 222 222 222 311 311 311 311 ...
#$ ptratio: 학생/교사 비율 num  15.3 17.8 17.8 18.7 18.7 18.7 15.2 15.2 15.2 15.2 ...
#$ black  : 흑인 비율 num  397 397 393 395 397 ...
#$ lstat  : 하위계층 비율 num  4.98 9.14 4.03 2.94 5.33 ...
#$ medv   : 주택가격(단위 : 1,000 달러) num  24 21.6 34.7 33.4 36.2 28.7 22.9 27.1 16.5 18.9 ...


# 단계2 : 분류모델 생성 : y변수 : medv, x변수 : 나머지 13개 변수
model=rpart(medv~.,data=Boston)

# 단계3 : 분류모델 시각화 - 중요변수 확인 
rpart.plot(model)

# 단계4 : 3겹 교차검정을 수행하여 모델 평가 
library(cvTools)
library(rpart)

# 1) K겹 교차검정을 위한 샘플링 
cross=cvFolds(n=nrow(Boston),K=3)

# 2) K겹 교차검정 
K=1:3
r2_score=c() # 결정계수 누적

for(i in K){ # 3회 반복
  idx <- cross$subsets[cross$which==i, 1] # 행번호 추출  
  test <- Boston[idx, ] # 평가셋 d1 -> d2 -> d3
  train <- Boston[-idx, ] # 훈련셋 (d2,d3) -> (d1,d3) -> (d2,d3)
  # 모델 생성 
  model <- rpart(medv ~ ., data = train) # 2개 셋
  # 예측치 
  y_pred <- predict(model, test) # 1개 셋
  y_true <- test$medv
  # 분류정확도 
  r2_score=c(r2_score,cor(y_true,y_pred)^2) # 결정계수 누적
}

# 3) 교차검정 평가
cat('R2 score 산술평균 =',mean(r2_score))
# R2 score 산술평균 = 0.7491104













