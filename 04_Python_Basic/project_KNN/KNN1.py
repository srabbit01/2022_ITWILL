# -*- coding: utf-8 -*-
'''
k 최근접이웃(kNN : k Nearest Neighbor) 알고리즘 구현
<조건1> 사용 문법 : 클래스와 파이썬 기초문법(현재까지 배운 내용 적용)
<조건2> 데이터 생성 : random 모듈의 random() 함수 이용(0과 1 사이의 난수 실수)
▪ 적용데이터 : [[x1, y1], [x2, y2], ... [xn, yn]] -> 10개 이상(중첩 list)
▪ 기준데이터 : [x, y] -> 1개(단일 list)
<조건3> 알고리즘 구현 내용
• 1. 거리계산 : 기준데이터와 적용데이터 간의 유클리드 거리계산식(다음 페이지 참고)
• 2. k 최근접 이웃 선정 : 최근접이웃 1, 3, 5개 선정
• 3. 최근접이웃 선정 결과 출력 예(소수점 5자리 까지 표기)
k1 -> [0.18133] -> 최근접이웃 1개 거리(distance)
real data : [0.91311, 0.12316] -> 적용데이터 중에서 선정된 데이터
k3 -> [0.18133, 0.18540, 0.24802] ] -> 최근접이웃 3개 거리(distance)
real data : [0.91311, 0.12316] [0.75420, 0.45281] [0.62317, 0.18049]
k5 -> [0.18133, 0.18540, 0.24802, 0.45897, 0.59520] ] -> 최근접이웃 5개 거리(distance)
real data : [0.91311, 0.12316] [0.75420, 0.45281] [0.62317, 0.18049] [0.8892, 0.7480] [0.24990, 0.28701]
'''

# 1. 사용자로부터 데이터 개수 입력 받기
num=int(input('데이터 개수 : ')); print()

# 2. 데이터 난수 생성
from random import random
# 적용 데이터 생성
rl_li = [[random(),random()] for n in range(num)]
# 기준 데이터 생성
st_li=[random(),random()]

# 3. 유클리드 거리 계산식 클래스 생성
class Udistance:
    from math import sqrt
    # 생성자
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    # 메서드
    def Udis(self):
        result=sqrt((self.x1-self.x2)**2+(self.y1-self.y2)**2)
        return round(result,5)

# 4. 각 데이터 별 유틀리드 거리 계산
Ud_cal=[]
for i in rl_li:
    Ud=Udistance(st_li[0],st_li[1],i[0],i[1])
    Ud_cal.append(Ud.Udis())
# 오름차순 정렬: 최근접 이웃 높은 순서대로 정렬
Ud_calS=sorted(Ud_cal)

# 5. k 최근접 이웃 선정
k1=[min(Ud_cal)] # 1개
k3=[Ud_calS[i] for i in range(3)] # 3개
k5=[Ud_calS[i] for i in range(5)] # 5개

# 6. 선정된 최근접 이웃 적용 데이터 추출 함수 생성
def get(kUd,k_data):
    for a in kUd:
        for b in Ud_cal:
            if a==b:
                k_data.append(rl_li[Ud_cal.index(a)])
# 선정된 최근접 이웃 적용 데이터 추출
k1_data=[]
get(k1,k1_data) # 1개

k3_data=[]
get(k3,k3_data) # 3개

k5_data=[]
get(k5,k5_data) # 5개

# 7. 결과 출력
print(f'''최근접이웃 선정 결과

1. 기준 데이터
standard_data: {st_li}

2. 최근접이웃 1개 거리
k1: {k1}
k1_realdata: {k1_data}

3. 최근접이웃 3개 거리
k3: {k3}
k3_realdata: {k3_data}

4. 최근접이웃 5개 거리
k5: {k5}
k5_realdata: {k5_data}
''')