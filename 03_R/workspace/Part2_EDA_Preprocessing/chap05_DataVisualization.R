# chap05_DataVisualization

# 1. 이산형 변수 시각화
# - 정수 단위로 나누어 지는 변수 (자녀수, 판매수)

## 차트 데이터 생성
chart_data <- c(305,450, 320, 460, 330, 480, 380, 520)
length(chart_data) # 8

## 각 원소에 이름 추가
names(chart_data) <- c("2016 1분기","2017 1분기","2016 2분기","2017 2분기","2016 3분기","2017 3분기","2016 4분기","2017 4분기")
str(chart_data)
# Named num [1:8] 305 450 320 460 330 480 380 520
# - attr(*, "names")= chr [1:8] "2016 1분기" "2017 1분기" "2016 2분기" "2017 2분기" ... # 각각 이름이 들어갔으며, 이름의 자료형은 문자형임을 의미
# [숫자1:숫자2]: 1차원 의미
# 만일, [숫자1:숫자2,숫자3:숫자4]: 2차원

chart_data
range(chart_data)

# 1) 막대 차트

# (1) 세로 막대차트
barplot(chart_data,ylim=c(0,600),
        main='2016년 vs 2017년도 매출현황',
        ylab='매출액(단위:천원)',
        xlab='년도별 판매 현황',
        col=rainbow(8))
# (2) 가로 막대차트
barplot(chart_data,xlim=c(0,600),
        horiz=TRUE,
        main='2016년 vs 2017년도 매출현황',
        ylab='매출액(단위:천원)',
        xlab='년도별 판매 현황',
        col=rainbow(8))

# (3) 범례추가
barplot(chart_data,ylim=c(0,800),
        main='2016년 vs 2017년도 매출현황',
        ylab='매출액(단위:천원)',
        xlab='년도별 판매 현황',
        offset=100,
        inside=F,plot=T,
        col=rainbow(8),
        legend.text = names(chart_data), # 범례 추가
        args.legend = list(x = 'topleft'))
# 범례 위치: x = 'topleft', 'topright', 'top'

# (4) 텍스트 추가: 
## [text] 추가 
bp <- barplot(chart_data, ylim = c(0, 600),
              col = rainbow(8), 
              ylab = '매출액(단위:천원)', 
              xlab = "년도별 분기현황",
              main ="2016년 vs 2017년 분기별 매출현황")
# text 반영
text(x = bp, y = char_data + 20, # 차트추가 위치
     labels = chart_data, col = "black", cex = 0.7)
# text 위치: x=막대위치(중앙), y=data+20
#            labels: text 자료, col: text 색상, cex= text 확대/축소


# (5) 1행 2열 차트 그리기
par(mfrow =c(1,2)) # 1 행 2 열 그래프 보기

## 개별형 막대 차트 (beside 기본: TURE)
barplot(VADeaths ,beside=T,col =rainbow(5),main="미국 버지니아주 하위계층 사망비율")
legend(19, 71, c("50 54","55 59","60 64","65 69","70 74"), cex =0.8, fill=rainbow(5))

## 누적형 막대 차트: beside=FALSE
barplot(VADeaths ,beside=F,col =rainbow(5),main="미국 버지니아주 하위계층 사망비율")

# 2) 점 차트
dotchart(chart_data,color=c("green","red "),gcolor='blue',lcolor ="yellow",
         labels= names(chart_data),
         xlab='매출액', main="분기별 판매현황",cex =1.2,gdata=FALSE)

# pch: 점의 모양 (1: 동그라미, 2: 삼각형)
# lcolor: 선 색상
# cex: x축/y축 모든 text 확대/축소

# 3) 파이 차트
pie(chart_data,border='blue',
    col =rainbow(8), cex =1.2)
## 제목 별도 추가 함수
title("2014~2015 년도 분기별 매출현황")

## 파이 차트 주의사항: 비율(점유율) -> 전체 중 차지하는 비율 환산(수치 그대로 X)
genre = c(45,25,15,30) # 100명 대상 장르 선호도 질문 시 (중복 허용 상태태)
sum(genre) # 중복이 되었기 때문에 집계값 115
names = names(genre) = c('액션','스릴러','공포','드라마')
genre

pie(genre,label=names,col=rainbow(4),
    main="영화 장르별 선호도")

rate = genre/sum(genre)
rate
# 실제 파이 차트는 비율로 표현됨
# 액션    스릴러      공포    드라마 
# 0.3913043 0.2173913 0.1304348 0.2608696 

labels = names(genre)
# 문자열 결합
labels = paste(labels,'\n',round(rate,2))

