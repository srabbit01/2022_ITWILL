'''
step03_print_input.py
1. print(): 표준 출력 장치 (=모니터=콘솔) 결과 출력
2. input(): 
'''

# 1. print()(기본 내장 함수)
# - 콘솔 출력 함수 
help(print) # 함수 도움말
# Help on built-in function print in module builtins:
# built-in function: 내장함수 의미
# print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False): 입력 가능 인수

# 1) 기본 인수 
print("value =",10,10+20)  # value, value, value
print('010','1234','1111', sep='-') # 010-1234-1111 
print('010','1234','1111', sep='*') # 010*1234*1111

# end 속성: 같은 줄에 중복 출력
print('value =', 10, end=',' )
print('value =', 20) # value = 10,value = 20 -> 같은 줄에 중복 출력

# 2) % 양식문자 
# 형식) print('%양식문자' %값) - ppt.23

num1 = 10; num2 = 20
tot = num1 + num2 
print('%d + %d = %d' %(num1, num2, tot))  # 10 + 20 = 30

print('이름은 %s이고, 나이는 %d 이다.' %('홍길동', 35))

print('원주율 = %8.3f' %(3.14159)) # 원주율 =    3.142: 전체 및 소숫점 이하 지정
print('원주율 = %f' %(3.14159)) # 원주율 = 3.142: 모두 지정 x
print('원주율 = %.3f' %(3.14159)) # 원주율 = 3.142: 전체 지정 x, 소숫점 이하만 지정

print('전체 찬성률은 %d%%이다.'%50) # 50%: 특수문자(%) 사용 = %%


# 3) format()함수 이용 

# 형식1) print('{형식}'.format(값))
print('이름은 {}이고, 나이는 {}이다.'.format('홍길동', 35)) # 이름은 홍길동이고, 나이는 35이다.

# '{위치:형식}'
print('정수형 = {0}, {1:5d}, 연봉 : {2:3,d}'.format(123, 1234, 2500)) # 정수형 = 123,  1234, 연봉 : 2,500

print('원주율 = {0:.3f}, {1:8.3f}'.format(3.14159, 3.14159))


# 형식2) format(값, '양식')
print('원주율 = ', format(3.14159, '5.3f'))
print('금액 = ', format(5432000,'3,d')) # 금액 =  5,432,000

# 축약형 format: SQL문
name='홍길동'; age=35
sql=f"select * from emp where name = {name} and age={age}"
sql2="select * from emp where name = {} and age={}".format(name,age)
print(sql) # select * from emp where name = 홍길동 and age=35
print(sql2) # select * from emp where name = 홍길동 and age=35

print(f"select * from emp where name = {name} and age={35}")

# 2. input()
# - 키보드로 입력받는 함수 

# 키보드 입력 -> 정수형 변환 
a = int(input('첫번째 숫자 입력 : ')) # 10
b = int(input('두번째 숫자 입력 : ')) # 20

c = a + b
print('c=', c) # c= 30

# 키보드(문자) -> 실수형 변환  
x = float(input('첫번째 실수 입력 : '))
y = float(input('두번째 실수 입력 : '))
z = x + y
print('z=', z) 

# 3. 자료형 변환 (casting)
print(int(24.564)) # 24: 실수 -> 정수 변환
print(float(123)) # 123.0: 정수 -> 실수 변환

int('2345') # 정수 변환 가능 문자
# int('hello') # error 정수 변환 불가능 문자

# print(2+'2') # error: 숫자+'문자'
print(2+int('2')) # 숫자+숫자

# print('나이:'+35) # error: '문자열'+정수
print('나이:'+str(35))

# 논리형(bollean): TRUE/FALSE -> 정수형
int(True) # TRUE = 1
int(False) # FALSE = 0

# 정수형 -> 논리형 변환
bool(1.3423) # TRUE
bool(0) # FALSE