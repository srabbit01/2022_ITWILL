# chap15_Logistic Regression


# 1. 로짓 변환 : y값을 0 ~ 1로 조정하는 과정 

# 단계1 : 오즈비(Odds ratio) : [실패(0)에 대한] 성공(1) 비율(0:fail, 1:success)
# ex) Odds of ten to one -> 10대 1의 배당률(성공 비율 1/10) 

p = 0.5 # success
1 - p # fail
odds_ratio = p / (1-p) 

p = 1 # 성공 100% 
odds_ratio = p / (1-p)  

p=0 # 성공 0%
odds_ratio = p / (1-p)  

# 단계2 : 로짓변환 : 오즈비에 log 적용 
p = 0.5 # 성공 50%
odds_ratio = p / (1-p) 
odds_ratio
logit1 = log(odds_ratio) 

p = 1 # 성공 100% 
odds_ratio = p / (1-p)  
logit2 = log(odds_ratio)

p=0 # 성공 0%
odds_ratio = p / (1-p)  
logit3 = log(odds_ratio)

# 로짓변환 범위: -Inf ~ + Inf: p: 0.5 -> 0

# 단계3 : 시그모이드 함수 
# sigmoid_function = (1 / (1 + exp(-로짓값)))
1 / (1 + exp(-(logit1))) # logit=0 -> 0.5
1 / (1 + exp(-(logit2))) # logit=+Inf -> 1
1 / (1 + exp(-(logit3))) # logit=-Inf -> 0


# 로지스틱 회귀분석(Logistic Regression) 모델 

# 단계1. 데이터 가져오기 
getwd()
setwd("E:/03. R/data")
weather = read.csv("weather.csv")
dim(weather)  # 366  15
head(weather)
str(weather)

# chr 칼럼, Date, RainToday 칼럼 제거 
weather_df <- weather[, c(-1, -6, -8, -14)]
str(weather_df)

# RainTomorrow 칼럼 -> 로지스틱 회귀분석 결과(0,1)에 맞게 더미변수 생성      
# weather_df$RainTomorrow[weather_df$RainTomorrow=='Yes'] <- 1
# weather_df$RainTomorrow[weather_df$RainTomorrow=='No'] <- 0
# weather_df$RainTomorrow <- as.numeric(weather_df$RainTomorrow)
weather_df$RainTomorrow=as.factor(weather_df$RainTomorrow)
head(weather_df)
str(weather_df)

# 결측치 제거
weather_df=na.omit(weather_df)

#  단계2.  데이터 셈플링
idx <- sample(nrow(weather_df), nrow(weather_df)*0.7)
train <- weather_df[idx, ]
test <- weather_df[-idx, ]

dim(train) # [1] 252  11
dim(test) # 109  11

#  단계3.  로지스틱  회귀모델 생성 : 학습데이터 
weater_model <- glm(RainTomorrow ~ ., data = train, family = 'binomial')
weater_model 
summary(weater_model) # Z검정 통계량(유의성)과 설명력(결정계수) 제공하지 X


# 단계4. 로지스틱  회귀모델 예측치 생성 : 검정데이터 
# newdata=test : 새로운 데이터 셋, type="response" : 0~1 확률값으로 예측 
pred <- predict(weater_model, newdata=test, type="response")  

pred
range(pred) # [1] 0.001142965 0.980328894

# 예측치
# cutoff = 0.5
y_pred <- ifelse(pred > 0.5, 1, 0) # ifelse(조건식,TRUE결과,FALSE결과)

#관측치(정답)
y_true <- test$RainTomorrow


# 단계5. model 평가 : 혼동 행렬 
tab <- table(y_true, y_pred)

tab
#                      y_pred
# y_true          0(N)   1(P)
#       No(N)   89(TN)  4(FP)
#      Yes(P)    7(FN)  9(TP)

# 분류기 평가지표
# 1) 분류정확도(Accuracy)=(TP+TN)/(TP+TN+FP+FN)
acc=(89+9)/sum(tab)
acc # 0.8990826

# 2) 오분류율=(FP+FN)/(TP+TN+FP+FN)
inacc=(7+4)/sum(tab)
inacc # 0.1009174

# 3) 정밀도(Precision)=(TP)/(TP+FP)
pre=9/(9+4)
pre # 0.6923077

# 4) 재현율(Recall)=민감도=(TP)/(TP+FN) # 실제 데이터 대상, 실제 참일때 예측 참인 비율
Re=9/(9+7)
Re # 0.5625

