# chap02_DataStructure

### 제 2장. 자료구조의 유형

# 1. Vector
# - 동일한 자료형을 갖는 1차원 배열 구조
# - 생성 함수: c(), seq(), rep()
# ** c: combine, seq: sequence 순서, rep: replicate 반복

# 1) c(값1,값2,...)
var1 = c(23,-12,10:20) # 10:20은 10부터 20까지 정수 출력 의미미
var1
length(var1) # 13
mode(var) # numeric
sum(var) # 숫자형인 경우, 합계 출력: 176

# 원소 이름 지정
ages = c(35,45,25)
ages
names(ages) = c('홍길동','이순신','유관순') # 실제 자료는 아니고 원소들의 이름
ages
mean(ages) # 35

words = names(ages) # 원소 이름들만 추출 가능
words

# 2) seq(from=시작숫자,to=끝숫자,by=증가율) # 등호 안 넣어도 동일: seq(시작숫자,끝숫자,증가율)
var2 = seq(from=1,to=100,by=2)
var2

var2 = seq(from=100,to=1,by=-2) # 감소형으로 추출 가능

# 3) rep(변수,times=전체반복횟수,each=개별반복횟수)
var3=rep(1:3,times=3)
var3 # 1 2 3 1 2 3 1 2 3

var3 = rep(1:3,each=3)
var3 # 1 1 1 2 2 2 3 3 3
var3 = rep(1:3,3,each=3)
var3

# 4) 복합 출력
rep(seq(1,10,2),times=2)

# 5) 자료 일부 추출(참조)
# (1) 색인 이용
# 색인(index): 값의 위치
# 형식: 변수[n]
# 색인의 시작은 '1'
a = 1:50 # c(1:50)
a
# 색인은 대괄호로 표현하며, 값의 위치 의미
# 색인을 이용하여, 특정 원소만 추출 가능
a[10] # 10번째 원소 출력 # 10
a[10:20] # 연속된 여러 원소 출력
a[c(5,10,15,20,25)] # 연속되지 않는 여러 원소 출력
a[-c(5,15,35)] # 대부분 선택하고 일부 원소만 제외하고자 할 때

# (2) 함수 이용
# 연속되지 않는 여러 원소들을 많이 선택하는 경우
length(a)
a[seq(2,length(a),2)] # 짝수만 출력

# (3) 조건식 이용
a[a>=10] # a[a 비교연산자 숫자]
a[a>=10 & a<=30] # 논리연산자 사용: a>=10 and a<=30
a[a>=10 | a<=30] # 논리연산자 사용: a>=10 or a<=30
a[!(a>=10)] # 논리연산자 사용: not(a>=10)


# 2. Matrix
# - 동일 데이터형을 갖는 2차원 배열
# - 생성 함수: matrix(), rbind(), cbind()
# - 처리함수: apply()

# 1) matrix(변수,nrow=행개수,ncol=열개수,byrow=FALSE,dimnames=NULL) # byrow: TRUE = 행방향 출력, dimnames: 열이름 지정
mat1 = matrix(1:5,nrow=1,ncol=5)
mat1
dim(mat1) # 행 열 개수 반환 (자료구조 모양: shape)

mat2 = matrix(1:9,nrow=3,ncol=3,byrow=TRUE)
mat2

# mode vs class
mode(mat2) # numeric
class(mat2) # 객체의 출처 (클래스): 자료 구조 (자료 모양) # "matrix" "array" 

# 2) rbind(): 행단위 묶음
v1 = 1:5
v2 = 6:10

mat3 = rbind(v1,v2) 
mat3

# 3) cbind: 열단위 묶음
mat4 = cbind(v1,v2)
mat4

# 4) Matrix 색인
# 형식) 변수[row,col] = 변수[행,열]
mat4[1,] # 1행 전체 참조
mat4[,1] # 1열 전체 참조
mat4[3,2] # 행,열의 값 한개 참조
mat4[2:4,] # 연속된 행 참조
mat4[c(2,4),] # 비연속 행 참조
mat4[-3,] # 특정 행 외 참조

# ADsP
xy = rbind(v1,v2)
xy
dim(xy)
# 보기1: xy[1,]는 v1과 같다.(ㅇ)
# 보기2: xy[,1]는 v2와 같다.(x)
# 보기3: xy는 2x5 행렬구조이다.(ㅇ)
# 보기4: 자료구조는 matrix이다.(ㅇ)

