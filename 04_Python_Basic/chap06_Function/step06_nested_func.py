# -*- coding: utf-8 -*-
"""
step06_nested_func.py

중첩함수(nested function)

형식)
def outer(인수) :
    명령문
    def inner(인수) :
        명령문
    return inner
"""

# 1. 중첩함수 예
def a() : # outer: 외부함수
    print('a 함수')
    
    def b() : # inner: 내부함수
        print('b 함수')
        
    return b # inner 함수 이름 반환 
# outer 함수 호출
b = a() # 외부함수 호출 -> b: 일급함수
# inner 함수 호출: inner함수는 정의되지 않았기 때문에 바로 호출 불가능
b() # b함수
# outer/inner함수 한 번에 호출
a()() # 외부함수 및 내부함수 호출

# 2. 중첩함수 응용 
'''
 - outer 함수 역할 : dataset 생성, inner 함수 포함 
 - inner 함수 역할 : dataset 조작 
'''
# 외부함수 내 여러 내부함수 존재
def outer_func(data) : # outer 함수 
    dataset = data # dataset 생성
    
    # inner 함수 
    def tot() : # 합계
        tot_val = sum(dataset)
        return tot_val

    def avg(tot_val) : # 평균 
        avg_val = tot_val / len(dataset)
        return avg_val        
    
    return tot, avg # inner 함수 반환: 반드싯 반환되어야 호출됨

data=list(range(1,101))
# outer 호출
tot, avg = outer_func(data)
# inner 호출
tot_val=tot() # total 함수 호출
avg_val=avg(tot()) # avg 함수 호출
print('tot = %d, avg = %.3f' %(tot_val,avg_val))
# tot = 5050, avg = 50.500

# 3. nonlocal 명령어 : 중첩함수 관련 명령어

def main_func(num) : # outer
    num_val = num # data 생성
    
    # inner 
    def get_func() : # 값 획득 : 획득자(getter) 
        return num_val  
    
    def set_func(value) : # 값 지정 : 지정자(setter) -> 수정 가능
        nonlocal num_val # outer 변수 지정
        # 지역변수 아님 -> 외부 함수에서도 사용 가능
        num_val = value # 외부함수에 수정한 값 저장
        
    return get_func, set_func

g, s = main_func(100)
print('num_val =', g()) # num_val = 100
s(1000) # setter를 이용하여 값 수정
print('new_num_val =',g()) # new_num_val = 1000

# 4. 함수 장식자: Tensorflow 2.0
'''
- 다른 함수의 시작과 종료 부분 장식(기능) 추가 기능
- 예: login -> 인증 -> logout (함수의 시작/종료 부분에 함수 추가 시 사용)
- 형식: @ = 함수 장식자 의미
    def 함수장식자명(대상함수명):
        def 내부함수명(인수,...):
            start 함수
            대상함수명(인수,...)
            end 함수
        return 내부함수명
- 함수 장식자 실행
    @함수장식자명 = 하나의 함수 -> 다른 함수 꾸밈
    def 대상함수명(인수,...): -> 적용 대상
        실행문
'''
# 함수 장식자 생성: 중첩 함수 이용
def hello_deco(func): # 인수 = 대상 함수 이름: 인수로 장식할 함수 지정
    def inner(name): # 인수 = 대상 함수 인수
        print('*'*6,'start','*'*6) # 함수 시작
        func(name) # 적용 대상(함수) 호출
        print('*'*7,'end','*'*7) # 함수 종료
        # inner함수의 반환 값 없음
    return inner # inner함수 결과 반환

# 적용 대상
@hello_deco
def hello(name):
    print('My name is %s' % name)

# 장식 대상 함수 호출
hello('Crystal') # my name is Crystal

'''
****** start ******
My name is Crystal
******* end *******
'''