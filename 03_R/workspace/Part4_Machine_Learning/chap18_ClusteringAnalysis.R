#chap18_ClusteringAnalysis

###################################################
# 군집분석(Clustering)
###################################################
# 유사성 거리에 의한 유사객체를 묶어준다.
# 거리를 측정하여 집단의 이질성과 동질성을 평가하고, 이를 통해서 
# 군집을 형성한다..
# 유사성 거리 : 유클리드 거리
# y변수가 없는 데이터 마이닝 기법
# 예) 몸, 키 관점에서 묶음 -> 3개 군집 <- 3개 군집의 특징 요약
# 주요 알고리즘 : hierarchical, k-means

# 그룹화를 통한 예측(그룹 특성 차이 분석-고객집단 이해)

# 1. 유클리드 거리
# 유클리드 거리(Euclidean distance)는 두 점 사이의 거리를 계산하는 
# 방법으로 이 거리를 이용하여 유클리드 공간을 정의한다.

# (1) matrix 생성
x <- matrix(1:9, nrow=3, by=T) 
x
# P1(1행) vs P2(2행)
sqrt(sum((x[1,]-x[2,])^2)) # 5.196152
# P1(1행) vs P3(3행)
sqrt(sum((x[1,]-x[3,])^2)) # 10.3923


# (2) matrix 대상 유클리드 거리 생성 함수
# 형식) dist(x, method="euclidean") -> x : numeric matrix, data frame
distance <- dist(x, method="euclidean") # method 생략가능
distance 
?dist

# (3) 활용분야
# 1) 분류모델: KNN(최근접 이웃 k개 분류)
# 2) 계층적 혹은 비계층적 군집모델
# 3) 추천모델: 유사도 계산
# 4) 좌표거리계산: 위도와 경도


# 2. 계층적 군집분석(탐색적 분석)
# - 계층적 군집분석(Hierarchical Clustering)
# - 거리가 가장 가까운 대상부터 결합하여 나무모양의 
#   계층구조를 상향식(Bottom-up)으로 만들어가면서 군집을 형성 

# (1) 군집분석(Clustering)분석을 위한 패키지 설치
install.packages("cluster") # hclust() : 계층적 클러스터 함수 제공
library(cluster) # 일반적으로 3~10개 그룹핑이 적정

# (2) 데이터 셋 생성
r <- runif(15, min = 1, max = 50) # 1~550
x <- matrix(r, nrow=5, by=T) 
x

# (3) matrix 대상 유클리드 거리 생성 함수
distance <- dist(x, method="euclidean") # method 생략가능
distance 

# (4) 유클리드 거리 matrix를 이용한 클러스터링
hc <-  hclust(distance, method="complete") # 완전결합기준

# 군집 방법(Cluster method) 
# method = "complete" : 완전결합기준(최대거리 이용) <- default(생략 시)
# method = "single" : 단순결합기준(최소거리 이용) 
# method = "average" : 평균결합기준(평균거리 이용) 

help(hclust)
plot(hc) # 클러스터 플로팅(Dendrogram) -> 1과2 군집(클러스터) 형성


#---------------------------------------------
#<실습> 중1학년 신체검사 결과 군집분석
#---------------------------------------------
# 단계1 : 데이터셋 가져오기 
getwd()
setwd("E:/03. R/data")
body <- read.csv("bodycheck.csv")
names(body)
body

# 단계2 : 거리계산 
idist <- dist(body)
idist

# 단계3 : 계층적 군집분석 
hc <- hclust(idist)
plot(hc,hang=-1) # 음수값 제외
# 3개 그룹 선정, 선 색 지정
rect.hclust(hc, k=3, border="red") # 3개 그룹 선정, 선 색 지정

# 단계4 : 각 그룹별 서브셋 만들기
g1<- body[c(10,4,8,1,15), ]
g2<- body[c(11,3,5,6,14), ]
g3<- body[c(2,9,13,7,12), ]

