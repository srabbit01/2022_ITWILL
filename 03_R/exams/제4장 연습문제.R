#################################
## <제4장 연습문제>
#################################   
# 01. 다음 3개의 vector 데이터를 이용하여 client 데이터프레임을 
# 생성하고, 조건에 맞게 처리하시오.

# vector 준비 
name <-c("유관순","홍길동","이순신","신사임당")
gender <- c("F","M","M","F")
price <-c(50,65,45,75)

# 데이터프레임 생성 
client <- data.frame(name, gender, price)
client

# <단계1> price가 65만원 이상인 고객은 "Best" 미만이면 
#     "Normal" 문자열을 result 변수에 넣고, client의 객체에 컬럼으로 추가하기
# 힌트 : ifelse() 함수 이용 
client$result = ifelse(price>=65,"Best","Normal") # 위 price 벡터 변수 사용 의미 (price 벡터 존재 경우)
client$result = ifelse(client$price>=65,"Best","Normal") # 데이터프레임 client의 price 컬럼 사용 의미
# 결과는 같으나 사용하는 데이터 구조 다름
client

# <단계2> client의 result 변수에 대한 빈도수를 구하시오. 힌트) table()함수 이용
table(client$result)

# <단계3> gender가 'M'이면 "Male", 'F'이면 "Female" 형식으로 client의 객체에
#  gender2 컬럼을 추가하고 빈도수 구하기 # 힌트 : ifelse() 함수 이용 
client$gender2 = ifelse(gender=="M","Male","Female")
table(client$gender2)

# 02. 다음 벡터(EMP)는 '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
# 이 벡터 데이터를 이용하여 다음과 같은 출력결과가 나타나도록 함수를 정의하시오. 

# <Vector 준비>
EMP <- c("2014홍길동220", "2020이순신300", "2010유관순260")

# <단계1> EMP 변수의 전체 원소를 줄 단위로 출력하기(힌트 : for함수 이용)
for(i in EMP){
  print(i)
}

# <단계2> 다음 <출력 결과>과 나타나도록 emp_pay 함수 완성하기(힌트 : stringr 패키지의 함수 이용) 

#  <출력 결과>
# 전체 급여 평균 : 260

# 힌트) 
# stringr 패키지 : str_extract(string, '패턴')함수 
# 숫자변환 함수 : as.numeric()함수
# 평균함수 : mean()함수
str_extract(EMP,'\\d{3,}$')

emp_pay <- function(x){
  library(stringr) # stringr 패키지 인메모리로 로딩
  pay = str_extract(x,'\\d{3}$') # 문자열 접미어 3개 출력
  pay = as.numeric(pay)
  avg_pay = mean(pay)
  cat('전체 급여 평균:',avg_pay)
}

# 함수 호출 
emp_pay(EMP)


# 03. 정규분포(평균=5, 표준편차=2)를 따르는 난수 10개를 생성한 후 정수 반올림한 결과가 짝수인 경우만
# 벡터 변수에 저장하고, 출력하시오.
vec_num = c()
runnum = runif(10,min=0,max=10)
runnum
runnum_int = round(runnum)
runnum_int
for(i in runnum_int){
  if(i%%2==0){
    vec_num = c(vec_num,i)
  }
}
vec_num

# <출력결과 예>
# 난수 : 0.3525728 5.7390681 8.5128361 9.4952819 2.5950957 4.7318683 4.3414820 3.2547769 4.8177737 6.6418599
# 정수 반올림한 짝수 : 0.3525728 5.7390681 4.3414820







