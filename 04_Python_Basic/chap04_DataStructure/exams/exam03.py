'''
step04, 05 문제 

 문1) 중복 되지 않은 직위와 각 직위별 빈도수를 출력하시오.
 
 <<출력 결과 >>
 중복되지 않은 직위 : ['사장', '과장', '대리', '부장'] - set()
 각 직위별 빈도수 : {'과장': 2, '부장': 1, '대리': 2, '사장': 1} - 단어빈도수 
'''

position = ['과장', '부장', '대리', '사장', '대리', '과장'] # list 

sposition=set(position)
dposition=set(sposition)

dposition={}
'''
for i in position:
    if i not in dposition:
        dposition[i]=1 # 키 없음 -> 키 생성
    else:
        dposition[i]+=1 # 키 있음 -> 출현 후 값 누적
'''
for i in position:
    dposition[i]=dposition.get(i,0)+1

print('중복되지 않은 직위 :',list(sposition))
print('각 직위별 빈도수 :',dposition)
'''
중복되지 않은 직위 : ['사장', '대리', '부장', '과장']
각 직위별 빈도수 : {'과장': 2, '부장': 1, '대리': 2, '사장': 1}
'''