# -*- coding: utf-8 -*-
"""
step04_set.py

set 특징 
 - 순서 없음(색인 사용불가)
 - 중복 허용 불가 
 - 수정 불가(추가, 삭제 가능) 
 - 형식) 변수 = {값,값,...}
- 집합 개념 사용
"""

# 1. set 생성 
st = {1, 3, 5, 1, 5} # 중복 허용 불가 
print(st, len(st)) # {1, 3, 5} 3

# for + set
for s in st :
    print(s, end = ' ') # 1 3 5
        
# 색인 사용 불가
# st[0] # TypeError

# 2. 중복 불가 
gender = ['남','여','남','여'] # list
gender

# list -> set
sgender = set(gender)
print(sgender) # {'남', '여'}

# sgender[0]

# set -> list
lgender=list(sgender)
lgender # ['여', '남']
print(lgender[0]) # 여

# 집합관련 
set1 = {1, 3, 4, 5, 7}
set2 = {3, 5}

set1.union(set2) #  합집합 : {1, 3, 4, 5, 7}
set1.difference(set2) # 차집합 : {1, 4, 7}
set1.intersection(set2) # 교집합 : {3, 5}

# 원소 추가 
set2.add(7)
print(set2) # {1, 3, 5, 7}

# 원소 삭제 
set2.discard(7) 
print(set2) # {1, 3, 5}

dir(set1)
'''
 'add',
 'clear',
 'copy',
 'difference',
 'difference_update',
 'discard',
 'intersection',
 'intersection_update',
 'isdisjoint',
 'issubset',
 'issuperset',
 'pop',
 'remove',
 'symmetric_difference',
 'symmetric_difference_update',
 'union',
 'update'
 '''
# remove
si={1,2,3,4}
si.remove(2) # 원소가 없는 경우 error 발생
si.discard(2) # 원소가 없는 경우 error 없음
 



