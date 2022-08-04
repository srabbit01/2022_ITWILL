# Red Tide_한수정

library(dplyr)
library(corrplot)
library(PerformanceAnalytics)
library(corrgram)
library(cvTools)
library(rpart)
library(rpart.plot)
library(rattle)
library(randomForest)
library(nnet)
library(AER) 
library(MASS)
library(caret)

# 1. 데이터 분석
# https://www.bigdata-environment.kr/user/data_market/detail.do?id=ff174540-53f9-11ec-8b4a-8de0170026ef

RedTide=read.csv('RedTide.csv') # 데이터 불러오기
RedTide=RedTide[c(2,3,4,7,8,15,16,17,18,19,20,21,11)] # 사용할 열(칼럼) 추출
names(RedTide)=c('Date','WTemp','Temp','Rain','Wind','Salt',
                 'DO','COD','PH','Turbidity','TN','TP','RedTide') # 열(칼럼) 이름 바꾸기
RedTide$Date=gsub("-","",RedTide$Date) # Date(날짜) '-' 특수문자 제거
RedTide$Date=as.numeric(RedTide$Date) # Date의 문자형 -> 숫자형 전환
str(RedTide)
# 'data.frame':	2068 obs. of  13 variables:
# $ Date     : num  20140101 20140102 20140103 20140104 20140105 ... # 측정 날짜
# $ WTemp    : num  7.7 7.7 7.7 7.8 7.7 7.6 7.6 7.5 7 6.8 ... # 수온
# $ Temp     : num  7.66 7.68 7.69 7.77 7.66 ... # 기온
# $ Rain     : num  0 0 0 0 0 0 0 4.2 0 0 ... # 강수량 (=0: 비가 오지 않음, >0: 비가 옴)
# $ Wind     : num  5.26 1.22 1.24 2.42 2.69 ... # 풍속
# $ Salt     : num  29.3 29.3 29.3 29.2 29.3 ... # 염분
# $ DO       : num  10.07 10 9.98 9.95 9.89 ... # 용존 산소량
# $ COD      : num  1.168 1.297 1.163 0.845 0.818 ... # 화학적 산소 요구량
# $ PH       : num  7.84 7.86 7.85 7.85 7.87 ... # 수소이온농도
# $ Turbidity: num  262.7 194.5 86.7 68.6 85.9 ... # 탁도
# $ TN       : num  0.29 0.29 0.29 0.29 0.29 ... # 총질소
# $ TP       : num  0.0262 0.0262 0.0262 0.0262 0.0281 ... # 총인
# $ RedTide  : int  0 0 0 0 0 0 0 0 0 0 ... # 적조 발생 여부 (0: 발생X, 1: 발생)

RT=subset(RedTide,subset=RedTide==1)
RT$Date # 보통 8~9월에 많이 발생
#  [1] 20140825 20140903 20140906 20140907 20140908 20140909
# [7] 20140910 20140911 20150810 20150811 20150812 20150813
# [13] 20150814 20150815 20150816 20150817 20150818 20150819
# [19] 20150820 20150821 20150822 20150831 20150901 20150902
# [25] 20150904 20150907 20150908 20150909 20150910 20150911
# [31] 20160820 20160821 20160822 20160823 20180802 20190827
# [37] 20190828
plot(RedTide$Date,RedTide$RedTide)

table(RedTide$RedTide)
#    0    1 
# 2031   37 
prop.table(table(RedTide$RedTide))
#          0          1 
# 0.98210832 0.01789168 

# 1) 결측치 확인 및 처리
sum(is.na(RedTide)) # 0 = 결측치 없음

# 2) 이상치 확인 및 제거
boxplot(RedTide[-1]) # Rain, Salt, Turbidity

# Rain 이상치 제거
boxplot(RedTide$Rain)$stats # 0~0.2
RedTide=subset(RedTide,0<=Rain & Rain<=0.2)
# Salt 이상치 제거
boxplot(RedTide$Salt)$stats # 28.78491~32.99567
RedTide=subset(RedTide,28.78491<=Salt & Salt<=32.99567)
# Turbidity 이상치 제거
boxplot(RedTide$Turbidity)$stats # 1~25.21942
RedTide=subset(RedTide,1<=Turbidity & Turbidity<=25)

# 차원확인
dim(RedTide) # [1] 1353   13 -> 약 700행 삭제

# 데이터 확인
plot(RedTide)

