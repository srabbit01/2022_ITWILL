# -*- coding: utf-8 -*-
"""
step03_tuple.py

tuple 특징
- 형식) 변수 = (값1,값2,...)
- 순서 존재(색인 사용)
- 수정 불가(새로운 내용 추가, 삭제, 수정 등)
- 리스트 보다 처리 속도 빠름
"""
lst=[10]
type(lst)

# tuple
# tp = tuple((10,))
tp=(10)=10
type(tp) # 원소가 한개 인 경우, 콤마(,)없이 지정하면 하나의 상수로 지정
tp = (10,) # 원소 한개 
print(tp) # (10,)

tp2 = (1,2,3,4,5)
print(tp2)

print(len(tp2), type(tp2)) # 5 <class 'tuple'>

# indexing
print(tp2[0], tp2[1:4]) # 1 (2, 3, 4)
print(tp2[-1], tp2[-3:]) # 5 (3, 4, 5)

# 수정 불가
tp2[0]=100 # TypeError

# tuple -> list 변환
lst = list(tp2)
print(lst)
lst[0]=100
tp2=tuple(lst)
tp2

# 객체 제거  
del tp2
#print(tp2) # name 'tp2' is not defined


# for + tuple
datas = (10, 23.4, 6, 8)

for d in datas :
    print(d*2, end = ' ')

# zip(): 내장함수 - vector 원소 묶음 -> tuple 반환    
names=['hong','lee','kang']
pay=[100,150,200]

zip_re=zip(names,pay) # 함수
type(zip_re)
print(zip_re) # <zip object at 0x00000258828E9640> -> zip 객체
for i in zip_re:
    print(i) # 한번 출력되어 소모되면 소진
'''
('hong', 100)
('lee', 150)
('kang', 200)
'''
print(list(zip_re)) # [] -> 커서나 그 아래 가리키기 때문에 한번 소진되면 사라짐

zip_li=list(zip(names,pay))
zip_li # [('hong', 100), ('lee', 150), ('kang', 200)]
type(zip_li) # list
type(zip_li[0]) # tuple
zip_li[0]
