# -*- coding: utf-8 -*-
"""
step04_func_args.py

함수의 가변인수 
 - 한 개 가인수로 여러 개의 실인수를 받는 인수
"""

# 1. tuple형 가변인수 
def func1(name, *names) : # 패킹 할당: *가인수 =  가변인수
    print(name) # 홍길동
    print(names) # ('이순신', '유관순')

func1("홍길동", "이순신", "유관순")
func1("홍길동", "이순신")

# 2. dict형 가변인수 
def person(w, h, **other) :
    print('몸무게 :', w)
    print('키 : ', h)
    print('기타 : ', other) # {'name': '홍길동', 'addr': '서울시'}

person(65, 175, name='홍길동', addr = '서울시')


# 3. 함수를 인수로 넘기기  
def square(x) : # x^2
    return x**2

def my_func(func, datas) : # (함수, 데이터셋)
    re = []
    for x in datas :
        re.append(func(x)) # square(x)
    return re    
datas=[2,4,6]
my_func(square,datas) # [4, 16, 36]