# 새로운 레이블 반영
pie(genre,label=labels,col=rainbow(4),lty=3,
    main="영화 장르별 선호도")


# 2. 연속형 변수 시각화
# - 주어진 범위 안의 모든 연속된 값(실수값)을 갖는 변수
# - 시간, 길이, 키, 몸무게, 나이, 구매금액 등

# 1) 상자 그래프
# - 요약 통계 정보 -> 시각화 도구
# - 확인 가능한 통계계: 사분위수(1,2,3), 최소값, 최대값, 이상치

# 1940년도 버지니아주의 1000명 당 사망률
VADeaths # 세로: 연령그룹 # 가로: 인구그룹(시골/도시&남자,여자)

summary(VADeaths) # 요약통계
boxplot(VADeaths)

# 사분위수
quantile(VADeaths[,1])
# 0%(Min)   25%   50%(Median) 75%  100%(Max)
# 11.7      18.1  26.9        41.0 66.0 

# 2) 히스토그램
# - 일정한 계급의 빈도수 확인 -> 막대 그래프로 보임

data(iris)
str(iris)
summary(iris)

range(iris$Sepal.Length) # 4.3 7.9

# (1) 기본 히스토그램(옵션X)
# 여러 개의 변수 한번에 시각화 X
# 하나 변수의 범주 확인 위해 사용
# y축 frequency: 빈도수
hist(iris$Sepal.Length,xlab='꽃받침',main='붓꽂의 꽃받침 길이')
# 각 계급 영역에서 값이 나타나는 비율 표시
# 계급은 연속성을 띠기 때문에 각 계급이 자동으로 나뉨

# (2) 계급수 조정
# x축의 개수를 원하는 대로 지정
hist(iris$Sepal.Length,xlab='꽃받침',
     main='붓꽂의 꽃받침 길이',
     breaks=30) # 계급수
# 계급의 간격이 촘촘해짐

# (3) 확률밀도함수(pdf): 확률변수 x의 크기 추정(계산) 함수
# 전체 넓이: 1
# 출현 빈도수가 아닌 전체 중 얼마나 차지하고 있는지 표기

# Step1: 밀도 단위 변경 (밀도=비울=확률)
hist(iris$Sepal.Length,xlab='꽃받침',
     main='붓꽂의 꽃받침 길이',
     freq=FALSE) # 밀도단위 히스토그램

# Step2: 확률밀도함수: 확률 밀도를 추정하여 곡선 분포 추가
lines(density(iris$Sepal.Length),col='blue')

# 3) 산점도: 두 변수의 값이 만나는 점 그래프
plot(x=iris$Sepal.Length,y=iris$Petal.Length)
plot(iris$Petal.Length~iris$Sepal.Length)

# 1) 4개의 격자 이용
price=runif(10,1,100) # 1~100사이 10개의 난수 발생
price # price=c(1:10)

# 자료가 1개 -> y축: 자료, x축: 자료 색인(Index)
par(mfrow=c(2,2)) # 2행 2열 차트 그리기기 # 격자 4개 분할
plot(price,type='l') # 유형: 실선
plot(price,type='o') # 유형: 원형과 실선 연결 (원형 통과)
plot(price,type='h') # 직선
plot(price,type='s') # 계단형: 꺾은선

# plot() 함수 속성 : pch : 연결점 문자타입 --> plotting characher 번호 (1~30)
plot(price, type="o",pch =5) # 빈 사각형
plot(price, type="o",pch =15) # 채워진 마름모
plot(price, type="o",pch =20, col ="blue") #color 지정
plot(price, type="o",pch =20, col ="orange", cex =1.5) #character expension 확대
plot(price, type="o",pch =20, col ="green", cex =2.0, lwd =3) #lwd : line width 선 굵기

# 2) 만능차트: 데이터에 따라 적절한 그래프 자동 제공
# plot을 통해 볼 수 있는 다양한 차트
methods(plot)
# acf: 시계열 관련, lm: 회귀모델 관련, hclust: 군집분석 관련, ts: 시계열 관련
# TukeyHSD: 분산분석 결과 시각화, princomp: 요인 분석 시각화
# 객체 유형에 따라 적합한 그래프 제시 -> 다양한 그래프 조회 가능

# (1) 시계열 데이터: 시간의 변화에 따른 통계량의 변화 -> 추세선이 적합

# 인터넷 사용 시간을 제공하는 시계열 데이터
WWWusage # Time Series: 분당 인터넷 사용 시간 # Frequency: 1분당
# 메모리 상에 있기 때문에 객체와 같음