# 단계5 : 군집별 특성분석 
summary(g1)
# Mean   : 7.6   Mean   :25.6   Mean   :149.8   Mean   :36.6   Mean   :1
summary(g2)
# Mean   : 7.8   Mean   :33.8   Mean   :161.2   Mean   :48.8   Mean   :1.4
summary(g3)
# Mean   : 8.6   Mean   :40.6   Mean   :158.8   Mean   :56.8   Mean   :2 


######################################
## cutree()함수: 군집 별 서브셋 만들기
######################################
# 형식: cutree(hc,k=군집수) -> 관측치가 많은 경우 유용

g_num=cutree(hc,k=3) # 각 행 별 군집 번호 생성
g_num # 1~3

table(g_num)
# 1 2 3: 그룹수
# 5 5 5: 빈도수

# 해당 군집의 관측치 확인
g1=which(g_num==1) # 위치(index) 반환
g2=which(g_num==2)
g3=which(g_num==3)

g1 # 1  4  8 10 15
g2 # 2  7  9 12 13
g3 # 3  5  6 11 14

c1=body[g1,]
c2=body[g2,]
c3=body[g3,]


# 3. 계층형 군집분석과 군집 자르기 

# 1) 유클리드 거리 계산 
dist_re <- dist(iris[1:4]) # dist(iris[, -5])

# 2) 계층형 군집분석(클러스터링)
hc <- hclust(dist_re)
plot(hc, hang=-1)
rect.hclust(hc, k=3, border="red") # 3개 그룹수 

# 3) 그룹수 만들기 : cutree()함수 -> 각 군집별로 군집 자르기
# 형식) cutree(계층형군집결과, k=군집수) 
ghc<- cutree(hc, k=3) # stats 패키지 제공
ghc 

# 칼럼 추가
iris$cluster=ghc
head(iris)
tail(iris)
iris[c(51:100),]

plot(iris$Sepal.Length,iris$Petal.Length,col=iris$cluster)

cluster1=subset(iris,subset=cluster==1)
cluster2=subset(iris,subset=cluster==2)
cluster3=subset(iris,subset=cluster==3)

# 4. 비계층적 군집분석(확인적 분석)
# - 군집 수를 알고 있는 경우 이용하는 군집분석 방법

# 군집분석 종류 : 계층적 군집분석(탐색적), 비계층적 군집분석(확인적) 

# 1) data set 준비 
library(ggplot2)
data(diamonds)

nrow(diamonds) # [1] 53940
t <- sample(nrow(diamonds),1000) # 1000개 셈플링 

test <- diamonds[t, ] # 1000개 표본 추출
dim(test) # [1] 1000 10

# 데이터프레임 변환 
test_df <- as.data.frame(test)

head(test_df) # 검정 데이터
mydia <- test_df[c("price","carat", "depth", "table")] # 4개 칼럼만 선정
head(mydia)

# 2) 비계층적 군집분석(확인적 분석) - kmeans()함수 이용
# - 확인적 군집분석 : 군집의 수를 알고 있는 경우
model <- kmeans(mydia,centers=3)
model 
# K-means clustering with 3 clusters of sizes 302, 95, 603 - 군집수 
# Cluster means: 클러스터별 변수의 평균 
#       price     carat    depth    table
# 1  1410.407 0.4872924 61.65930 57.19884 -> 가장 품질이 낮은 다이아몬드 존재
# 2 13475.838 1.7194286 61.61810 57.57905 -> 가장 고가의 다이아몬드 존재
# 3  5940.474 1.1070307 61.80614 57.81775

# Clustering vector: 1~3 클러스터 번호 
# Within cluster sum of squares by cluster: 각 군집내 응집도 
# [1] 458279133 707085456 791803289] -> 작을 수록 좋음

