# chaop01_ Basic

# 1. 패키지와 세션 보기
dim(available.packages())
# 세션(session): R 작업환경
sessionInfo()
# R version, OS, 다국어(locale), base package(7개)

# 주요 단축키
# 실행: Ctrl+Enter
# 자동완성: Ctrl+SpaceBar
# 주석: #
# 여러 줄 주석 처리: Ctrl+Shift+c (토굴)

# 2. 패키지 사용법
# 패키지 = 함수(알고리즘)+데이터

# 1) 패키지 설치: 주의 - 컴퓨터 이름이 한글인 경우 오류 발생
install.packages('stringr') # ('패키지명')
install.packages('plyr')
# 주의: 패키지는 R 공식 사이트에 명시된 패키지만 설치 가능
# 다운로드 및 설치 동시에 이루어짐

# 2) 설치된 패키지 경로
.libPaths()
## [1] "C:/Users/srabb/Documents/R/win-library/4.1": 사용자가 설치한 패키지 위치
## [2] "C:/Program Files/R/R-4.1.2/library": 30개의 기본 패키지 설치 위치
## 패키지 의존성: 해당 패키지와 관련이 있는 패키지 함께 설치

# 3) 패키지 실행
library(stringr)
library(help='plyr')
string = "홍길동35이순신45유관순25"
# stringr 패키지를 이용한, 문자열(string) 내 일부 추출
str_extract_all(string,"[0-9]{2}") # 숫자 2자 추출
str_extract_all(string,"[가-힣]{3}") # 한글 3자 추출출

# 4) 패키지 삭제: 물리적 폴더 삭제 가능
remove.packages('stringr')
remove.packages('plyr')

# 5) 설치된 패키지 검색
installed.packages()
# 설치된 패키지 이름만 추출
rownames(installed.packages())

# 3. 변수

# 1) 변수(참조변수): 자료(객체)가 저장된 메모리 주소 기억

# 2) 변수 작성 규칙
# - 시작 영문 또는 _
# - 두번째: 영문, 숫자, 특수문자(_, .) 혼용
# - 대소문자 구분: NUM, num 다름
# - 한글도 사용 가능하나, 깨짐 현상 발생 가능성이 있어 영어 사용 권장
# - 이미 정의된 패키지명, 함수명 등은 변수명으로 사용하지 X -> 덮어씌워서 제대로 함수 실행 되지 않을 수 있음
# 예) score, member.id, _kor
# - 특징: 가장 최근값으로 수정

kor <- 90
mat <- 85
tot <- kor+mat
avg <- tot/2
print(tot) # 175
print(avg) # 87.5

member.id <- 'hong'
member.pwd <- '1234'

NAMES <- c('홍길동','이순신','유관순')
print(NAMES) # "홍길동" "이순신" "유관순"
print(NAMES[2]) # "이순신"

# 4. 자료형(data type)
# - 숫자형, 문자형, 논리형(참/거짓), 기타형(NA, NAN) 등
int <- 100
string <- '우리나라 대한민국'
bool <- TRUE # False

int # print(int) # 직접 print()하지 않아도 출력 가능
int; string; bool # 세미콜론(;): 한 줄에 여러 변수 출력

# mode(변수) -> 특정 변수의 자료형 반환
mode(string) # character
mode(int) # numberic
mode(bool) # logical

# is.XXXX(변수) -> 해당 자료형 유무 (T/F)
is.numeric(int)
is.numeric(bool)
is.logical(bool)

score<-c(90,85,NA,75,68) # 5명 점수
score
length(score) # 5

in.na(score) # FALSE FALSE TRUE FALSE FALSE
# 3번 결측치

# 5. 자료형 변환 (casting)
# as.xxxx(변수)

# 1) 문자형 -> 숫자형
# 벡터의 경우, 반드시 문자형이 먼저 들어가 있으면 문자형으로 전부 변경
x <- c(10,20,30,'40')
mode(x)
# numeric -> character
x # "10" "20" "30" "40"
# 자료형이 모두 문자형으로 변환
barplot(x) # 문자이기 때문에 데이터 Error 발생
sum(x) # 통계 함수는 숫자형만 사용가능하기 때문에 Error

# 숫자형 변환은 숫자인 문자형만 변환 가능
num <- as.numeric(x)
mode(num) # numeric
barplot(num) # 숫자이기 떄문에 막대차트 그림

