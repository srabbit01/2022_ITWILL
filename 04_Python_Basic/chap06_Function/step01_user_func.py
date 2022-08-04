# -*- coding: utf-8 -*-
"""
chap06_Function > step01_user_func.py

1. 함수(function)
 - 중복 코드 제거 
 - 재사용
 - 기능 정의

2. 사용자정의함수  
 형식)
 def 함수명([인수]) :
     실행문
     실행문
     [return 값]
"""

# 1. 인수가 없는 함수 
def userFunc1() :
    print('userFunc1')
    print('인수가 없는 함수')


# 2. 인수가 있는 함수 
def userFunc2(x, y) :
    z = x + y
    print('z=', z)

# 3. return 있는 함수 
def userFunc3(x, y) :
    add = x + y
    sub = x - y     
    mul = x * y
    div = x / y
    return add, sub, mul, div # 여러개 값 반환 

# 함수 호출
userFunc1()
userFunc2(1,2)
re=userFunc3(1,2) 
re # (3, -1, 2, 0.5)
type(re)

a, b, c, d = userFunc3(400,35) 
print(a,b,c,d)
# 435 365 14000 11.428571428571429

# 2차 방정식 예
def fx(x): # x변수
    y = 2*x + 3 # 1차 방정식: x^1 = a*x + b (직선)
    # y = 2*x**2 + 3*x + 2 # 2차 방정식: x^2 = a^2*x + bx + c (곡선)
    return y

fx(1) # 5
fx(2) # 7
fx(3) # 9

import matplotlib.pyplot as plt # as 별칭
# 패키지 내 모듈 불러오기

x=list(range(1,11)) # 1~10
print(x) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list 내포
y = [fx(i) for i in x]
print(y) # [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]

plt.plot(x,y) # 선형 그래프 생성
plt.show() # 그래프 보여주기