# 5) apply(변수,마진:행/열,Func)
# 행렬 데이터 구조를 이용하여 행/열 기준으로 통계 함수 결과 출력
# 행렬: 행=1, 열=2
# 마진 당 반드시 하나의 결과 출력
mat4
apply(mat4,1,mean) # 행 단위 평균
apply(mat4,1,sum) # 행 단위 합계
apply(mat4,2,mean) # 열 단위 평균
apply(mat4,2,sum) # 열 단위 합계


# 3. Array
# - 동일 데이터형을 갖는 3차 배열
# - 생성 함수: array()

# 1) array(변수,dim) # dim: 각 축의 길이, dinames: 각 x,y,z 축의 이름
data = 1:12
arr = array(data,c(3,2,2))
arr

# 2) array 색인
# 형식) 변수[행,열,면]
arr[,,1] # 1면만 참조
arr[,,2] # 2면만 참조조
arr[2:3,,2] # 2면 중 2행 3행 출력


# 4. DataFrame
# - 서로 다른 자료형을 갖는 열(칼럼), 2차원 배열
# - Matrix와의 공통점은 2차원이나, Matrix는 모두 동알힌 자료형을 가져야 하나 DataFrame은 열 별로 달라도 됨
# - 생성 함수: data.frame()
# - 처리 함수: apply()
# - 목적: 칼럼 단위로 출력

# 1) data.frame(변수)
#(1) Vector 생성
eno = 1:3
ename = c('hong','lee','yoo')
age = c(35,45,25)
pay = c(250,350,200)
# (2) DataFrame 생성
emp = data.frame(NO=eno,NAME=ename,AGE=age,PAY=pay)
emp

str(emp) # 각 칼럼의 이름, 자료형, 데이터 등 확인
# 'data.frame':	3 obs.(관측치=행개수) of  4 variables(변수=열개수):
# $ NO  : int  1 2 3 -> 이산형
# $ NAME: chr  "hong" "lee" "yoo" -> 문자형
# $ AGE : num  35 45 25 -> 연속형
# $ PAY : num  250 350 200 -> 연속형

# 2) 자료 참조

# (1) object$칼럼명 -> object: 객체/변수 (색인보다 더 많이 사용)
pay = emp$PAY
pay # 열 참조
mean(pay) # 266.6667
sum(pay) # 800

# (2) 색인 참조: 변수[행,열]
emp[2,] # 2행 전체 참조
emp[,2] # 2열 전체 참조

# 3) 자료 처리: apply()
x1 = 1:5
x2 = 6:10
x3 =c("hello","hi")
df = data.frame(x1,x2,x3)
df
apply(df,1,sum) # 행 단위 압압
apply(df,2,sum) # 열 단위 합
# 문자가 존재하면 Error 발생: 컬럼지정


# 5. List
# - 서로 다른 자료형과 서로 다른 자료 구조 저장
# - 생성 함수: list(key1=value,key2=value,...) # 하나의 요소(원소)에 한쌍의 키와 값 존재
# - 벡터 비교: c(값1,값2,...) # 하나의 요소에 값만 존재
# - 주의: key 값은 절대 중복될 수 없음
# - 색인이 아닌, key를 이용하여 value 참조
# - 처리 함수: unlist, do.call,lapply, sapply

# 1) list(key=value)
member1 = list(name="홍길동",
               age=30,
               address="한양시",
               gender="남자")
member1

# 2) key -> value 참조
# object$key
member1$age # 35
member1$address # "한양시"

# name         -> $key
# [1] "홍길동" -> value

# 2) list(value): key 생략 -> 기본 key 제공
member2 = list("홍길동",35,"한양시","남자자")
member2
# [[1]] -> 기본키: [[n]] 중복되면 안되기 때문에 인덱스값이 기본키가 됨
# [1] "홍길동" -> value
member2[[3]] # "한양시"

# 3) list(key=[value1,value2,...]): key 안에 여러값 저장
member3 = list(names=c('홍길동','유관순'),
               ages=c(30,25),
               gender=c("남자","여자"))
member3
# $names
# [1] "홍길동" "유관순"
member3$names # names 키에 저장된 값 참조
member3$names[2] # names 키에 저장된 일부 자료값

# 4) 다양한 자료구조(vector,matrix,array 등)
lst_var = list(one=c('하나','둘','셋'),
               two=matrix(1:9,nrow=3),
               three=array(1:12,c(3,2,2)),
               four=data.frame(1:5,6:10))
lst_var

lst_var$one # 백터 형식: 1차원 배열
lst_var$two # 행렬 형식: 2차원 배열
lst_var$three # 배열 형식: 3차원 배열
lst_var$four # 데이터프레임 형식: 4차원 배열

