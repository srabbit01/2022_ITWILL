#################################
## <제15장 연습문제>
################################# 

# 01.  admit 객체를 대상으로 다음과 같이 로지스틱 회귀분석을 수행하시오.
# <조건1> 변수 모델링 : y변수 : admit, x변수 : gre, gpa, rank 
# <조건2> 7:3비율로 데이터셋을 구성하여 모델과 예측치 생성 
# <조건3> 분류 정확도 구하기 

# 파일 불러오기
getwd()
setwd("E:/03. R/data")
admit <- read.csv("admit.csv")
str(admit) # 'data.frame':	400 obs. of  4 variables:
#$ admit: 입학여부 - int  0 1 1 1 0 1 1 0 1 0 ...
#$ gre  : 시험점수 - int  380 660 800 640 520 760 560 400 540 700 ...
#$ gpa  : 시험점수 - num  3.61 3.67 4 3.19 2.93 3 2.98 3.08 3.39 3.92 ...
#$ rank : 학교등급 - int  3 3 1 4 4 2 1 2 3 2 ...


# 1. train/test data 나누기 
samp=sample(x=nrow(admit),0.7*nrow(admit))
train=admit[samp,]
test=admit[samp,]

# 2. model 생성 
library(nnet)
model=multinom(admit~.,data=train)

# 3. predict 생성 
pre=predict(model,test,type='class')
pre

# 4. 모델 평가(분류정확도) 

# 1) 혼동행렬 작성 
real=test$admit
table=table(pre,real)
table

# 2) 분류정확도(accuracy)
accuracy=sum(diag(table))/sum(table)
accuracy # 0.7035714

# 3) f1 score
# 정밀도(Precision)=TP/(TP+FP) # model(yes) -> yes
p=table[2,2]/sum(table[,2])
p

# 민감도=TP/(TP+FN) # real(yes) -> yes
r = table[2,2]/sum(table[2,])
r

# f측정치(f measure): 비율 뷸균형(조화평균)
f1=2*(p*r)/(p+r)
f1

# 4) ROCR 패키지 제공 함수 : prediction() -> performance
library(ROCR)
test_pred=model$fitted.values
test_y=test$admit

pr=prediction(test_pred,test_y)
prf=performance(pr,measure='tpr',x.measure='fpr')
plot(prf)

