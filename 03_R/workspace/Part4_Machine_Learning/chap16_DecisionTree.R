# chap16_DecisionTree


install.packages('rpart') # rpart() : 분류모델 생성 
install.packages("rpart.plot") # prp(), rpart.plot() : rpart 시각화
install.packages('rattle') # fancyRpartPlot() : node 번호 시각화 

library(rpart) 
library(rpart.plot) 
library(rattle) 

####################################
# 암 진단 분류 분석 : 이항분류
####################################
# "wdbc_data.csv" : 유방암 진단결과 데이터 셋 분류

# 1. 데이터셋 가져오기 

getwd()
setwd("E:/03. R/data")
wdbc <- read.csv('wdbc_data.csv')
str(wdbc)

# 2. 데이터 탐색 및 전처리 
wdbc_df <- wdbc[-1] # id 칼럼 제외
head(wdbc_df)
wdbc_df$diagnosis # 진단결과 : B -> '양성', M -> '악성'
table(wdbc_df$diagnosis)
#   B   M 
# 357 212

# 목표변수(y변수)를 factor형 변환 : 0, 1 dummy 변수  
wdbc_df$diagnosis <- as.factor(wdbc$diagnosis) # 0, 1
wdbc_df$diagnosis[1:10] # Levels: B M -> 0(False), 1(True)

# as.factor() vs factor()
# as.factor(): 문자형/숫자형->요인형
# factor(): 문자형/숫자형->요인형+Levels변경

# 3. 훈련데이터와 검정데이터 생성 : 7 : 3 비율 
set.seed(415)
idx = sample(nrow(wdbc_df), 0.7*nrow(wdbc_df))
wdbc_train = wdbc_df[idx, ] # 훈련 데이터 
wdbc_test = wdbc_df[-idx, ] # 검정 데이터 


# 4. rpart 분류모델 생성 
model_wdbc <- rpart(diagnosis ~ ., data = wdbc_train)
model_wdbc # - 가장 중요한 x변수? points_mean

# tree 시각화 
prp(model_wdbc)
rpart.plot(model_wdbc)
fancyRpartPlot(model_wdbc)

# 5. 모델 평가
y_pred=predict(model_wdbc,wdbc_test,type='class') # 예측치
y_pred

y_true=wdbc_test$diagnosis # 관측치(정답)

# 혼동행렬
tab=table(y_true,y_pred)
#       y_pred
# y_true  B  M
#      B 92  3 = 95
#      M 13 63 = 76
tab

# 예측치 출력 (확률 형태)
y_pred2=predict(model_wdbc,wdbc_test,type='prob')
y_pred2
dim(y_pred2) # [1] 171   2[B,M]
# 예측확률 -> 예측class 변환
y_pred2=ifelse(y_pred2[,1]>=0.5,'B','M')
table(y_true,y_pred2)

# 정확도 구하기
acc=sum(diag(tab))/sum(tab)
cat('accuracy=',acc) # 0.9064327

# B의 정확도
92/95 # 0.9684211
# M의 정확도
64/76 # 0.8421053

################################
## rpart 분류모델 결과 해석 방법
################################
#  1) root 398 136 B (0.65829146 0.34170854) -> 양성(B): 66%, 악성(M): 34%
wdbc_train$diagnosis # 훈련 데이터 종속변수(Y)
tab=table(wdbc_train$diagnosis) # 262 136
prop.table(tab) # 0.6582915 0.3417085
# 차트 내용: 범주(많은 비율) > 비율(M=1), 전체 비율

#    2) points_mean< 0.04923 255  10 B (0.96078431 0.03921569) *
# LeftNode: 분류기준, 분류기준해당(관측치), 다른범주, 주요범주(분류비율), 단노드
255-10 # 245 = B의 빈도수

#    3) points_mean>=0.04923 143  17 M (0.11888112 0.88111888)
# RightNode: 분류기준, 분류기준해당(관측치), 다른범주, 주요범주(분류비율)
255+143 # 398
143-17 # 126 = M의 빈도수, 17 = B의 빈도수

left_node=subset(wdbc_train,points_mean<0.04923)
dim(left_node) # 255  31 = 64%
tab=table(left_node$diagnosis) # B 245 M 10
prop.table(tab) # B 96% M 4%

