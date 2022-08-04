# chap17_RandomForest

##################################################
#randomForest
##################################################
# 결정트리(Decision tree)에서 파생된 모델 
# 랜덤포레스트는 앙상블 학습기법을 사용한 모델
# 앙상블 학습 : 새로운 데이터에 대해서 여러 개의 Tree로 학습한 다음, 
# 학습 결과들을 종합해서 예측하는 모델(PPT 참고)
# DT보다 성능 향상, 과적합 문제를 해결


install.packages('randomForest')
library(randomForest) # randomForest()함수 제공 

data(iris)

# 1. 랜덤 포레스트 모델 생성 
# 형식) randomForest(y ~ x, data, ntree=500, mtry)
# ntree: 생성할 나무 개수 (기본:500개) -> 보통 400~500개 정도가 적절
# mtry: 설명변수(X)의 개수 (분류트리: sqrt(p), 회귀틀: p/3) (과적합,다공선성 등 해결)
# na.action: 결측치 처리 방법 (na.omit: 결측치 모두 제거)

# 분류모델에서 독립변수(X) 개수 구하기
p=4
mtry=sqrt(p)
mtry # 분류모델이기 때문에 2개가 적절

# train/test split 과정 없음
model = randomForest(Species~., data=iris,
                     ntree=500, mtry=2,  na.action=na.omit)  
model
# Number of trees: 500 = 생성된 나무 개수
# No. of variables tried at each split: 2 = 독립변수(X) 개수
# 모델 평가
# OOB estimate of  error rate: 4% (오분류율=오차) = 96% 정분류율
143/150 # 0.9533333 정분류율
# Confusion matrix:
#            setosa versicolor virginica class.error
# setosa         50          0         0        0.00 -> 각 범주 별 오분류율
# versicolor      0         47         3        0.06
# virginica       0          3        47        0.06

# 2. model 정보 확인 
names(model) # 19컬럼 제공 
# "predicted": 모델의 예측치
# "err.rate": 모델의 오차율
# "confusion": 혼돈행렬
# "importance": 중요변수 정보
# "y": 모델의 관측치

con=model$confusion
con

# 정분류율 계산
acc=sum(diag(con))/sum(con)
acc # 0.9592326

# 오분류율 계산
odd=1-acc
odd # 0.04076739
model$err.rate

# 중요변수 정보
model$importance
#              MeanDecreaseGini
# Sepal.Length         9.343739
# Sepal.Width          2.448793
# Petal.Length        43.208428
# Petal.Width         44.290290

# 3. 중요 변수 생성  
model2 = randomForest(Species ~ ., data=iris, 
                      ntree=500, mtry=2, 
                      importance = T,
                      na.action=na.omit )
# importance: 중요변수에 대한 상세 정보 제공

model2 

# importance(model2) = model2$importance
importance(model2)
model2$importance

# MeanDecreaseAccuracy: 분류정확도 개선의 공헌도
# MeanDecreaseGini: 노드 불순도(불확실성) 개선의 공헌도
#               MeanDecreaseAccuracy MeanDecreaseGini
# Petal.Length          0.290409060        41.543878
# Petal.Width           0.310337063        45.232241

varImpPlot(model2) # 중요변수 공헌도(지니계수)

# 정확도가 다소 높음

predict(model,ir)

################################
## 회귀트리(y변수 : 비율척도)
################################
library(MASS)
data("Boston")
str(Boston)
#crim : 도시 1인당 범죄율 
#zn : 25,000 평방피트를 초과하는 거주지역 비율
#indus : 비상업지역이 점유하고 있는 토지 비율  
#chas : 찰스강에 대한 더미변수(1:강의 경계 위치, 0:아닌 경우)
#nox : 10ppm 당 농축 일산화질소 
#rm : 주택 1가구당 평균 방의 개수 
#age : 1940년 이전에 건축된 소유주택 비율 
#dis : 5개 보스턴 직업센터까지의 접근성 지수  
#rad : 고속도로 접근성 지수 
#tax : 10,000 달러 당 재산세율 
#ptratio : 도시별 학생/교사 비율 
#black : 자치 도시별 흑인 비율 
#lstat : 하위계층 비율 
#medv(y) : 소유 주택가격 중앙값 (단위 : $1,000)

# 회귀모델에서 독립변수(X) 개수 구하기
p=13
mtry=p/3
mtry # 4.333333 = 4개 혹은 5개

