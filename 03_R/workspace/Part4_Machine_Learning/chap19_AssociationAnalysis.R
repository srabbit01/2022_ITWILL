# chap19_AssociationAnalysis

###################################################
# 연관분석(Association Analysis)
###################################################

# 특징
# - 데이터베이스에서 사건의 연관규칙을 찾는 무방향성 데이터마이닝 기법                                            
# - 무방향성(x -> y변수 없음) -> 비지도 학습에 의한 패턴 분석 방법
# - 사건과 사건 간 연관성(관계)를 찾는 방법(예:기저귀와 맥주)
# - A와 B 제품 동시 구매 패턴(지지도)
# - A 제품 구매 시 B 제품 구매 패턴(신뢰도)


# 예) 장바구니 분석 : 장바구니 정보를 트랜잭션(상품 거래 정보)이라고 하며,
# 트랜잭션 내의 연관성을 살펴보는 분석기법
# 분석절차 : 거래내역 -> 품목 관찰 -> 상품 연관성에 대한 규칙(Rule) 발견

# 활용분야
# - 대형 마트, 백화점, 쇼핑몰 등에서 고객의 장바구니에 들어있는 품목 간의 
#   관계를 탐구하는 용도
# ex) 고객들은 어떤 상품들을 동시에 구매하는가?
#   - 맥주를 구매한 고객은 주로 어떤 상품을 함께 구매하는가?


#########################################
# 1. 연관규칙 평가 척도
#########################################

# 연관규칙의 평가 척도
# 1. 지지도(support) : 전체자료에서 A를 구매하고 B를 구매하는 거래 비율 
#  A->B 지지도 식 
#  -> A와 B를 포함한 거래수 / 전체 거래수
#  -> n(A, B) : 두 항목(A,B)이 동시에 포함되는 거래수
#  -> n : 전체 거래 수

# 2. 신뢰도(confidence) : A가 포함된 거래 중에서 B를 포함한 거래의 비율(조건부 확률)
# A->B 신뢰도 식
#  -> A와 B를 포함한 거래수 / A를 포함한 거래수

# 3. 향상도(Lift) : 하위 항목들이 독립에서 얼마나 벗어나는지의 정도를 측정한 값
# 향상도 식
#  -> 신뢰도 / B가 포함될 거래율


# <지지도와 신뢰도 예시>
# 거래 6개 범주 5개
# t1 : 라면,맥주,우유
# t2 : 라면,고기,우유
# t3 : 라면,과일,고기
# t4 : 고기,맥주,우유
# t5 : 라면,고기,우유
# t6 : 과일,우유

0.5/4
0.333/2

#    A -> B                 지지도         신뢰도          향상도
#  맥주 -> 고기         1/6=0.166       1/2=0.5      0.5/0.66(4/6)=0.75
# 라면,우유 -> 맥주     1/6=0.166       1/3=0.333    0.333/0.333(2/6)=1

## 연관성 규칙 분석을 위한 패키지
#install.packages("arules") # association Rule
# read.transactions(),  apriori(), Adult 데이터셋 제공
library(arules) #read.transactions()함수 제공


# 1. transaction 객체 생성(파일 이용)
getwd()
setwd("E:/03. R/data")
tran<- read.transactions("tran.txt", format="basket", sep=",")
tran

# 2. transaction 데이터 보기
inspect(tran)

# 3. rule 발견(생성) - 지지도,신뢰도 = 0.1
# apriori(트랜잭션 data, parameter=list(supp, conf))

# 연관성 규칙 평가 척도 - 지지도와 신뢰도
rule1 <- apriori(tran, parameter = list(supp=0.3, conf=0.1)) # 16 rule
rule2 <- apriori(tran, parameter = list(supp=0.1, conf=0.1)) # 35 rule 
rule3 <- apriori(tran, parameter = list(supp=0.3, conf=0.5)) # 13 rule
inspect(rule1) # 규칙 보기
inspect(rule2) # 규칙 보기
inspect(rule3)

# items             
# [1] {라면, 맥주, 우유}
# [2] {고기, 라면, 우유}
# [3] {고기, 과일, 라면}
# [4] {고기, 맥주, 우유}
# [5] {고기, 라면, 우유}
# [6] {과일, 우유}   