# 5) 특이도=(TN)/(TN+FP) # 실제 거짓인 경우 예측 거짓인 비율
Sp=89/(89+4)
Sp # 0.9569892

# 6) F-측청치(F measure): 비율 불균형(조화평균)
f1=(pre*Re)/(pre+Re)
f1

# 단계6. 모델 유의성(적합도) 검정 
install.packages("ResourceSelection")
library(ResourceSelection)

names(weater_model)

weater_model$y # y변수 값 
weater_model$fitted.values # 예측치

hoslem.test(weater_model$y, weater_model$fitted.values)
# p-value = 0.8296 > 0.05: 차이가 있음 = 가설 채택 (통계적으로 유의)


### ROC Curve를 이용한 모형평가(분류정확도)  ####
# Receiver Operating Characteristic

install.packages("ROCR")
library(ROCR)

# ROCR 패키지 제공 함수 : prediction() -> performance
pr <- prediction(pred,test$RainTomorrow)
prf <- performance(pr, measure = "tpr", x.measure = "fpr")
prf
plot(prf)

?performance
AUC=performance(pr,measure = "auc")
plot(AUC)
names(AUC)
AUC$y.values


#########################
## 다항 로지스틱 회귀분석
#########################

install.packages('nnet')
library(nnet)

unique(iris$Species) # setosa     versicolor virginica 

# split 70:30
idx=sample(x=nrow(iris),size=nrow(iris)*0.7)

train_set=iris[idx,]
test_set=iris[-idx,]

# 활성함수
## (1) 이항 분류: sigmoid 함수
## (2) 다항 분류: softmax 함수

# 1. 모델 생성
model=multinom(Species~.,data=train_set)
model

names(model)
model$fitted.values
sum(1.796824e-18+3.870630e-07+9.999996e-01) # 확률의 합 = 1

# 2. 예측치: 각 범주 당 확률 혹은 class로 예측 가능
pred=predict(model,test_set,type='probs')
pred

pred2=predict(model,test_set,type='class') # y 범주 출력(확률이 가장 높은 범주)
pred2

# 3. 모델 평가
y_true=test_set$Species # class
y_true

table(y_true,pred2)
#              pred2
# y_true       setosa versicolor virginica
# setosa         14          0         0
# versicolor      0         14         0
# virginica       0          0        17
# 100% 예측했음을 알 수 있음

summary(model)

library(ResourceSelection)

names(model)

model$y # y변수 값
model$fitted.values # 예측치

z = summary(model)$coefficients / summary(model)$standard.errors
(1 - pnorm(abs(z), 0, 1)) * 2

library(MASS)
install.packages("AER")
library(AER)
coeftest(model)

anova(model, test="Chisq")

######################################
# 3. Logistic Regression example
######################################

# 대출 수락 or 거절 prediction
Data = read.csv('UniversalBank.csv')
str(Data)
#$ ID(x)             : int  1 2 3 4 5 6 7 8 9 10 ...
#$ Age               : 고객 나이
#$ Experience        : 은행 거래 가입기간
#$ Income            : 수입
#$ ZIP.Code(x)       : int  91107 90089 94720 94112 91330 ...
#$ Family            : 구성원
#$ CCAvg             : 카드지출 평균액
#$ Education         : 교육수준
#$ Mortgage          : 모기지-주택담보대출 
#$ Personal.Loan(y)  : 수락 or 거절 
#$ Securities.Account: 비밀계좌
#$ CD.Account        : CD계좌 
#$ Online            : 인터넷뱅킹
#$ CreditCard        : 신용카드 사용여부

str(Data)

unique(Data$Education) # int: 1 2 3 -> 더미변수 변환 (O)
unique(Data$Personal.Loan) # int: 0 1 -> 더미변수 변환 (X)

# 불필요한 변수 제거: 구분(id), 날짜(date), name(문자열), 우편변호(postcode)

# 더미변수 생성 : factor형 변환 
Data$Education <- as.factor(Data$Education)
Data$Personal.Loan <- as.factor(Data$Personal.Loan)
Data$Securities.Account <- as.factor(Data$Securities.Account)
Data$CD.Account <- as.factor(Data$CD.Account) # 0 1
Data$Online <- as.factor(Data$Online) # 0 1
Data$CreditCard <- as.factor(Data$CreditCard) # 0 1