# 5) list 처리 함수: unlist, do.call,lapply, sapply

# (1) unlist: list -> vector 변환
# 간혹 값 참조가 번거로운 경우, 벡터로 전환하여 저장
x = list(1:10,11:20)
x
# [[1]] -> key
# [1]  1  2  3  4  5  6  7  8  9 10 -> value
x[[1]] # 자료값 출력 시, 변수[[인덱스]][키인덱스]로 번거롭기에
x[[1]][6] # list에서 원소 참조

v = unlist(x) # 키(key) 제거
v
v[6] # vector에서 원소 참조

# (2) do.call(함수,변수): 함수 호출 후 변수에 적용
# 변수는 리스트 뿐만 아니라 다른 리스트도 사용 가능
multi_list = list(r1=list(1,2,3),
                  r2=list(10,20,30),
                  r3=list(100,200,300))
multi_list

# list -> matrix 변환
mat = do.call(rbind,multi_list) # r1, r2, r3를 각각 행 단위로 변형
mat # 기본함수


# (3) lapply, sapply: list 자료 처리
a = list(1:5)
# [[1]]
# [1] 1 2 3 4 5
b = list(6:10)
# [[1]]
# [1]  6  7  8  9 10

## lapply(x,함수명): list 반환 (키와 값 반환)
lapply(c(a,b),max) # 각 리스트의 최대값 반환
# [[1]] -> a
# [1] 5
# [[2]] -> b
# [1] 10

## sapply(x,함수명): vector 반환 (값만 반환)
sapply(c(a,b),max)
# [1]  5 10 -> a b


# 6. Subset 만들기
# - 데이터프레임을 대상으로 특정 열 또는 행만 선택하여 만든 새 데이터프레임
x = 1:5
y = 6:10
z = letters[1:5] # n개의 영문자 소문자 추출
df = data.frame(x,y,z, stringsAsFactors=FALSE)
# stringAsFactors=TRUE: 문자형을 요인형으로 변경
# stringAsFactors=FALSE: 문자형을 요인형으로 변경 X (기본)
df

str(df)
help(subset) # x에 대상 객체를 넣고, select: 조건식(사용할 컬럼 지정), drop=FALE,...
# subset(x, subset, select, drop = FALSE, ...)

# 1) 조건식으로 subset 만들기: 행 기준
new_df = subset(df,subset=y>=8) # subset=조건식
new_df

# 2) 조건식으로 subset 만들기: 열(칼럼) 기준
new_df2 = subset(df,select=c(x,z)) # select=c(칼럼1,칼럼2)
new_df2

# 3) 특정 자료값으로 subset 만들기: 칼럼명 %in% c(list) 
new_df3 = subset(df,z %in% c('a','c','e')) # 특정 자료값을 가진 행 전체 반환
new_df3

# example: iris dataset
data('iris') # iris 데이터 메모리로 로딩
iris
str(iris)
# 'data.frame':	150 obs. of  5 variables:
# $ Sepal.Length: num  5.1 4.9 4.7 4.6 5 5.4 4.6 5 4.4 4.9 ... # 꽃받침 길이
# $ Sepal.Width : num  3.5 3 3.2 3.1 3.6 3.9 3.4 3.4 2.9 3.1 ... # 꽃받침 너비
# $ Petal.Length: num  1.4 1.4 1.3 1.5 1.4 1.7 1.4 1.5 1.4 1.5 ... # 꽃잎 길이
# $ Petal.Width : num  0.2 0.2 0.2 0.2 0.2 0.4 0.3 0.2 0.2 0.1 ... # 꽃잎 너비
# $ Species     : Factor w/ 3 levels "setosa","versicolor",..: 1 1 1 1 1 1 1 1 1 1 ... # 꽃의 종

# 예1) 1, 3, 5번 칼럼 선택: iris_df
iris_df = subset(iris,select=c(Sepal.Length,Petal.Length,Species))
str(iris_df)

# 예2) 예1의 결과에서 2번 컬럼의 평균값 이상 값 선택: iris_df2
mean(iris_df$Petal.Length) # 3.758
iris_df2 = subset(iris_df,subset = Petal.Length >= mean(iris_df$Petal.Length))
str(iris_df2)
# 'data.frame':	93 obs. of  3 variables:

# 예3) 예1의 결과에서 Species 칼럼을 대상으로 "setosa" 꽃의 종 선택: iris_df3
iris_df3 = subset(iris_df,Species %in% "setosa")
str(iris_df3)
# 'data.frame':	50 obs. of  3 variables: