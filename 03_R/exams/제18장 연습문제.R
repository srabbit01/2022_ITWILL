#################################
## <제18장 연습문제>
################################# 

# 01. 다음은 15명의 면접자를 대상으로 가치관, 전문지식, 자격증 유무 등을 토대로 
#  종합점수에 근거하여 합격여부를 결정한 자료이다. 다음과 같은 단계로 계층적 
#  군집분석을 수행하여 군집수(cluster)를 탐색하고, 각 군집별로 서브셋을 작성하여 
#  각 군집의 특성을 분석하시오. 

# 단계1 : dataset 가져오기 
interview <- read.csv("interview.csv")
head(interview)

# 단계2 : 유클리디안 거리 계산  
inter_df <- interview[c(2:8)] # 응시번호와 합격여부 제외


# 단계3 : 계층적 군집분석 & 덴드로그램 시각화 
dis=dist(inter_df)
hc=hclust(dis)
plot(hc,hang=-1)
rect.hclust(hc,k=3,border="red")

# 단계4 : 군집별 서브셋 만들기 : cutree()함수 이용 
num=cutree(hc,k=3)

g1=inter_df[which(num==1),]
g2=inter_df[which(num==2),]
g3=inter_df[which(num==3),]

# 단계5 : 각 군집별 특성 분석 : summary()함수 이용 
summary(g1) # 자격증: 1, 종합점수: 75
summary(g2) # 자격증: 0.4, 종합점수: 62.8
summary(g3) # 자격증: 0, 종합점수: 71.6

# 02. 다음과 같은 조건을 이용하여 각 단계별로 비계층적 군집분석을 수행하시오.

# 조건1) 대상 파일 : product_sales.csv
# 조건2) 변수 설명 : tot_price : 총구매액, buy_count : 구매횟수, 
#                    visit_count : 매장방문횟수, avg_price : 평균구매액

sales <- read.csv("product_sales.csv", header=TRUE)
head(sales) 

# 단계1: 비계층적 군집분석 : 3개 군집으로 군집화
str(sales)
model=kmeans(sales,3)
model

# 단계2: 원형데이터에 군집수 추가
sales$cluster=model$cluster

# 단계3 : tot_price 변수와 가장 상관계수가 높은 변수와 군집분석 시각화
cor(sales) # avg_price

# 단계4. 군집의 중심점 표시
plot(sales$tot_price,sales$avg_price,col=sales$cluster)
points(model$centers[,c('tot_price','avg_price')],pch=8,cex=1.2)
