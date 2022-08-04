# -*- coding: utf-8 -*-
"""
step05_lambda_scope.py

1. 축약함수(Lambda)
 - 한 줄 함수 
 형식) 변수 = lambda 인수 : 명령문(리턴값) 
 ex) lambda x, y : x + y

2. scope : 변수의 사용범위 
 - 전역변수 : 함수 외.내에서 사용 
 - 지역변수 : 함수에서 정의된 변수(매개변수) 
   -> 함수가 종료되면 자동 소멸된다.  
"""

# 1. 축약함수(Lambda)
def Adder(x, y) :
    add = x + y
    return add

print('add =',Adder(10, 30)) # add = 40



# 형식) 변수 = lambda 인수 : 명령문 or 리턴값 
Adder2 = lambda x, y : x + y

print('add =', Adder2(10, 30)) # add = 40

# 1) x변량에 제곱
datas=[2,4,5,7,9] # 실인수

sq = lambda datas: [d**2 for d in datas]

print('square =',sq(datas))
# square = [4, 16, 25, 49, 81]

# 2) 혈액형 더미변수: AB(1), A(0), B(0), C(0)
map_data={'AB':1,'A':0,'B':0,'O':0} # dict table
datas=['A','B','A','O','AB','B'] # list: real data
datas2=['A','B','AB','O','B','AB','O']

# lambda 함수 (중복 코드 해결) 및 list 내포 사용 
dum = lambda datas: [map_data[d] for d in datas] # 더미변수 리스트 함수 생성
dum(datas) # [0, 0, 0, 0, 1, 0]
dum(datas2) # [0, 0, 1, 0, 0, 1, 0]

# 2. scope : 변수의 사용범위 

# 전역변수 : 전 지역 사용 
# 지역변수 : 함수 내에서만 사용

x = 50 # 전역변수 

# 지역변수 : x
def local_func(x) :
    x += 50  # 지역변수
    print('local func(x) =', x) # Local func(x) = 100

# 함수 호출
local_func(x)
print('x =',x) # x = 50

# 전역변수 : x
def global_func() :
    global x 
    x += 50
    print('global_func(x) =', x)  

# 함수 호출
global_func()
print('x =',x) # x = 150


