right_node=subset(wdbc_train,points_mean>=0.04923)
dim(right_node) # 143  31 = 36%

#      6) concavity_worst< 0.2269 12   2 B (0.83333333 0.16666667) *
#      7) concavity_worst>=0.2269 131   7 M (0.05343511 0.94656489)  
#        14) area_worst< 710.2 8   3 B (0.62500000 0.37500000) *
#        15) area_worst>=710.2 123   2 M (0.01626016 0.98373984) *

# [정리] 중요변수 3개의 수치가 낮을 수록 양성 비율이 높아짐, 수치가 클 수록 악성 비율이 높아짐


################################
# iris 데이터셋 : 다항분류 
################################
# 단계1. 실습데이터 생성 
data(iris)
set.seed(415)
idx = sample(nrow(iris), 0.7*nrow(iris))
train = iris[idx, ]
test = iris[-idx, ]
dim(train) # 105 5
dim(test) # 45  5

table(train$Species)

# 단계2. 분류모델 생성 
# rpart(y변수 ~ x변수, data)
model = rpart(Species~., data=train) # iris의 꽃의 종류(Species) 분류 
model

# 분류모델 시각화 - rpart.plot 패키지 제공 
prp(model) # 간단한 시각화   
rpart.plot(model) # rpart 모델 tree 출력
fancyRpartPlot(model) # node 번호 출력(rattle 패키지 제공)


# 단계3. 분류모델 평가  
pred1 <- predict(model, test) # 비율 예측 
dim(pred1) # [1] 45  3(setosa versicolor virginica)
#비율 -> class 예측
pred1=ifelse(pred1[,1]>0.5,'setosa',
       ifelse(pred1[,2]>0.5,'versicolor','virginica'))
table(pred1)

pred2 <- predict(model, test, type="class") # 분류 예측 

y_true <- test$cty

# 1) 분류모델로 분류된 y변수 보기 
table(pred2)

# 2) 분류모델 성능 평가 
tab=table(pred2, test$Species)

# 정확도
sum(diag(tab))/length(pred2) # 0.9111111 

###################################
### 회귀트리 
###################################
# 독립변수(설명변수) : 범주형 또는 연속형 변수  
# 종속변수(반응변수) : 연속형 변수

library(ggplot2) # dataset 사용 
data(mpg)
str(mpg) 

# 단계1 : 학습데이터와 검정데이터 샘플링
idx <- sample(nrow(mpg), nrow(mpg)*0.7)
train <- mpg[idx, ]
test <- mpg[-idx, ]
dim(train) # 163 11


# 단계2 : 학습데이터 이용 분류모델 생성 
model <- rpart(cty ~ displ + cyl + year, data = train)
model # 중요변수 : displ
range(train$cty) # 9 35 : 연속형 

# 단계3 : 검정데이터 이용 예측치 생성 및 평가 
y_pred <- predict(model, test) # 항등함수(type 생략)
y_pred

y_true=test$cty

# 평균제곱오차 이용
MSE=mean((y_true - y_pred)^2)
MSE # 3.387998

# 결정계수(R^2)
cor(y_true, y_pred)^2 # 0.797021


# 단계4 : 분류분석 결과 시각화
prp(model)
rpart.plot(model) 
fancyRpartPlot(model)

#  13 14  17  20  24 -> 분류조건에 의해 분류된 값의 평균
# 29% 9% 28% 24% 10% 해당 분류조건에 의해 분류된 비율

# 24(9%) 관련 서프셋 & 평균 예시
re=subset(train,displ<2.6&displ<2)

dim(re) # 16 11

re$cty
mean(re$cty) # 결과 아래의 것은 각 값의 평균(대푯값)

# 색상이 진할 수록 종속변수 숫자가 커짐

################################
### 교차검정 
################################
# 객관적으로 모델을 평가하는 방법

#install.packages('cvTools')
library(cvTools)

# 단계1 : # K겹 교차검정을 위한 샘플링 
cross <- cvFolds(nrow(iris), K=5)
cross # Fold(dataset 구분)   Index(행번호): 2개의 컬럼 생성
# R: 반복횟수 (*반복횟수개의 데이터개수 생성)
# type: (기본: random)

# Fold(5등분 각 세트)   Index(행번호=위치)

str(cross) # List of 5

