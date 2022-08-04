#################################
## <제2장 연습문제>
#################################

# 01. 다음과 같은 벡터 객체를 생성하시오.

#1) Vec1 벡터 변수를 만들고, 1~5까지 연속된 정수를 만드시오. - c()함수 이용 
vec1 = c(1:5)
vec1

#2) Vec2 벡터 변수에 1~10까지 3간격으로 연속된 정수를 만드시오. - seq()함수 이용 
vec2 = seq(1,10,3)
vec2

#3) Vec3 벡터 변수에 "R" 문자가 5회 반복되도록 하시오. - rep()함수 이용 
vec3 = rep('R',5)
vec3

#4) Vec4에는 Vec1~Vec2가 모두 포함되는 벡터를 만드시오. - c()함수 이용 
vec4 = c(vec1,vec2)
vec4

#5) 25~ -15까지 5간격으로 벡터 생성 - seq()함수 이용 
seq(25,-15,-5)

#6) Vec4에서 홀수번째 값들만 선택하여 Vec5에 할당하시오. - 색인 이용
vec5 = vec4[seq(1,length(vec4),2)]
vec5

# 02. 다음 두 개의 벡터를 이용하여 단계별로 처리하시오. 
v1 <- c(2,3,10,-5,8)
v2 <- c(40,50,-30,7,10)

# 단계1> 행 단위로 묶어서 matrix 생성하기  
rm = rbind(v1,v2)
rm

# 단계2> matrix 차원 보기 
dim(rm)

# 단계3> matrix 열 단위 합계 계산하기 
apply(rm,2,sum)

# 03. 다음과 같은 벡터를 칼럼으로 갖는 DataFrame을 생성하시오.
name <-c("최민수","유관순", "이순신","김유신","홍길동")
age <-c(55,45,45,53,15) #연령
gender <-c(1,2,1,1,1) #1:남자, 2: 여자
job <-c("연예인","주부","군인","직장인","학생")
sat <-c(3,4,2,5,5) # 만족도
grade <- c("C","C","A","D","A")
total <-c(44.4,28.5,43.5,NA,27.1) #총구매금액(NA:결측치)

# <조건1> 위 7개 벡터를 user이름으로 데이터프레임 만들기 
user  = data.frame(NAME=name,AGE=age,GENDER=gender,JOB=job,SAT=sat,GRADE=grade,TOTAL=total)
user
str(user)

# <조건2> 총구매금액(total) 변수를 이용하여 히스토그램 그리기-hist()
hist(user$TOTAL)

# <조건3> 만족도(sat) 변수를 이용하여 산점도 그리기-plot()
plot(user$SAT)
data.fra

# 04. Data를 대상으로 apply()를 적용하여 행/열 방향으로 조건에 맞게 통계량을 구하시오.
kor <- c(90,85,90)
eng <- c(70,85,75)
mat <- c(86,92,88)    

# 조건1) 3개의 과목점수를 이용하여 데이터프레임(Data)을 생성한다. 
score = data.frame(KOREAN=kor,ENGLISH=eng,MATH=mat)
score

# 조건2) 행/열 방향으로 max()함수를 적용하여 최댓값 구하기
apply(score,1,max) # 개인의 최고 점수
apply(score,2,max) # 과목별 최고 점수

# 조건3) 행/열 방향으로 mean()함수를 적용하여 평균 구하기(소숫점 2자리 까지 표현)
#  힌트 : round(data, 자릿수)
round(apply(score,1,mean),2)
round(apply(score,2,mean),2)

# 조건4) 행 단위 분산과 표준편차 구하기  
#  힌트 : var(), sd()
apply(score,1,var)
apply(score,1,sd)

# 05. R에서 제공하는 CO2 데이터셋을 대상으로 다음과 같이 서브셋을 만드시오.
# 힌트 : subset() 함수 이용 

data("CO2") # 데이터셋 메모리 로딩 
print(CO2) # 데이터셋 보기 
str(CO2) # 데이터셋 구조 보기 

# 단계1) Treatment 칼럼 값이 'nonchilled'인 자료만 df1로  만들기 
df1 = subset(CO2,Treatment %in% "nonchilled")
df1
str(df1)

# 단계2) Treatment 칼럼 값이 'chilled'인 자료만 df2로 만들기 
df2 = subset(CO2,Treatment %in% "chilled")
df2
str(df2)

# 단계3) Plant, Type, conc 칼럼을 대상으로 df3로 만들기  
df3 = subset(CO2,select=c(Plant, Type, conc))
df3
str(df3)