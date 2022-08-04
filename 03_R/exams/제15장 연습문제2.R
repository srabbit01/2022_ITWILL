#################################
## <제15장 연습문제>
################################# 

# 02. 아래와 같은 단계를 이용하여 로지스틱 회귀분석을 수행하시오.


# 단계1. 패키지 설치 및 데이터 로드 

install.packages('survival')
library(survival)

# 1858명 colon 데이터셋 
str(colon)
# 종속변수 : status(대장암 재발 또는 사망인 경우 1)
# 독립변수 
# obstruct : 종양에 의한 장 폐쇄
# perfor : 장의 천공
# adhere : 인접장기와 유착
# nodes : 암세포가 확인된 림프절 수
# differ : 암세포의 조직학적 분화 정도
# extent : 암세포의 침습한 깊이
# surg : 수술후 등록까지 시간(0=short, 1=long) 


# 단계2. 결측치 제거 : 칼럼에 포함된 모든 결측치 제거 
colon=na.omit(colon)
dim(colon) # [1] 1776   16

# 단계3. 기본 glm모델 만들기 : 종속변수 ~ 독립변수 
model=glm(status~obstruct+perfor+adhere+nodes+differ+extent+surg,data=colon,
          family='binomial')

# 단계4. 효과적인 변수 선택 : 후진제거법(backword)으로 유의하지 않은 변수 제거 
library(MASS) # 힌트) stepAIC() 이용 
stepAIC(model,direction='backward')

# 단계5. 훈련셋과 평가셋 7:3 나누기 : 결측치가 제거된 데이터셋 이용  
set.seed(123) # 시드값 이용 샘플링 
samp=sample(x=nrow(colon),0.7*nrow(colon))

train=colon[samp,]
test=colon[-samp,]

# 단계6. 훈련셋으로 모델 생성 : 훈련셋 이용, 유의하지 않은 변수 제거
model2=glm(formula = status ~ obstruct + adhere + nodes + extent + surg, 
           family = "binomial", data = test)


# 단계7. 평가셋으로 모델 평가 : 혼동행렬 & 분류정확도 
pre=predict(model2,test,type='response')
range(pre)
pre=ifelse(pre>=0.5,1,0)

real=test$status

tab=table(pre,real)
#        real
# pre   0   1
# 0   201 114
# 1    63 155

acc=sum(diag(tab))/sum(tab)
acc # [1] 0.6679174