#      lhs             rhs    support   confidence coverage  lift  count
# [10] {고기}       => {우유} 0.5000000 0.7500000  0.6666667 0.900 3    
# 지지도(support)
supp=3/6 # 0.5
# 신뢰도
conf=3/6/(4/6) # 0.75
# 포함율
cov=(5/6)/(6/6) # 0.8333333
# 향상도
0.75/0.83

# 지지도, 신뢰도, maxlen 인수  
help("apriori") # support 0.1, confidence 0.8, and maxlen 10 
rule <- apriori(tran) 
rule<- apriori(tran, parameter = list(supp=0.1, conf=0.8, maxlen=10)) 

inspect(rule) 

# maxlen=lhs수+rhs수

#########################################
# 2. 트랜잭션 객체 생성 
#########################################

#형식)
#read.transactions(file, format=c("basket", "single"),
#      sep = NULL, cols=NULL, rm.duplicates=FALSE, encoding="unknown")
#------------------------------------------------------
#file : file name
#format : data set의 형식 지정(basket 또는 single)
# -> single : 데이터 구성(2개 칼럼) -> transaction ID에 의해서 상품(item)이 대응된 경우
# -> basket : 데이터 셋이 여러개의 상품으로 구성 -> transaction ID 없이 여러 상품(item) 구성
#sep : 상품 구분자
#cols : single인 경우 읽을 컬럼 수 지정, basket은 생략(transaction ID가 없는 경우)
#rm.duplicates : 중복 트랜잭션 항목 제거
#encoding : 인코딩 지정
#------------------------------------------------------

# (1) single 트랜잭션 객체 생성
## read demo data - sep 생략 : 공백으로 처리, single인 경우 cols 지정 
# format = "single" : 1개의 transaction id에 의해서 item이 연결된 경우 
stran <- read.transactions("demo_single",format="single",cols=c(1,2)) 
inspect(stran)
#     items          transactionID
# [1] {item1}        trans1       
# [2] {item1, item2} trans2   

stran_new <- read.transactions("demo_single2.txt",format="single",cols=c(1,2),rm.duplicates=T) 
inspect(stran_new)

bas_new = read.transactions('item.txt',format='basket',rm.duplicates=F)
inspect(bas_new)

bas_new2 = read.transactions('item.txt',format='basket',rm.duplicates=T)
inspect(bas_new2)

# <실습> 중복 트랜잭션 객체 생성
stran2<- read.transactions("single_format.csv", format="single", sep=",", 
                           cols=c(1,2), rm.duplicates=F)
stran2
?read.transactions
inspect(stran2)

summary(stran2) # 248개 트랜잭션에 대한 기술통계 제공


# 트랜잭션 보기
inspect(stran2) # 248 트랜잭션 확인 

# 규칙 발견
astran2 <- apriori(stran2) # supp=0.1, conf=0.8와 동일함 
#astran2 <- apriori(stran2, parameter = list(supp=0.1, conf=0.8))
astran2 # set of 102 rules
attributes(astran2)
inspect(astran2)

# 향상도가 높은 순서로 정렬 
inspect(sort(astran2, by="lift"))

# (2) basket 트랜잭션 데이터 가져오기
btran <- read.transactions("demo_basket",format="basket",sep=",") 
inspect(btran) # 트랜잭션 데이터 보기

##############################################
# 3. 연관규칙 시각화(Adult 데이터 셋 이용)
##############################################

data(Adult) # arules에서 제공되는 내장 데이터 로딩
str(Adult) # Formal class 'transactions' , 48842(행)
# slot 3개: data, itemInfo, itemsetInfo -> 각 자료 맴버
# data는 data slot에 저장
# 실제 아이템에 대한 정보는 itemInfo에 저장

Adult

attributes(Adult)# 트랜잭션의 변수와 범주 보기
################ Adult 데이터 셋 #################
# 인구조사데이터를 기반으로 32,000개의 관찰치와 15개의 변수로 
# 구성되어 있으며, 년간 소득이 5만달러를 초과하는지 여부를
# 예측하는 데이터 셋으로 transactions 데이터로 읽어온
# 경우 48,842행(트랜잭션수)과 115 항목(범주)으로 구성된다.
##################################################