# 2) (중요) 요인형(Factor) 변환
# 범주형 변수 대상 -> 가짜(dummy) 변수 변환 = 명목상 숫자로 바꿈
# 왜? 기계학습에서 문자형 자료를 숫자형 자료로 변환하고자 할 때, 요인형 이용
# 문자형을 가짜의 숫자로 변환하는 것
# 예1) 회귀분석에서 독립변수(설명변수) 범주형 -> 0 or 1
# 설명변수: Female=0, Male=1
# 예2) 앙상블 모델에서 종속변수(반응변수) 범주형 -> 집단 분류
# 비유무: no=0, yes=1

# 범주형 변수
gender <- c("F","M","F","M","F") # 문자형이나, 집단으로 분류되는 것은 범주형 변수라 함
mode(gender) # character
plot(gender) # 문자형이기 때문에 Error

# [1] 요인형 변환
fgender <- as.factor(gender)
fgender
plot(fgender)
# Level이 결정: 문자 알파벳 우선순위에 따라 지정
# Level: F(1) M(2)
mode(fgender) # numeric -> F:0, M:1
class(fgender) # factor

# [2] levels 변경: base 변셩
mgender <- factor(x=gender,levels=c('M','F')) # 순서 변경
mgender
# Levels: M(1), F(2): M -> 0, F -> 1
plot(mgender)

# 3) 날짜형 변환
Sys.Date() # 시스템이 인식하고 있는 오늘 날짜 출력
Sys.time() # 날짜 + 시간 ## KST 대한민국 표준시간 의미
mode(Sys.Date())

today <- "2022-02-28 16:06:58" # 문자형 날짜짜
mode(today) # character

ctoday <- as.Date(today,"%Y-%m-%d %H:%M:%S") # as.Date(변수, 양식(포멧))
mode(ctoday) # numeric # 숫자형으로 변환
class(today) # Date # 출처 확인

# mode vs class
# mode(x): x에 대한 자료형 반환
# mode: 변수의 자료형 확인
# class(x): x에 대한 클래스(객체)의 출처(class) 반환
# class: 해당 변수가 어떤 class에 의해 만들어졌는지, 객체의 출처 확인

# 영어식 날짜(주식정보) -> 한국식 날짜
# 우리나라 날짜: Y년m월d일 # 영어식 날짜: d월영어식(m)월-y년
edate <- '26-Apr-21'
kdate <- as.Date(edate,'%d-%b-%y')
kdate # NA # 영어식 날짜 인식 X

# 다국어 정보 확인
Sys.getlocale() # LC_COLLATE=Korean_Korea.949

# 다국적 정보 수정: 영어권
Sys.setlocale(locale='English_USA')
kdate <- as.Date(edate,'%d-%b-%y')
kdate # 영어식 날짜 한국식 날짜로 변형 (영어 형식에서만 사용 가능)

# 다국적 정보 수정: 한국어권
Sys.setlocale(locale='Korean_Korea')

# 6. 기본함수 사용 & 작업공간

# 1) 기본함수: 7개의 기본 패키지에서 제공하는 함수
# -> 메모리에 올리지 않고 바로 사용
help(mean) # 평균 함수에 대한 도움말 확인
?mean # 도움말 확인인
args(mean) # 해당 함수에 사용 가능한 인수 확인
example(mean) # 해당 함수 사용에 대한 예시

x <- c(10,20,30) 
mean(x) # 10

# 만일 결측치 포함되어 있다면,
n <- c(10,20,30,NA)
mean(n) # 결측치가 있는 경우, 전부 결측치로 처리
# 결측치 지우고 계산하기
mean(n,na.rm=TRUE) # 결측치가 있으면, 제외하고 평균 구하기
# 기본값: na.rm=FALSE
# trim: 사용자가 정한 기준으로 절사 등

# 2) 기본 데이터셋
# 기본 데리터셋 확인
data() # R 스튜디오에서 기본적으로 제공하는 데이터 자료 목록
# In memory
data(Nile) # 데이터를 메모리로 로딩
Nile
mode(Nile) # 자료형: 숫자 (연산 가능)
plot(Nile)
mean(Nile) # 919.35: 100년치의 평균값 출력
sd(Nile) # 169.2275: 표준편차 확인

# 3) 작업 공간
# 작업 공간 확인
getwd() # 현재 작업 위치: D:/03. R

# 작업 위치 변경
setwd('D:/03. R/data') # 작업 경로 변경경
bmi <- read.csv('bmi.csv')
bmi