# Available components: 군집분석 결과의 구성요소(9개)
names(model)
# 1] 모델 기본 정보
model$cluster # 1~3 클러스터 번호 
model$centers # 군집 별 각 변수의 중심
model$size # 군집 별 크기
# 2] 모델 평가 척도
model$totss # 제곱합의 총합 = 응집도 + 분리도
model$withinss # 각 군집 별 응집도 -> 작을 수록 좋음
model$tot.withinss # 응집도의 총합 = sum(model$withinss)
model$betweenss # 분리도 = 사이 거리의 제곱의 합 -> 클 수록 좋음

# 모델의 우수성 평가
between_ss=model$betweenss # 분리도 총합
tot_ss=model$totss
between_ss/tot_ss
# [해설] 1에 가까울 수록 좋은 모델

# 3) 원형데이터에 군집수 추가
mydia$cluster <- model$cluster
head(mydia) # cluster 칼럼 확인 

# 4) 변수 간의 상관성 보기 
plot(mydia[,-5])
cor(mydia[,-5], method="pearson") # 상관계수 보기 

#install.packages('corrgram')
library(corrgram) # 상관성 시각화 
corrgram(mydia[,-5], upper.panel=panel.conf) # 수치(상관계수) 추가(위쪽)


# 5) 비계층적 군집시각화
plot( mydia$price,mydia$carat, col=mydia$cluster)
plot(mydia[,-5],col=mydia$cluster)
# mydia$cluster 변수로 색상 지정(1,2,3)

# 각 그룹의 중심점에 포인트 추가 
points(model$centers[,c("price","carat")], col=c(3,1,2), 
       pch=8,cex=5)
# names(result2) -> centers 칼럼 확인 
# col : color, pch : 중심점 문자, cex : 중심점 문자 크기
# pch(plotting character), cex(character expansion)


# 6) k-means model 시각화 
install.packages('factoextra')
library(factoextra)

fv=fviz_cluster(model, data = mydia[-5])
fv
names(fv)
fv$plot_env
fv$labels
# 4개 차원 -> 상관계수 높은 변수 2개 차원으로 축소: x축 y축 2차원으로 축소
# 상관계수 높은 변수 2개: price, caret
# DIM1 48.8%(첫번째 차원의 공헌도) -> price 중성분
# DIM2 33.2%(두번째 차원의 공헌도) -> carat 주성분

eig=eigen(cor(mydia[-5]))
prc=prcomp(mydia[-5],scale=T,center=T)
prc
summary(prc)

mydia[29,] # cluster2: 고품질
#    price carat depth table cluster
# 29 17433  2.01  61.1    60       2

mydia[510,] # cluster3: 저품질
#     price carat depth table cluster
# 510  7644  1.17  59.3    59       3

mydia[27,] # cluster1
#     price carat depth table cluster
# 27  2674  0.72  60.8    56       1

##############################
## 최적의 군집수 찾기 
##############################

data("iris")

# data.frame -> matrix
iris_max <- as.matrix(iris[-5])
dim(iris_max) # 150   4

install.packages('NbClust') # 군집수 
library(NbClust)

nc <- NbClust(data = iris_max, distance = "euclidean", min.nc = 2, max.nc = 15, # 최소 최대 군집 수 범위 지정
              method = 'complete', index = "all", alphaBeale = 0.1)
# method: 군집 생성 방법
# index, alphaBeale (생략 가능)

# 결과 확인: 최적의 군집 수 3개
# According to the majority rule, the best number of clusters is  3 

names(nc)
# "All.index"          "All.CriticalValues" "Best.nc"            "Best.partition" 
# Best.nc
nc$All.index
nc$Best.nc
nc$Best.partition

# 그래프1(RED) Y축: 
# 그래프2(BLUE) Y축:

# 각 클러스터 빈도수 
table(nc$Best.nc[1,])
# 0  1  2  3  4  6 15 : 클러스터 개수
# 2  1  2 13  5  1  2 : 빈도수 -> 가장 빈도수가 높은 것이 이상적
barplot(table(nc$Best.nc[1,]))

# 최적의 군집수의 경우 군집 별 예상되는 빈도수
table(nc$Best.partition)
#  1  2  3 
# 50 72 28 