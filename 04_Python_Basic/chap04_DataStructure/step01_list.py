# -*- coding: utf-8 -*-
"""
chap04_DataStucture > step01_list.py

list 특징
- 1차원 배열 구조(vector)
형식) 변수 = [값1,값2,...]
- 다양한 자료형 저장 가능
- 순서 존재(색인 사용)
- 값 추가, 삽입, 수정, 삭제 가능
"""

# 1. 단일 list & 색인 
# lst=list([1,2,3,4,5]) # class -> list 객체 변환
lst = [1,2,3,4,5] # list() 생략 가능
print(lst) # [1, 2, 3, 4, 5]
len(lst) # 객체 길이: 5
type(lst) # list
print(type(lst)) # <class 'list'>
# type(): 객체의 출처 반환

# 색인(index) : 값의 위치
lst[:] # 전체 원소 
lst[0] # 첫번째 원소 
lst[-1] # 마지막 원소 

# list + for 이용 
for i in lst : 
    print(i, end = ' ') # 한 줄 중복 출력 
    print(lst[i-1]) # 수식의 색인: i = 1-0 -> list[0]

# range(start,stop,step)
x = list(range(1,101)) # 1~100의 list 객체
type(x) # list
print(x)

# 객체[start:stop-1]
print(x[:5]) # 앞부분 5개 확인 (처음부터 ~)
print(x[-5:]) # 뒷부분 5개 확인 (~ 마지막까지)

# 객체[start:stop:step]: step 생략 가능 (기본: 1씩 증가)
print(x[::2]) # 홀수 수열
print(x[1::2]) # 짝수 수열


# 2. 중첩 list & 색인 
y = [['a','b','c'], [1,2,3]] 
print(y) # [['a', 'b', 'c'], [1, 2, 3]]
len(y) # 2: 리스트 내 리스트의 개수 반환

print(y[0]) # ['a', 'b', 'c']
print(len(y[0])) # 3: 리스트 내 첫번째 리스트 요소 개수 반환
print(y[1]) # [1, 2, 3]

# 리스트 내 리스트의 요소 반환: 중첩 인덱스 지정
print(y[0][2]) # c
print(y[1][1]) # 2
print(y[1][1:]) # [2, 3] -> 2개 이상의 요소 반환 경우 리스트로 반환

# 3. 값 수정(추가, 삽입, 수정, 삭제)
num = ['one', 2, 'three', 4] # 다양한 자료형 가능
print(num) # ['one', 2, 'three', 4]
len(num) # 4

# object.method(): 객체의 메서드 사용

# 1) list 추가 
num.append('five') 
print(num) # ['one', 2, 'three', 4, 'five']

# 2) list 삭제 
num.remove('three')
print(num) # ['one', 2, 4, 'five']

# 3) list 수정 : 색인 이용 
num[1] = 'two' 
print(num) # ['one', 'two', 4, 'five']

# 4) list 삽입 
num.insert(0, 'zero')
print(num)


# 4. list 연산 
x = [1, 2, 3, 4]
y = [1.5, 2.5]

# 1) list 결합(+)
z = x + y # new object: 결합을 하여 새로운 객체 생성
print(z) # [1, 2, 3, 4, 1.5, 2.5]

# 2) list 확장 
x.extend(y) # old object: 단일 list
print(x) # [1, 2, 3, 4, 1.5, 2.5]

# 3) list 추가 
x.append(y) 
print(x) # [1, 2, 3, 4, 1.5, 2.5, [1.5, 2.5]]

# 4) list 반복(*)
result = y * 2
print(result) # [1.5, 2.5, 1.5, 2.5]
# y * 0.5: TypeError -> 반드시 정수만 가능

for el in y: # [1.5,2.5]
    el*0.5
    print(el*0.5)


# 5. list에서 원소 찾기 
'''
if '원소' in list :
    list에 '원소' 포함 
'''

num = [] # 빈 list : 숫자 저장 

# 임의 숫자 입력 
for i in range(5) : # 0~4
    num.append(int(input('값 입력: ')))


# 숫자 원소 찾기 
if int(input("숫자를 입력하시오. ")) in num :
    print('숫자 있음')
else :
    print('숫자 없음')

# 6. list 객체 메서드
# 매서드(method): 해당 객체의 자료를 조작하는 함수
# 형식.매서드()

import random # 난수 함수 제공 모듈
r=[] # 빈list: 난수 저장

# 난수 10개 생성
for i in range(10):
    r.append(random.randint(1,10)) # 1~10 난수 정수
print(r)
len(r)
type(r)

# 메서드 확인
dir(r)
'''
 'append', # 추가
 'clear', # 전부 삭제
 'copy', # 복사
 'count', # 특정 요소 개수 확인
 'extend', # 확장
 'index', # 위치 확인
 'insert', # 삽입
 'pop', # 제거(인덱스 기준)
 'remove', # 제거(요소 기준)
 'reverse', # 정렬 반대로
 'sort' # 정렬
'''
print(r) # [6, 2, 4, 3, 5, 8, 9, 4, 6, 9]

# 특정 요소 개수 반환
r.count(10) # 객체 개수 반환
r.count(2) # 객체 없는 경우 0 변환

# index에 값 반환&제거
r.pop(0)
print(r) # [2, 4, 3, 5, 8, 9, 4, 6, 9]

# 요소의 색인 반환
r.index(9) # 가장 앞의 색인 반환 (1개 반환)
r.index(1) # 요소가 없는 경우 ValueError 발생 

# 정렬
r.sort() # 오름차순: [2, 3, 4, 4, 5, 6, 8, 9, 9]
sorted(r)

r.sort(reverse=True) # 내림차순: [9, 9, 8, 6, 5, 4, 4, 3, 2]

r.reverse() # 현재 값의 역순으로 실행

# 복제(copy)
r2=r.copy()
r2 # 깊은 복사: 내용만 복사 -> 주소 복사 X
id(r) # 2579171405888
id(r2) # 2579171301952

r3=r
r3 # 얕은 복사: 주소만 복사
id(r3) # 2579171405888 -> r의 주소와 같음

# 원소와 객체 제거
r.remove(10) # 특정 원소 제거
print(r)

r.clear() # 전체 원소 제거

del r # 객체 제거