plot(WWWusage) # 추세선

# (2) 회귀모형: 관련 차트 (회귀선 시각화)
plot(iris$Petal.Length~iris$Sepal.Length,col='blue') # 비례관계
# 반대로 왼쪽 상단 ~ 오른쪽 하단 방향은 반비례 관계

# x에 따라 y의 변화를 확인하는 것
# 회귀모델 생성 함수: lm
model = lm(iris$Petal.Length~iris$Sepal.Length) # 회귀모델
model # y절편 기울기: (Intercept)  iris$Sepal.Length 

# 산점도에 회귀선 추가(추정)
abline(model,col='red')

plot(model) # 회귀모델 관련 차트들 보여줌
# 2. y에 대한 적합치와 잔차에 대한 산점도 출력
# ...

# 3) plot 2개 이상 겹치기
# (1) 그래프 1개 그리기
plot(iris$Sepal.Length,type='o',ann=FALSE,col='blue')
# ann=FALSE: 축 이름 제거 -> 새로운 차트 추가 시 헷갈릴 수 있어 제거
# ann=TRUE: 축이름 존재

# (2) 그래프 겹치기
plot(iris$Petal.Length,type='o',ann=FALSE,col='red') # 이러면 새로운 차트 생성

# 대개 예측 데이터와 실제 데이터를 비교하고자 할 때 사용
par(new=TRUE) # 만일 직접의 차트에 겹치려면
plot(iris$Petal.Length,type='o',axes=FALSE,ann=FALSE,col='red') 
# axes=FALSE: 축의 제거

# (3) 범례 그리기: legend
legend(x=0,y=7,legend=c("꽃받침 길이","꽃잎 길이"),
       col=c('blue','red'),lty=1) # 범례가 그려질 좌표
# lty: 선 스타일 -> 1: 선, 3: 점 등
title(main='iris 데이터셋 길이 비교')

# 4) 산점도 행렬(Scatter Matrix): 하나의 변수 기준으로 여러 변수와 관계 시각화 (1:n)
# - 용도: 연속형 변수가 많은 경우, 변수간 비교할 때 사용
# pairs(여러칼럼을 가진 인수)
pairs(iris[-5]) # 5번 변수 제외
# 각 변수들 끼리 선형관계인지 확인 (관련성 여부 확인)

# 꽃의 종: 빈도수
table(iris$Species)
# 꽂 별로 50개씩 존재
#     setosa versicolor  virginica 
#     50         50         50
pairs(iris[iris$Species=='setosa',1:4]) # x축, y축 개수(1:4 = 칼럼 4개만 사용)
pairs(iris[iris$Species=='versicolor',1:4])
pairs(iris[iris$Species=='virginica',1:4])


# 3. 차트 파일 저장
getwd() # "E:/03. R"
setwd("E:/03. R/output")

# 블록형 스크립트: 한 블록의 문장이 다 끝나야 실행 완료
jpeg('iris_sm.jpg',width=720,height=480) # file open
# 가로세로 길이가 길 수록 필셀 수가 많아 고해상도이나, 많은 용량 차지지
pairs(iris[-5]) # 차트 시각화
dev.off() # file close

# 4. 3차원 산점도
# 별도의 패키지 설치 필요
# z축까지 3개의 칼럼 관계 확인
install.packages('scatterplot3d')
library(scatterplot3d)

# 꽃의 종류별 분류 
iris_setosa = iris[iris$Species == 'setosa',] # 50
iris_versicolor = iris[iris$Species == 'versicolor',] # 50
iris_virginica = iris[iris$Species == 'virginica',] # 50

# scatterplot3d(밑변, 오른쪽변, 왼쪽변, type='n') # type='n' : 기본 산점도 제외 
d3 <- scatterplot3d(iris$Petal.Length, iris$Sepal.Length, iris$Sepal.Width, type='n')
# scatterplot3d(x축,y축,z축,type='종류') # 3d 큐브의 틀 만들기

# 각각의 데이터 추가
d3$points3d(iris_setosa$Petal.Length, iris_setosa$Sepal.Length,
            iris_setosa$Sepal.Width, bg='orange', pch=21) # 동그라미
d3$points3d(iris_versicolor$Petal.Length, iris_versicolor$Sepal.Length,
            iris_versicolor$Sepal.Width, bg='blue', pch=23) # 마름모
d3$points3d(iris_virginica$Petal.Length, iris_virginica$Sepal.Length,
            iris_virginica$Sepal.Width, bg='green', pch=25) # 역삼각형
# 요인 분석 시, 세개의 요인을 겹치지 않고 출력하기 위해 사용