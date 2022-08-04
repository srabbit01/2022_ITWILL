# chap04_1_Control

# 제어문에서 쓰이는 연산자
# SELECT * FROM table WHERE 조건식(산술,비교,논리연산자) 생각

# <실습> 산술연산자 
num1 <- 100 # 피연산자1
num2 <- 20  # 피연산자2
result <- num1 + num2 # 덧셈
result # 120
result <- num1 - num2 # 뺄셈
result # 80
result <- num1 * num2 # 곱셈
result # 2000
result <- num1 / num2 # 나눗셈
result # 5

result <- num1 %% num2 # 나머지 계산
result # 0

result <- num1^2 # 제곱 계산(num1 ** 2)
result # 10000
result <- num1^num2 # 100의 20승
result # 1e+40 -> 1 * 10의 40승과 동일한 결과


# <실습> 관계연산자 
# (1) 동등비교 
boolean <- num1 == num2 # 두 변수의 값이 같은지 비교
boolean # FALSE
boolean <- num1 != num2 # 두 변수의 값이 다른지 비교
boolean # TRUE
# 주의: 대입연산자: num1 = num2 (num2를 num1에 넣음)

# (2) 크기비교 
boolean <- num1 > num2 # num1값이 큰지 비교
boolean # TRUE
boolean <- num1 >= num2 # num1값이 크거나 같은지 비교 
boolean # TRUE
boolean <- num1 < num2 # num2 이 큰지 비교
boolean # FALSE
boolean <- num1 <= num2 # num2 이 크거나 같은지 비교
boolean # FALSE

# <실습> 논리연산자(and, or, not, xor)
logical <- num1 >= 50 & num2 <=10 # 두 관계식이 같은지 판단 
logical # FALSE
logical <- num1 >= 50 | num2 <=10 # 두 관계식 중 하나라도 같은지 판단
logical # TRUE

logical <- num1 >= 50 # 관계식 판단
logical # TRUE
logical <- !(num1 >= 50) # 괄호 안의 관계식 판단 결과에 대한 부정
logical # FALSE

x <- TRUE; y <- FALSE
xor(x,y) # [1] TRUE
x <- TRUE; y <- TRUE
xor(x,y) # FALSE


# 제어문 = 조건문 + 반복문
# 프로그램의 순서를 바꿔주는 역할


# 1. 조건문: if(조건식), ifelse(조건식), which(조건식)

# 1) if 조건문: TURE인 경우 if 블록 실행, FALSE인 경우 else 블록 실행

# if(조건식){
# 조건이 TRUE인 경우 실행문
# } else{
# 조건이 FALSE인 경우 실행문
# }

x = 5
y = 10
if(x>y){
  cat('x > \n') # 조건 참이면 출력
  print(x) # TRUE
} else{
  cat('x < y\n') # 조건이 거짓이면 출력
  print(y) # FALSE
}
# 결과를 화면에 출력하기 위해 print() 혹은 cat() 이용

# 학점 구하기
score = scan() # 점수 입력

# (1) 단일 선택 if문
if(score>=60){
  cat('합격:',score)
} else{
  cat('불합격:',score)
}
# {} 생략
if(score>=60)
  cat('합격:',score)
else
  cat('불합격:',score)


# (2) 다중 선택 if문
if(score>=90 & score<=100){
  cat('A학점:',score)
} else if(score>=80){
  cat('B학점:',score)
} else if(score>=70){
  cat('C학점:',score)
} else{
  cat('F학점:',score)
}

# 2) ifelse 조건문: 조건문+반복문
# vector 입력 (N) -> ifelse(조건식) -> vector 출력 (N)
# 벡터의 원소 크기만큼 자동으로 반복하여 T/F 여부 확인
# 벡터의 크기만큼 반복

# 합격 처리
score = c(75,85,NA,55,80,60)

# ifelse(조건식,TRUE,FALSE)
ifelse(score>=60,"합격","불합격")
# [1] "합격"     "합격"     NA         "불합격" "합격"     "합격"

# 결측치 처리: 0으로 대체
ifelse(is.na(score),0,score) # 0으로 대체
ifelse(is.na(score),mean(score,na.rm=TRUE),score) # 평균으로 대체

# 파일 자료 처리
getwd()
setwd('D:/03. R/data')
data = read.csv('excel.csv',header=T)
str(data) # 'data.frame':	402 obs. of  5 variables:

table(data$q3)
#   1   2   3   4   5 
#   3  74  72 176  77 

