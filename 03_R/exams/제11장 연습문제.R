#################################
## <제11장 연습문제>
################################# 

# 01. 우리나라 전체 중학교 2학년 여학생 평균 키가 148.5cm로 알려져 있는 상태에서  
# A중학교 2학년 전체 500명을 대상으로 10%인 50명을 표본으로 선정하여 표본평균신장을 
# 계산하고, 모집단의 평균과 차이가 있는지를 검정하시오.(단일표본 T검정)

setwd('C:/ITWILL/3_Rwork/data')

# 단계1 : 데이터셋 가져오기
data <- read.csv("student_height.csv")
height <- data$height
head(height)


# 단계2 : 기술통계량/결측치 확인
summary(height)
mean(height)

# 단계3 : 정규성 검정 - 기본가정 
shapiro.test(height)
#  p-value = 0.0001853 < 유의수준: 귀무가설 기각
hist(height)

# 단계4 : 가설검정 - 양측검정  
wilcox.test(height,alter='two.sided',mu=148.5) # 유의확률:0.067 < 유의수준:0.05 -> 기각



# 02. 교육방법에 따라 시험성적에 차이가 있는지 검정하시오.(독립표본 T검정)
#조건1) 변수 : method : 교육방법, score : 시험성적
#조건2) 모델 : 교육방법(명목)  ->  시험성적(비율)
#조건3) 전처리 : 결측치 제거 : 평균으로 대체 


#단계1. 실습파일 가져오기
Data <- read.csv("twomethod.csv", header=TRUE)
head(Data) #3개 변수 확인 -> id method score

#단계2. 두 집단 subset 작성
unique(Data$method) # 1 2

# 변수 선택 -> 서브셋 생성 
data_df <- Data[c('method', 'score')]
data_df


#단계3. 데이터 분리
# 1) 교육방법으로 집단 분리
table(data_df$method)
method1=subset(data_df,data_df$method==1)
method2=subset(data_df,data_df$method==2)

# 2) 교육방법에서 시험성적 추출
score1=method1$score
score2=method2$score

#단계4 : 분포모양 검정: 등분산성
var.test(score1,score2) # p-value = 0.8494 > 0.05: 귀무가설 채택
mean(score1,na.rm=T) # [1] 16.40909
mean(score2,na.rm=T) # [1] 29.22857

#단계5: 가설검정
t.test(score1,score2,alter='two.sided',conf.int=T) # 1.303e-06 < 0.05: 귀무가설 기각
t.test(score1,score2,alter='greater',conf.int=T) #  p-value = 1 > 0.05 : 귀무가설 채택
t.test(score1,score2,alter='less',conf.int=T) # 6.513e-07 < 0.05: 귀무가설 기각


# 03.datas를 대상으로 연령별(age) 만족도(satis)에 차이가 있는지 검정하시오.
# (일원배치 분산분석 : 모수 검정)    

# 단계1 : dataset 생성 
#20대 만족도(10점 만족)
age20 <- rep(20, 10)
satis20 <- c(5,7,10,6,8,3,9,5,6,5)
df1 <- data.frame(age=age20, satis=satis20)

#30대 만족도
age30 <- rep(30, 10)
satis30 <- c(8,7,10,6,8,5,9,7,6,6)
df2 <- data.frame(age=age30, satis=satis30)

#40대 만족도
age40 <- rep(40, 10)
satis40 <- c(8,9,10,6,8,7,9,7,9,8)
df3 <- data.frame(age=age40, satis=satis40)

# DataFrame 생성 
datas <- rbind(df1, df2, df3)
datas # age satis
str(datas)

# 독립변수 요인형 변환 : 집단변수 생성(숫자변수 : 사후검정 시 오류) 
datas$age <- as.factor(datas$age)
str(datas) # $ age  : Factor w/ 3 levels


# 단계2 : 등분산성 검정 : 연령에 따른 만족도의 분산 차이  
bartlett.test(satis~age,data=datas) # p-value = 0.2494 > 0.05: 기본 가정 채택

# 단계3 : 분산분석 
result=aov(satis~age,data=datas)

# 단계4. 분석분석 결과 해석 
summary(result) # p-value = 0.0922 > 0.05: 귀무가설 채택 -> 차이 없음

# 단계5. 사후검정 : 각 집단간 차이검정 
TukeyHSD(result)
#        diff        lwr      upr     p adj
# 30-20  0.8 -1.0468164 2.646816 0.5379671 
# 40-20  1.7 -0.1468164 3.546816 0.0756158
# 40-30  0.9 -0.9468164 2.746816 0.4586358
# 모든 집단 간의 평균 차이 없음
plot(TukeyHSD(result))

# 04.airquality를 대상으로 월별(Month)로 오존량(Ozone)에 차이가 있는지 검정하시오.
# (일원배치 분산분석 : 비모수 검정)  

airquality
str(airquality)
# $ Ozone -> y : 연속형 변수 
# $ Month -> x : 집단변수 
table(airquality$Month) # 5  6  7  8  9

# 단계 1: 전처리(결측치 제거)
summary(airquality) # 결측치 발견 
dataset <- na.omit(airquality) # 결측치 제거 

dataset$Month=as.factor(dataset$Month)
str(dataset) # Factor w/ 5 levels
str(airquality)

# 단계 2: 등분산성 검정 
bartlett.test(Ozone~Month,data=dataset) # p-value = 0.007395 < 0.05: 기본 가정 기각


# 단계 3: 분산분석(모수 vs 비모수) & 해석

kruskal.test(Ozone~Month,data=dataset) # p-value = 2.742e-05 < 0.05: 귀무가설 기각

# 단계 4: 사후검정 : 집단별 평균(dplyr 패키지 이용)
dataset %>% group_by(Month) %>% summarize(avg = mean(Ozone))

plot(Ozone~Month,data=dataset)