boston_model <- randomForest(medv ~ ., data = Boston,
                             mtree = 500, mtry = 5,
                             importance = T,
                             na.action=na.omit)

boston_model2 <- randomForest(medv ~ ., data = Boston,
                             mtree = 500, mtry = 5,
                             importance = F,
                             na.action=na.omit)

boston_model
#                      Number of trees: 500
# No. of variables tried at each split: 5
# Mean of squared residuals: 9.674087 -> MSE(평균제곱오차): 0에 가까울 수록 오차 작음 
# % Var explained: 88.54 -> 분산의 설명력 작을 수록 좋음

mean(Boston$medv) # 22.53281

names(boston_model)
# $predicted: 예측치
# $y: 관측치
# $mse: 평균오차제곱

# 결정계수 평가: 객관적인 해석
y_pred=boston_model$predicted # 모델의 예측치
y_true=boston_model$y # 모델의 관측치(정답)

r2_score=cor(y_true,y_pred)^2
r2_score # 0.8905859 -> 80% 예측률
# 객관적인 해석이 쉬움

# 중요변수 확인: 평가 지표와 다름
importance(boston_model)
# IncMSE: 평균제곱오차의 공헌도
# IncNodePurity: 노드 불순도를 감안한 공헌도
#    %IncMSE IncNodePurity
# 15.380655     2234.1546
varImpPlot(boston_model)

importance(boston_model2)

################################
## 분류트리(y변수 : 범주형)
################################
titanic = read.csv(file.choose()) # titanic3.csv
str(titanic) 
# titanic3.csv 변수 설명
#'data.frame': 1309 obs. of 14 variables:
#1.pclass : 1, 2, 3등석 정보를 각각 1, 2, 3으로 저장
#2.survived : 생존 여부. survived(생존=1), dead(사망=0)
#3.name : 이름(제외)
#4.sex : 성별. female(여성), male(남성)
#5.age : 나이
#6.sibsp : 함께 탑승한 형제 또는 배우자의 수
#7.parch : 함께 탑승한 부모 또는 자녀의 수
#8.ticket : 티켓 번호(제외)
#9.fare : 티켓 요금
#10.cabin : 선실 번호(제외)
#11.embarked : 탑승한 곳(제외) C(Cherbourg), Q(Queenstown), S(Southampton)
#12.boat     : (제외)Factor w/ 28 levels "","1","10","11",..: 13 4 1 1 1 14 3 1 28 1 ...
#13.body     : (제외)int  NA NA NA 135 NA NA NA NA NA 22 ...
#14.home.dest: (제외)

# 종속변수(Y)
# 요인형/문자형: 분류모델 생성
# 숫자형: 회귀모델 생성

# 삭제 칼럼 : 3, 8, 10~14
df <- titanic[, -c(3, 8, 10:14)]
dim(df)  # 1309    7 

# 분류모델에서 mtry 구하기
p=7
mtry=sqrt(p)
mtry # 2.645751 = 2~3개 -> 각각 넣어보고 비교 판단

# 1) 분류모델 생성을 위한 종속변수(Y): 숫자형 -> 요인형(더미변수): 명목척도로 해석
# $ survived : int  1 1 0 0 0 1 1 0 1 0 ...
df$survived=as.factor(df$survived) # 형변환하지 않으면 회귀모델 생성

str(df)
# survived: Factor w/ 2 levels "0","1": 2 2 1 1 1 2 2 1 2 1 ...
# 주의: 분류모델 생성 시, 종속변수가 숫자형이면 요인형으로 변환

# 2) 랜덤포레스트 모델 생성
?randomForest
titanic_model=randomForest(survived~., data=df,
                    mtree=500,mtry=round(mtry), # 값 반올림
                    importance=T,na.action=na.omit)
titanic_model

# Confusion matrix: # 혼동행렬 확인
#     0   1 class.error
# 0 545  73   0.1181230 -> 사망
# 1 130 297   0.3044496 -> 생존

con=titanic_model$confusion
acc=sum(diag(con))/sum(con)
acc # 0.8054159

# 3) 중요변수 확인
importance(titanic_model)
varImpPlot(titanic_model)
# 성별(sex) > fare(티켓요금) > age > pclass(선실등급)
# MeanDecreaseAccuracy와 MeanDecreaseGini는 기준에 따라 중요 변수 다름
# 대부분 둘 다 높은 것 기준: 사용자 선택

plot(titanic_model)