# 2. 상관분석
RedTide2=RedTide[-1] # Date 제
corr=cor(RedTide2)
corr
#                 WTemp        Temp         Rain        Wind        Salt            DO
# WTemp      1.00000000  0.99998944  0.019816550 -0.23461689 -0.23506338 -0.4052641633
# Temp       0.99998944  1.00000000  0.019797619 -0.23453756 -0.23515812 -0.4051372036
# Rain       0.01981655  0.01979762  1.000000000  0.07496405  0.01207697 -0.0082998948
# Wind      -0.23461689 -0.23453756  0.074964051  1.00000000  0.06747942  0.0598728959
# Salt      -0.23506338 -0.23515812  0.012076968  0.06747942  1.00000000  0.2445760612
# DO        -0.40526416 -0.40513720 -0.008299895  0.05987290  0.24457606  1.0000000000
# COD        0.33432530  0.33418235  0.012251692 -0.08711536 -0.28741758 -0.2742251117
# PH        -0.12537156 -0.12559070  0.026758737  0.04703072  0.28055175  0.2451105184
# Turbidity  0.17660030  0.17673580  0.058508837  0.04213868  0.07538034  0.0842605060
# TN         0.04687081  0.04691662  0.021441657  0.08551785 -0.16669651  0.0614530320
# TP         0.33342799  0.33345373  0.030603377 -0.08303982 -0.22322835 -0.2775321587
# RedTide    0.19973114  0.19958204  0.032469051 -0.02155956  0.02001962  0.0004668346
#                    COD          PH   Turbidity          TN          TP       RedTide
# WTemp      0.334325301 -0.12537156  0.17660030  0.04687081  0.33342799  0.1997311410
# Temp       0.334182353 -0.12559070  0.17673580  0.04691662  0.33345373  0.1995820441
# Rain       0.012251692  0.02675874  0.05850884  0.02144166  0.03060338  0.0324690508
# Wind      -0.087115362  0.04703072  0.04213868  0.08551785 -0.08303982 -0.0215595600
# Salt      -0.287417581  0.28055175  0.07538034 -0.16669651 -0.22322835  0.0200196235
# DO        -0.274225112  0.24511052  0.08426051  0.06145303 -0.27753216  0.0004668346
# COD        1.000000000 -0.21890561 -0.03795197 -0.28613573  0.18880582 -0.0081473581
# PH        -0.218905613  1.00000000  0.06787176  0.17850070 -0.05683173  0.0295731357
# Turbidity -0.037951971  0.06787176  1.00000000  0.28960891  0.33874228  0.0652164617
# TN        -0.286135733  0.17850070  0.28960891  1.00000000  0.14390781  0.0654755314
# TP         0.188805816 -0.05683173  0.33874228  0.14390781  1.00000000  0.0372010196
# RedTide   -0.008147358  0.02957314  0.06521646  0.06547553  0.03720102  1.0000000000
# 상관관계가 0.9 이상인 것은 없음

# 상관관계 시각화
corrgram(RedTide)
corrplot(corr)
chart.Correlation(RedTide,histogram=T)

# 로지스틱 회귀분석 X 분류나무/앙상블 모델

# 3. 분류나무모델
# 종속변수(Y) 범주 별 발생 빈도수 확인
# 0: 적조 발생하지 않음, 1: 적조 발생함
table(RedTide2$RedTide)
#    0    1 
# 1326   27 
prop.table(table(RedTide2$RedTide))
#          0          1 
# 0.98004435 0.01995565  

RedTide2$RedTide=as.factor(RedTide2$RedTide) # 숫자형 -> 요인형 변환

# 샘플 추출
set.seed(123)
samp=sample(x=nrow(RedTide2),0.7*nrow(RedTide2))
train=RedTide2[samp,]
test=RedTide2[-samp,]

# 분류나무모델 만들기
tree=rpart(formula=RedTide~.,data=train)
tree
# 1) root 947 19 0 (0.97993664 0.02006336)  
#   2) Temp< 24.06625 820  0 0 (1.00000000 0.00000000) *
#   3) Temp>=24.06625 127 19 0 (0.85039370 0.14960630)  
#     6) Temp>=24.68229 98  7 0 (0.92857143 0.07142857) *
#     7) Temp< 24.68229 29 12 0 (0.58620690 0.41379310)  
#       14) Wind< 2.124583 9  1 0 (0.88888889 0.11111111) *
#       15) Wind>=2.124583 20  9 1 (0.45000000 0.55000000)  
#         30) Temp< 24.26125 9  3 0 (0.66666667 0.33333333) *
#         31) Temp>=24.26125 11  3 1 (0.27272727 0.72727273) *

# 분류나무모델 시각화
rpart.plot(tree)
fancyRpartPlot(tree)

# 모델 예측하기
test_pred=predict(tree,newdata=test,type='class')
test_real=test$RedTide
tab=table(test_real,test_pred)
tab
#          test_pred
# test_real   0   1
#         0 402   1
#         1   6   2

# 정밀도(Precision)=(TP)/(TP+FP)
preci=tab[2,2]/sum(tab[,2])
preci # 0.6666667
# 민감도(TPR)=(TP)/(TP+FN)
Recall=tab[2,2]/sum(tab[2,])
Recall # 0.75
# F-측정치(F-Measure)=(정밀도*민감도)/(정밀도+민감도)
F_Measure=(preci*Recall)/(preci+Recall)
F_Measure # 0.3529412

# 4. 랜덤포레스트
sqrt(11) # 3.316625

# 1) mtry=4
RF2=randomForest(formula=RedTide~.,data=RedTide2,ntree=500,mtry=4,
                na.action=na.omit,importance=T)
RF2
# OOB estimate of  error rate: 2.22%

# 2) mtry=3
RF=randomForest(formula=RedTide~.,data=RedTide2,ntree=500,mtry=3,
                na.action=na.omit,importance=T)
RF
# OOB estimate of  error rate: 2.14%

# 독립변수(X) 중요도 구하기 
RF$importance
#                       0           1 MeanDecreaseAccuracy MeanDecreaseGini
# WTemp      1.608282e-02 0.017120618         1.583202e-02        6.8675472
# Temp       1.744924e-02 0.033676213         1.779576e-02        8.2253388
# Rain      -5.261013e-06 0.001688167         3.495514e-05        1.1145045
# Wind       1.830659e-03 0.004184443         1.816228e-03        4.5600324
# Salt       9.944316e-06 0.004648413         9.577612e-05        0.4230589
# DO         1.579235e-03 0.006572944         1.661834e-03        0.5165968
# COD       -2.053870e-04 0.005280880        -1.155815e-04        0.4163729
# PH        -2.360622e-04 0.003176984        -1.629265e-04        0.3441054
# Turbidity -2.754429e-04 0.002644444        -2.123009e-04        0.7156425
# TN        -5.177153e-04 0.014137590        -2.382106e-04        0.3238264
# TP         1.092028e-05 0.004876912         1.081763e-04        0.2736021
varImpPlot(RF) # Temp > WTemp > Wind > DO ...