result = ifelse(data$q3>3,'큰값','작은값')
result
table(result)

# 데이터프레임 칼럼 추가
# 파생변수: 기존의 변수를 이용하여 새로운 변수 추가
data$result = result # 파생변수
str(result)


# 3) which(조건식)
# - 특정 값의 위치(Index)를 찾는 경우 이용

x = c(2,5,10:20,30:50)
length(x)
x

# which(변수 연산자 대상)
idx=which(x==33)
idx # 17 (숫자 33의 위치)

x[idx] # 33
# 여러 컬럼에서 해당 값의 행 위치 등 2차원의 행렬 구조에서 값을 찾는 기능

st = read.csv('student4.txt')
st

row_idx = which(st$이름=='park')
row_idx
st[row_idx,] # [행위치,열위치] 
# 'park'에 대한 정보 확인

# 문제) num 변수를 대상으로 짝수와 홀수 구분하기
num = c(35,46,80,90,25)
ifelse(num%%2==0,"짝수","홀수")


# 2. 반복문: for(변수 in 값), while(조건식)

# 1) for(변수 in 값)

num = 1:10
num

for(x in num){
  cat('x=',x,'\n') # '\n': 줄바꿈
  print(x^2)
}
# 특정 결과 벡터 구조로 저장
d = c() # 빈벡터 만들기: 반복문에서 이루어진 계산 결과 저장
for(x in num){
  cat('x=',x,'\n') # '\n': 줄바꿈
  d = c(d,x^2) # 벡터에 파생 결과 누적
}
cat('d =',d) # d = 1 4 9 16 25 36 49 64 81 100

# 초기값 만들기
even = 0 # 짝수의 합
odd = 0 # 홀수의 합

# 반복문 + 조건문
for(x in num){
  if(x%%2==0){
    cat(x,"= 짝수\n")
    even = even + x # 누적변수
  } else{
    cat(x,"= 홀수\n")
    odd = odd + x
  }
}
cat("짝수의 합:",even,", 홀수의 합:",odd) # 짝수의 합: 30 , 홀수의 합: 25

# 학생 관리
kor = c(65,89,96)
eng = c(69,95,80)
mat = c(55,80,76)
name = c('홍길동','이순신','유관순')

st = data.frame(name,kor,eng,mat)
st

# 새로운 컬럼: total과 mean 추가
# 총점(total) 계산 후 컬럼 추가
tot = st$kor + st$eng + st$mat
tot # 각 학생별 총점 출력
st$tot = tot # 컬럼 추가
st
# 평균(mean) 계산 + 컬럼 추가
st$avg = round(tot/3,2)
st

# 평균을 이용하여 학점 매기기: 학점(A,B,C,D,F)
# 학점(grade) 계산 후 컬럼 추가
grade = c() # 빈벡터: 학점 저장
for(x in st$avg){
  if(x>=90)
    grade=c(grade,"A")
  else if(x>=80)
    grade=c(grade,'B')
  else if(x>=70)
    grade=c(grade,'C')
  else if(x>=60)
    grade=c(grade,'D')
  else
    grade=c(garde,"F")
}
st$grade = grade # [1] "D" "B" "B"
st

# ifelse() 함수를 이용하여 결과 출력
# ifelse(조건식,참,거짓): 반복문 + 조건문
grade2 = ifelse(st$avg>=90,"A",
                ifelse(st$avg>=80,"B",
                       ifelse(st$avg>=70,"C",
                              ifelse(st$avg>=60,"D","F"))))
st$grade2 = grade2
st

# 2) while(조건식){반복문}

i = 0 # 초기변수
while(i<10){ # 조건이 거짓이면 더 이상 반복문 출력하지 않음
  i = i + 1 # 카운터 변수 # 특정 변수가 1씩 증가는 것
  cat('i=',i,'\n')
}
i # [1] 10

# 문제2) x의 각 변량에 5의 배수만 y에 저장하기
x = 1:1000
y = c() # 빈 벡터: 5의 배수 저장

# while문 사용
i = 0 # 색인 역할
while(i < length(x)){ # (i < 1000)
  i <- i + 1 # 카운터 변수 
  if(x[i] %% 5 == 0) # i를 색인으로 이용
    y <- c(y, x[i]) # 벡터 변수에 5의 배수 저장 
} 
cat('y 변수 :', y)
length(y) # 200개

# for문 사용
for(i in x){
  if(i%%5==0)
    y=c(y,i)
}
y