# 요약 통계량
summary(Adult)


#---------------------------------------------------------------
# 신뢰도 80%, 지지도 10%이 적용된 연관규칙 6137 발견   
#----------------------------------------------------------------
ar1 <- apriori(Adult, parameter = list(supp=0.1, conf=0.8)) # 6137 가장 규칙 수 많음
ar2 <- apriori(Adult, parameter = list(supp=0.2)) # 지도도 높임
ar3 <- apriori(Adult, parameter = list(supp=0.2, conf=0.95)) # 신뢰도 높임
ar4 <- apriori(Adult, parameter = list(supp=0.3, conf=0.95)) # 신뢰도 높임
ar5 <- apriori(Adult, parameter = list(supp=0.35, conf=0.95)) # 신뢰도 높임
ar6 <- apriori(Adult, parameter = list(supp=0.4, conf=0.95)) # 신뢰도 높임 -> 36 가장 규칙 수 적음

# 결과보기
inspect(head(ar6)) # 상위 6개 규칙 제공 -> inspect() 적용

# confidence(신뢰도) 기준 내림차순 정렬 상위 6개 출력
inspect(head(sort(ar6, decreasing=T, by="confidence")))

# lift(향상도) 기준 내림차순 정렬 상위 6개 출력
inspect(head(sort(ar6, by="lift"))) 


## 연관성 규칙에 대한 데이터 시각화를 위한 패키지
#install.packages("arulesViz") 
library(arulesViz) # rules값 대상 그래프를 그리는 패키지

plot(ar4,method=NULL) # 지지도(support), 신뢰도(conf) , 향상도(lift)에 대한 산포도
plot(ar5, method="graph") #  연관규칙 네트워크 그래프
# 각 연관규칙 별로 연관성 있는 항목(item) 끼리 묶여서 네트워크 형태로 시각화
# 화살표: 아이템 간 관계
# 향상도: 색상
# 지지도: 타원의 크기

# 중심어 기준 subset
# rhs: 자본 손실 없음 -> 연관어
sub1=subset(ar5,rhs %in% 'capital-loss=None') # set of 34 rules
inspect(sub1)
plot(sub1,method='graph')
# lhs: 인종=백인 -> 연관어
sub2=subset(ar5,lhs %in% 'race=White')
inspect(sub2)
plot(sub2,method='graph')

######################################
# 4. 식료품점 파일 예제 
######################################

library(arules)

# transactions 데이터 가져오기
data("Groceries")  # 식료품점 데이터 로딩
str(Groceries) # Formal class 'transactions' [package "arules"] with 4 slots
Groceries

rules <- apriori(Groceries, parameter=list(supp=0.001, conf=0.8))

inspect(rules) 
# 규칙을 구성하는 왼쪽(LHS) -> 오른쪽(RHS)의 item 빈도수 보기  
plot(rules, method="grouped")

# 최대 길이 3이내로 규칙 생성
rules <- apriori(Groceries, parameter=list(supp=0.001, conf=0.80, maxlen=3))
inspect(rules) # 29개 규칙

# confidence(신뢰도) 기준 내림차순으로 규칙 정렬
rules <- sort(rules, decreasing=T, by="confidence")
inspect(rules) 

library(arulesViz) # rules값 대상 그래프를 그리는 패키지
plot(rules, method="graph", control=list(type="items"))

# 1. rhs: whole milk (전지분유)
sub3=subset(rules,rhs %in% 'whole milk')
inspect(sub3)
plot(sub3,method='graph')
# 1) 지지도 높은 상품: 동시에 구매 가능성이 높은 상품 -> 허브+ 롤빵, 커드+햄버거
# 2) 향상도 높은 상품 : 관련성 높은 상품 -> 쌀+설탕

# 2. rhs: other vegetables
sub4=subset(rules,rhs %in% 'other vegetables')
sub4 # set of 10 rules
inspect(sub4)
plot(sub4,method='graph')

# 3. 2개 이상의 선행 사건이 동시 포함: lhs = yogurt + rice
sub5=subset(rules,lhs %in% c('yogurt','rice')) # or 관계: 둘 중 하나, 아니면 모두 포함 된 경우 추출
inspect(sub5)
plot(sub5,method='graph')
