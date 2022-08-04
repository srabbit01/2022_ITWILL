#################################
## <제1장 연습문제>
#################################

#01. 다음 조건에 맞게 name, age, address 변수를 생성하고 출력하시오.

#조건1) name, age, address 변수에 자신의 이름, 나이, 주소를 만들고 출력한다. 
name = "한수정"
age = 25
address = "경기도 수원시 이의동"

#조건2) mode() 함수를 이용하여 각 변수의 자료형(data type)을 확인한다.
mode(name)
mode(age)
mode(address)

#02. 다음 rain 변수는 비 유무를 나타내는 변수이다. 이 변수를 요인형(Factor)으로 변경하시오.  
rain <- c('YES', 'NO', 'YES', 'YES', 'NO')
mode(rain) # character
frain = factor(rain,levels=c('YES','NO'))
frain # Levels: YES(1)=0, NO(2)=1
mode(frain) # numeric
plot(frain)

#03. R에서 제공하는 c()함수를 이용하여 다음과 같이 변수를 만들고, 자료를 처리하시오.

#조건1) 2,4,6,8,10의 자료를 num 변수로 만든다.
num = c(2,4,6,8,10)

#조건2) num 변수를 대상으로 평균을 구한다.(힌트 : 평균 함수 이용)
mean(num)

#04. R에서 제공하는 women 데이터 셋을 이용하여 다음 조건에 맞게 처리하시오.

#조건1) women은 어떤 데이터 셋 인지를 쓰시오?
data(women)
women # 여성의 키 별로 몸무게를 나타내는 데이터셋

#조건2) women 데이터 셋의 자료형은 무엇인가?
mode(women) # list

#조건3) plot() 함수를 이용하여 차트 그리기
plot(women) # (x,y)

#05. 현재 작업 공간을 확인하고 "C:/ITWILL/2_Rwork/output"로 변경하시오.
getwd()
setwd("E:/03. R/output")

#06. R 프로그래밍 언어의 특징에서 in memory computing에 대해서 설명하시오.
# 데이터를 메모리에 로딩해 두고 작업하는 방식 -> 속도가 빠름
