#################################
## <제5장 연습문제>
################################# 

# 01. 다음 Bug_Metrics_Software 데이터셋을 이용하여 시각화하시오. 
install.packages('RSADBE')
library(RSADBE) # 패키지 로드  
data(Bug_Metrics_Software) # 데이터셋 로드 

str(Bug_Metrics_Software) # 데이터셋 구조보기 
# num [1:5, 1:5, 1:2] -> [행, 열, 면]
dim(Bug_Metrics_Software) # 5 5 2
# Software: 행이름
# Bugs: 버그 이름
# BA_Ind: 발표 전과 후
Bug_Metrics_Software

# Bug_Metrics_Software 데이터셋 설명 
# 5개 소프트웨어 발표 전 각 버그 수와 발표 후 각 버그의 수 
Bug_Metrics_Software[,,1] # 1면 : 소프트웨어 발표 전 버그 수
Bug_Metrics_Software[,,2] # 2면 : 소프트웨어 발표 후 버그 수

# 단계1) 소프트웨어 발표 전 버그 수를 대상으로 각 소프트웨어별 버그를
# beside형 세로막대 차트로 시각화하기(각 막대별 색상적용) 
par(mfrow=c(1,2))
barplot(Bug_Metrics_Software[,,1],beside=T,col=rainbow(5),
        xlab='소프트웨어',ylab='버그 수',
        main='소프트웨어 발표 전 버그 수')

# 단계2) 소프트웨어 발표 후 버그 수를 대상으로 각 소프트웨어별 버그를
# 누적형 가로막대 차트로 시각화하기(각 막대별 색상적용) 
barplot(Bug_Metrics_Software[,,2],beside=F,col=rainbow(5),
        xlab='소프트웨어',ylab='버그 수',
        main='소프트웨어 발표 후 버그 수')
# 범례 추가
legend(x=800,y=6,legend=row.names(Bug_Metrics_Software[,,2]),
       col=rainbow(5))

# 02. quakes 데이터 셋을 대상으로 다음 조건에 맞게 시각화 하시오.
data(quakes) # 데이터셋 로드  
str(quakes) # 데이터셋 구조보기 

# 조건1) 1번 칼럼 : y축, 2번 컬럼 : x축 으로 산점도 시각화
plot(quakes[,1],quakes[,2])

# 조건2) 5번 컬럼으로 색상 지정 : col = 
plot(quakes[,5],col='purple')

# 조건3) "지진의 진앙지 산점도 차트" 제목 추가  : main =
plot(quakes$long,quakes$lat,col=rainbow(8))

# 조건4) "quakes.jpg" 파일명으로 차트 저장하기
# 작업 경로 : "c:/itwill/3_Rwork/output"
# 파일명 : quakes.jpg
 #픽셀 : 폭(720픽셀), 높이(480 픽셀)
getwd()
jpeg("quakes.jpg",width=720,height=480)
plot(quakes$long,quakes$lat,col=rainbow(8))
dev.off()

# 03. iris3 데이터 셋을 대상으로 다음 조건에 맞게 산점도를 그리시오.
data("iris3")

# 조건1) iris3 데이터 셋의 자료구조 확인 : 힌트) str() 
str(iris3)

# 조건2) Setosa 꽃의 종을 대상으로 x축은 "Sepal W." 칼럼, 
#        y축은 "Sepal L." 칼럼으로 산점도 그리기 
plot(iris3[,c(2,1),1]) # 실답변

# 조건3) "Versicolor" 꽃의 종을 대상으로 산점도 행렬 시각화하기
plot(iris3[,c(2,1),2])

# 04. 각 년도별 물가상승률과 라면값 증가율을 비교하는 차트를 시각화하시오. 
# 시각화 결과 : "chap05_4번연습문제결과.png" 파일 참고 
# 힌트 : plot 2개 겹치기

getwd()
setwd("E:/03. R/data")
noodel = read.csv(file="noodle.csv")
str(noodel)

# step1
plot(noodel$price~noodel$year,ylim=c(0,500),ann=FALSE,type='o',col='blue')

# step2
par(new=TRUE)
plot(noodel$noodle~noodel$year,axes=FALSE,ann=FALSE,type='o',col='red')

title(main="물가와 라면값 증가율 비교")
title(xlab="년도",col.lab='blue')
title(ylab='증가율',col.lab='red')
?legend
legend(1980,450,legend=c('물가','라면'),lty=1,col=c('blue','red'))
