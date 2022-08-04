# -*- coding: utf-8 -*-
"""
step05_dict.py

dict 특징 
 형식) {key1:value1, key2:value2, ...}
 - key 이용 -> 수정, 삭제, 추가 
 - key 중복 불가, 순서 없음(숫자 색인 사용 불가)
 - key를 색인으로 사용 (예) dict객체[key])
"""

# 1. dict 생성 
person = {'name':'홍길동', 'age':35, 'addr':'서울시'}
print(person) 
print(len(person), type(person)) # 3 <class 'dict'>


# 2. 수정, 삭제, 추가, 검색 
person['age'] = 45 # 수정 
del person['addr'] # 삭제 
person['pay'] = 350 # 추가 

# 3. for + dict
for key in person.keys() : # key 넘김 
    print(key, end = ' ') # key
    print(person[key]) # value
    
for value in person.values() :  # value 넘김 
    print(value) # value

for item in person.items() : # key+value
    print(item)

for k,v in person.items() : # key+value
    print('key:',k,', value:',v)

p = {'hi':['this','is','me'],'hello':('not','me'),
     123:{'my':1,'name':2}}
for item in p.items() : # key+value
    print(item)

# key 검색 
'age' in person
'age' not in person
print('age' in person) # True    

# key 유무
if 'age' in person:
    print('키 있음')
else:
    print('키 없음')

# 4. 단어 빈도수 
charset = ['pay', 'name', 'pay', 'name', 'age']
charset

# 방법1) key 검색 이용
wc = {} # 빈set 

for ch in charset :
    if ch not in wc : # 사전에 key 유무 
        wc[ch] = 1 # key 없음 
    else :
        wc[ch] += 1 # key 있음 
print(wc) # {'pay': 2, 'name': 2, 'age': 1}

# 방법2) get메서드 이용
wc={} # 빈set or dic
wc[1]=wc.get(1,0)
wc.get(1,0)
wc
for ch in charset:
    wc[ch]=wc.get(ch,0)+1

print(wc) # {'pay': 2, 'name': 2, 'age': 1}

help(wc.get) # 있으면 키, 없으면 기본값 반환
# Return the value for key if key is in the dictionary, else default.

# 5. {key : [value1, value2, ...]}
# 예) {'사번' : [급여, 수당]}
emp = {'1001' : [250, 50], '1002' : [200, 40], '1003': [300, 80]}

# 급여가 250 이상이면 사번 출력 & 수당 합계 
su_tot = 0 # 수당 합계

for eno, pay_su in emp.items() : # key + value
    if pay_su[0] >= 250 : # 급여 이용 
        print(eno) # 사번 출력 
        su_tot += pay_su[1] # 수당 누적 

print('수당의 합계 : %d'%su_tot) # 수당의 합계 : 130

# key 이용 연산 : 급여 + 보너스 
pay = {'홍길동' : 200, '이순신':250, '유관순' : 200} 
bonus = {'홍길동' : 50, '이순신':80, '유관순' : 30} 

pays = [pay[k] + bonus[k] for k in pay.keys() ] # lsit 내포
pays # [250, 330, 230]

avg = sum(pays) / len(pays)
print('급여 평균 =', avg)

# 6. key의 값을 list로 추가
weather = {} # {'지역': [최저온도,최고온도]}

citys=['서울','부산','대구'] # 지역
temps=[10,30,15,35,20,40]
for i in range(len(citys)): # range(3)
    weather[citys[i]]=[] # {'서울':[],'부산':[],'대구':[]} -> 리스트로 만들고자 할 때 초기값 항상 만들기
    # weather[citys[i]].append(temps[i*2:i*2+2])
    weather[citys[i]].extend(temps[i*2:i*2+2])
'''
citys index = 0,1,2
temps index = 0:2, 2:4, 4:6
  start index=city index * 2
  step index = citys index * 2 + 2
'''
print(weather)
# append: {'서울': [[10, 30]], '부산': [[15, 35]], '대구': [[20, 40]]}
# 중첩 리스트: 새로운 리스트를 추가하는 것이기 때문에 중첩 리스트 생성
# append 대신 extend 사용하면 단일 리스트 생성
# extend: {'서울': [10, 30], '부산': [15, 35], '대구': [20, 40]}

# 7. 더미변수 생성 방법 = 0과 1로 구성된 것

# 1) 혈액형 더미변수
map_data={'AB':1,'A':0,'B':0,'O':0}
datas=['A','B','A','O','AB','B'] # 실제 혈액형 정보

# list 내포 사용 
dummy=[map_data[d] for d in datas] # 더미변수 리스트 생성
dummy # [0, 0, 0, 0, 1, 0]

# 2) label 인코딩: y(종속)변수 숫자로 변환
label_map={'thin':[1,0,0],'normal':[0,1,0],'fat':[0,0,1]}
datas=['normal','fat','thin','normal']
# list 내포
label=[label_map[d] for d in datas] # one-hot-encoding: 정답=1, 정답X=0
label # [[0, 1, 0], [0, 0, 1], [1, 0, 0], [0, 1, 0]]

# 딕셔너리 메소드    
dir(person)
'''
 'clear',
 'copy',
 'fromkeys',
 'get',
 'items',
 'keys',
 'pop',
 'popitem',
 'setdefault',
 'update',
 'values'
 '''