# $ subsets: int [1:150, 1] 60 59 53 50 65 121 91 126 20 57 ... # 인덱스 정보
# $ which  : int [1:150] 1 2 3 4 5 1 2 3 4 5 .. # 세트 정도
# 두 키를 가지고 train test 생성

# 5개 데이터셋 구성 : which 이용 색인으로 사용   
dataset1 <- cross$subsets[cross$which==1, 1]
dataset2 <- cross$subsets[cross$which==2, 1]
dataset3 <- cross$subsets[cross$which==3, 1]
dataset4 <- cross$subsets[cross$which==4, 1]
dataset5 <- cross$subsets[cross$which==5, 1]
length(set1); length(set5)

# 단계2 : K겹 교차검정 
K = 1:5 # 5겹
ACC <- c() # 분류정확도 누적

for(i in K){ # 5회 반복
  idx <- cross$subsets[cross$which==i, 1] # 행번호 추출  
  test <- iris[idx, ] # 평가셋 (d1)
  train <- iris[-idx, ] # 훈련셋 (d2~d4)
  # 모델 생성 
  model <- rpart(Species ~ ., data = train)
  # 예측치 
  y_pred <- predict(model, test, type='class')  
  t <- table(test$Species, y_pred) # 혼돈행렬
  # 분류정확도 
  ACC <- c(ACC,  (sum(diag(t))) / sum(t) ) # 분류정확도 누적
}

# 단계3 : 교차검정 평가 
cat('분류정확도 산술평균 =', mean(ACC))


#####################################
### Entropy vs GINI : 불확실성 척도 
#####################################
# 두 확률변수 간 불확실성을 나타내는 수치(척도)

# p1 : 앞면, p2 : 뒷면 - 불확실성이 높은 경우 
p1 = 0.5; p2 = 0.5

# Entropy = -sum(p * log(p))
e1 <- -(p1 * log2(p1)) + -(p2 * log2(p2))
e1 # 1 -> 엔트로피 가장 큰 경우 

# GINI = p1 * (1-p1) + p2 * (1-p2)
gini1 <- p1 * (1 - p1) + p2 * (1 - p2)
gini1 # 0.5 -> gini 계수 가장 큰 경우 


# p1 : 앞면, p2 : 뒷면 - 불확실성이 낮은 경우 
p1 = 0.9; p2 = 0.1

e2 <- -(p1 * log2(p1)) + -(p2 * log2(p2))
e2 # 0.4689956

gini2 <- p1 * (1 - p1) + p2 * (1 - p2)
gini2 # 0.18


###################################
### 분류분석 적용 예(ppt.18)
###################################
# - 먹구름(x1)과 돌풍(x2)에 대한 비 유무 예측  

#먹구름(x1) 돌풍(x2)  비(y) 
#   1        1         yes
#   1        1         yes
#   1        0         no
#   0        1         no
#   0        1         no


# 단계1 : 전체 엔트로피(Entropy Root)
hit_prop = 2/5 # yes 확률 
no_hit_prop = 3/5 # no 확률 
# Entropy 수식 
entropyRoot = - (hit_prop*log2(hit_prop) + no_hit_prop*log2(no_hit_prop))
entropyRoot # 0.9709506


# 단계2 : 각 x변수 엔트로피 
# 1) x1 변수(YYN/NN) 엔트로피 
YYN = -(2/3*log2(2/3)) + -(1/3*log2(1/3)) # x1=1 entropy  
NN = -(0) + -(2/2*log2(2/2)) # x1=0  entropy 
x1_Entropy = (3/5)*YYN + (2/5)*NN # 가중치 * entropy 적용 
x1_Entropy # 0.5509775


# 2) x2 변수(YYNN/N) 엔트로피 
YYNN = -(2/4*log2(2/4)) + -(2/4*log2(2/4)) # x2=1 entropy   
N = -(0) + -(1/1*log2(1/1))# x2=0 entropy
x2_Entropy = (4/5)*YYNN + (1/5)*N 
x2_Entropy # 0.8


# 단게3 : 정보이득(Information gain) 
x1_infoGain <- entropyRoot - x1_Entropy  # 0.4199731
x2_infoGain <- entropyRoot - x2_Entropy  # 0.1709506

# 해설 : 정보이득이 높은 x1 변수를 중요변수로 선정 