'''
문2) 다음 벡터(emp)는 '입사년도이름급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 사원의 이름만 추출하는 함수를 정의하시오. 

# <출력 결과>
 names = ['홍길동', '이순신', '유관순']
'''

from re import findall

# <Vector data>
emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]

# 함수 정의
def name_pro(emp):
    # pass #내용 채우기
    name=[]
    for e in emp:
        # name.append(findall('[가-힣]{3}',e)) # 중첩 list 저장
        name.extend(findall('[가-힣]{3}',e)) # 단일 list 저장
    return name

# 함수 호출 
names = name_pro(emp)
print('names =', names)