# random sample 비복원 추출
idx <- sample(1:nrow(Data), 0.7*nrow(Data), replace = FALSE)
# 전체 Data를 7:3으로 구분
train_bank <- Data[idx, ]
test_bank <- Data[-idx, ]


#formula = y(종속) ~ x(독립변수)
formula <- Personal.Loan ~.
Reg_Model <- glm(formula, data = train_bank, family = 'binomial')

summary(Reg_Model)

# 기여도가 낮은 변수(“Age”, “Mortgage”, “Experience” ) 제거 후 model 생성 
Reg_Model <- glm(formula, data = train_bank[c(-1,-2,-7)], family = 'binomial')
Reg_Model
summary(Reg_Model)

library(MASS)
stepAIC(Reg_Model,direction='both')
# direction=c('both','forward','backward')

# Train Set 데이터를 모델에 적용한 결과
Reg_Model$fitted.values
# histogram  생성
h <- hist(Reg_Model$fitted.values, main = "Regression_ Model Fitted Values", breaks = 10, col = "grey")
# 0 ~ 1에 치우친 것을 확인 #cutoff 위치 낮춤

names(h)
h$mids
# $ count: 각 계급의 빈도수
# $ mids: 각 계급의 중앙(위치)

# count된 결과값 표시
text(h$mids,h$counts, labels=h$counts, adj=c(0.5, -0.5))
# text(x축 위치, y축 위치, labels=출력값, adj=c(상하정렬,좌우정렬))
# adj=c(좌우,상하)

# cut-off 값 적용하여 검정데이터 예측 
pred <- predict(Reg_Model, newdata=test_bank[c(-1,-2,-7)], type="response")  # 검정데이터 예측치 

# cut-off = 0.5
pred_result_0.5 <- ifelse(pred >= 0.5, 1, 0)
# 혼동행렬 
Pred_Table_0.5 <- table(test_bank$Personal.Loan, pred_result_0.5)
Pred_Table_0.5
#    pred_result_0.5
#      0    1
# 0 4318  107
# 1  131  339
acc=(4318+339)/sum(Pred_Table_0.5)
acc # 0.951379

# cut-off = 0.3 -> 하향조정
pred_result_0.3 <- ifelse(pred >= 0.3, 1, 0)
# 혼동행렬 
Pred_Table_0.3 <- table(test_bank$Personal.Loan, pred_result_0.3)
Pred_Table_0.3
pred_result_0.3
#      0    1
# 0 4311  114
# 1  130  340

acc2=(4311+340)/sum(Pred_Table_0.3)
acc2 # 0.9501532: 정확도 감소

# cut-off = 0.7 -> 상향조정
pred_result_0.7 <- ifelse(pred >= 0.7, 1, 0)
# 혼동행렬 
Pred_Table_0.7 <- table(test_bank$Personal.Loan, pred_result_0.7)
Pred_Table_0.7
# pred_result_0.7
#      0    1
# 0 4323  102
# 1  135  335

acc3=(4323+335)/sum(Pred_Table_0.7)
acc3 # 0.9515832: 정확도 조금 증가


###################################
# 최적의 cutoff값 정하기
###################################
# cut off=0.5 타당성 테스트 
cutOff_test <- function(prop, realdata){ # (예측확률, 실제 정답)
  cutOff_re <- c() # cutoff 누적 
  acc_re <- c() # 분류정확도 누적     
  cutOff <- seq(0.3, 0.7, by = 0.1) # 테스트 cutoff(0.3~0.7 : 5개) 
  
  for( cut in cutOff ){ # 5회 반복 
    cutOff_re <- c(cutOff_re, cut ) 
    pred <- ifelse(prop >= cut, 1, 0) 
    conf <- table(pred, realdata) # 혼돈행렬 생성      
    cat('cutoff=',cut,'\n') # 현재 cutoff
    print(conf) # 혼돈행렬 출력
    
    acc <- sum(diag(conf))/sum(conf) # 분류정확도 
    acc_re <- c(acc_re, acc) # 분류정확도 누적 
  }
  df <- data.frame(cutOff_re, acc_re) # df 생성 
  print(df) #  전체 : cutOff와 accuracy
  print(df[df$acc_re == max(df$acc_re), ]) # 가장 높은 cutOff와 accuracy
}
# 가장 최적의 cutoff를 데이터프레임 형식으로 제공

# 함수 호출

cutOff_test(pred,test_bank$Personal.Loan)
