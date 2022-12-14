# chap11_CorrelationAnalysis

##################################################
# chap11. 상관관계 분석(Correlation_Analysis)
##################################################
# - 전제 조건: 숫자형 변수 대상
# - 두 변수에 대한 상관성의 방향과 크기 제공
# - 사용변수: 숫자형 변수 (등간척도/비율척도)
# - 관련함수: cor(상관계수), cov(공분산), cov2cor(공분산->상관계수)

getwd()
setwd('E:/03. R/data')
product <- read.csv("product.csv") # 상품 만족도
head(product) # 친밀도 적절성 만족도(등간척도 - 5점 척도)

# 기술통계량
summary(product) # 요약통계량

sd(product$제품_친밀도); sd(product$제품_적절성); sd(product$제품_만족도)
# 변수 간의 상관관계 분석 
# 형식) cor(x,y, method) # x변수, y변수, method(pearson): 방법

# 1) 상관계수(coefficient of correlation) : 두 변량 X,Y 사이의 상관관계 정도를 나타내는 수치(계수)
cor(product$제품_친밀도, product$제품_적절성) # 0.4992086 -> 다소 높은 양의 상관관계

cor(product$제품_친밀도, product$제품_만족도) # 0.467145 -> 다소 높은 양의 상관관계

# 시각화

# 전체 변수 간 상관계수 보기
cor(product, method="pearson") # 피어슨 상관계수 - default

# 방향성 있는 색상으로 표현 - 동일 색상으로 그룹화 표시 및 색의 농도 
install.packages("corrgram")   
library(corrgram)
corrgram(product) # 색상 적용 - 동일 색상으로 그룹화 표시
corrgram(product, upper.panel=panel.conf) # 수치(상관계수) 추가(위쪽)
corrgram(product, lower.panel=panel.conf) # 수치(상관계수) 추가(아래쪽)

# 차트에 곡선과 별표 추가
install.packages("PerformanceAnalytics") 
library(PerformanceAnalytics) 

# 상관성,p값(*),정규분포 시각화 - 모수 검정 조건 
chart.Correlation(product, histogram=T) 

# 상관계수 행렬 시각화 
install.packages('corrplot')
library(corrplot) # 상관계수 시각화 
corrplot( cor(product, method="pearson") )
# 타원의 크기: 두변수의 상관계수 크기
# 색상: 두 변수의 양음 방향 정도

# 자동차연비 관련 자료
str(mtcars)
Cor=cor(mtcars)

class(Cor)
Cor['mpg',]
corrplot(Cor)

# 2) 공분산(covariance) : 두 변량 
# X,Y의 관계를 나타내는 양
cov(product)
cor(product)
cov2cor(cov(product)) # 공분산 행렬 -> 상관계수 행렬 변환(기존 상관계수와 동일함) 

# 3) 상관계수 vs 공분산(ppt.12) 
# [1] 공분산 : 두 확률변수 간의 분산(평균에서 퍼짐 정도)를 나타내는 통계
#  - Cov(X,Y) = sum( (X-𝒙_bar) * (Y-𝒚_bar) ) / n
#  - 문제점 : 값이 큰 변수에 영향을 받는다.(값 큰 변수가 상관성 높음) : 
summary(product) # 값이 비슷한 자료는 공분산 사용 가능

x=product$제품_적절성
y=product$제품_만족도

x_bar=mean(x)
y_bar=mean(y)

cov_xy=mean((x-x_bar)*(y-y_bar)) # 모집단에 대한 공분산
cov_xy=sum((x-x_bar)*(y-y_bar))/(length(x)-1) # 표본집단에 대한 공분산


cov_xy # 0.5442637
cov(x,y) # 0.5463331 -> 표본집단에 대한 공분산

sum((x-x_bar)*(x-x_bar))/(length(x)-1) # 0.7390108 -> 같은 칼럼의 공분산을 구하더라도 1이 출력 X

# [2] 상관계수 : 공분산을 각각의 표준편차로 나눈어 정규화한 통계
#   - 공분산 문제점 해결 
#   - 부호는 공분산과 동일, 값은 절대값 1을 넘지 않음(-1 ~ 1)    
#   - Corr(X, Y) = Cov(X,Y) / std(X) * std(Y)
corr_xy=cov_xy/(sd(x)*sd(y))
corr_xy # 0.7668527
cor(x,y) # 0.7668527

# [3] 각 변수 간 scale(범위)이 다른 경우
getwd()
score_iq=read.csv('score_iq.csv')
score_iq
str(score_iq)
# id: 식별변수(구분자이지, 독립/종속변수로 사용하지 X)
summary(score_iq)

# score, iq, academy(학교) 간의 상관관계 -> 정규화(값을 일정하게 맞춤): 객관적 상관성 확인 가능
cor(score_iq[,2:4]) # 상관계수
#             score        iq   academy
# score   1.0000000 0.8822203 0.8962647 -> 상관성이 매우 높음
# iq      0.8822203 1.0000000 0.6717826 -> 상관성이 높음
# academy 0.8962647 0.6717826 1.0000000

# 문제: 공분산을 사용하는 경우
cov(score_iq[2:4]) # 표준화 -> 공분산
#             score        iq  academy
# score   42.968412 51.337539 7.119911
# iq      51.337539 78.807338 7.227293
# academy  7.119911  7.227293 1.468680
# 공분산 문제점: 값이 큰 변수가 더 큰 상관성을 가짐

# 스케일링: 변수의 척도(scale)을 맞추는 과정

# 1. 표준화: z = x(평균)/sigma(표준편차)
z_score=scale(score_iq) # 데이터프레임 -> 행렬(matrix)
summary(z_score) # 평균=0, 표준편차=1
cov(z_score) # 공분산의 결과와 동일
class(z_score)

cov(z_score[,2:4])
#             score        iq   academy
# score   1.0000000 0.8822203 0.8962647
# iq      0.8822203 1.0000000 0.6717826
# academy 0.8962647 0.6717826 1.0000000

# 2. 정규화: 최솟값/최댓값 이용
nor_scale=function(x){
  nor=(x-min(x))/(max(x)-min(x))
  return(nor)
}
nor_re=apply(score_iq[2:4],2,nor_scale)
apply(score_iq[2:4],MARGIN=2,FUN=nor_scale)
summary(nor_re) # min: 0, max: 1
class(nor_re)

cov(nor_re)
#              score         iq    academy
# score   0.06874946 0.05867147 0.07119911
# iq      0.05867147 0.06433252 0.05162352
# academy 0.07119911 0.05162352 0.09179251

# 4) 스피어만(Spearman) 상관계수
# - 서열척도 변수를 대상으로 단조 증가 또는 하강하는 관계를 나타내는 계수 
# - 선형성은 아니지면 줄곧 증가하거나 하강하는 관계 이용 

# 예) 국어성적 석차와 영어성적 석차의 관계
# cor(국어성적_석차, 영어성적_석차, method = "spearman") 

# 점수
kor_score=round(runif(10,min=50,max=90))
eng_score=round(runif(10,min=40,max=75))

kor_score
eng_score

# 서열척도: 순서 포함
kor_score_rank=sort(kor_score)
eng_score_rank=sort(eng_score)

kor_score_rank
eng_score_rank

# 스피어만 함수 
cor(kor_score_rank,eng_score_rank,method="spearman") # 0.9939209: 아주 강한 단조증가 형태
cor(kor_score_rank,eng_score_rank) # 피어슨 상관계수 -> 0.9620942: 아주 강한 형태 X

# 시각화
plot(kor_score_rank,eng_score_rank,type='l') # 선형
plot(kor_score_rank,eng_score_rank) # 산점도
