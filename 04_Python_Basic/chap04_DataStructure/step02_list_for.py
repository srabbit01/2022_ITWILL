# -*- coding: utf-8 -*-
"""
step02_list_for.py

리스트 내포 
 - list안에서 for와 if문을 한 줄로 표현한 문법

 형식1) 변수 = [실행문  for 변수 in 열거형객체] 
       실행순서: 1. for문 > 2. 실행문 > 3. 변수 저장
      
 형식2) 변수 = [실행문  for 변수 in 열거형객체 if 조건식]   
"""

# 형식1) 변수 = [실행문  for 변수 in 열거형객체] 

# x변량에 제곱(**) 계산 예
x = [2, 4, 1, 5, 8]

# print(x ** 2) # TypeError: list 객체 전체 대상 산술 연산 불가능

# list + for 예   
lst = [] # 계산결과 저장 
for i in x :
    lst.append(i**2)

lst # [4, 16, 1, 25, 64]

# list 내포 : 각 원소 산술연산
lst = [i ** 2 for i in x]
print(lst)

# 각 원소 -> 짝수 혹은 홀수 여부 판별
'''
result=[]
for i in x:
    if i%2==0:
        result.append('짝수')
    else:
        result.append('홀수')
'''
result=["짝수" if i%2==0 else "홀수" for i in x]
print(result) # ['짝수', '짝수', '홀수', '홀수', '짝수']

# 형식2) 변수 = [실행문  for 변수 in 열거형객체 if 조건식]
dataset = list(range(1, 101)) 

#  list+for : 10배수 값 저장  
'''
result = []
for data in dataset :
    if data % 10 == 0 :
        result.append(data)
        
print(result)        
'''
result=[data for data in dataset if data%10==0]
print(result)

# 내장함수 사용
min(x) # 최솟값 반환: 1
max(x) # 최댓값 반환: 8
sum(x) # 전체 원소의 합 반환: 20
# mean(x) # error -> 별도의 라이브러리 로딩 필요