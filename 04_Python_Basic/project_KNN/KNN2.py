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

# 1. KNN 클래스 생성
class KNN:
    ## 생성자
    def __init__(self,num):
        from random import random
        self.num=num
        self.st_li=[random(),random()] # 적용 데이터 생성
        self.rl_li=[[random(),random()] for n in range(num)] # 기준 데이터 생성
    ## 메서드
    # 1) 유클리드 거리 계산
    def Udis(self):
        from math import sqrt
        self.Ud_cal=[]
        # 각 적용 데이터 별 유클리드 거리 계산
        for i in self.rl_li:
            x=(self.st_li[0]-i[0])
            y=(self.st_li[1]-i[1])
            self.Ud_cal.append(round(sqrt(x**2+y**2),5))
        # 유클리드 거리 계산 결과 오름차순 정렬
        self.Ud_calS=sorted(self.Ud_cal)  
    # 2) K 최근접 이웃 선정
    def neighbor(self,n):
        self.Udis()
        # 최근접 이웃 n개 추출
        self.k=[self.Ud_calS[i] for i in range(n)]
        # 선정된 최근접 이웃 n개 적용 데이터 추출
        self.k_data=[]
        for a in self.k:
            for b in self.Ud_cal:
                if a==b:
                    self.k_data.append(self.rl_li[self.Ud_cal.index(a)])
              
# 2. 사용자로부터 적용 데이터 개수 입력 받기
num=int(input('데이터 개수 : '))

# 3. KNN 객체 생성
knn=KNN(num)

# 4. 결과 출력
print('최근접이웃 선정 결과')
print(f'StandardData : {knn.st_li}')
a=1; do='yes'
while do=='yes':
    n=int(input('최근접 이웃 개수 : '))
    if 0 < n <= num:
        nei=knn.neighbor(n)
        print(f'{a}. 최근접이웃 {n}개 거리')
        print(f'- k{n} : {knn.k}')
        print(f'- k{n}_RealData: {knn.k_data}')
        a+=1
        do=input('계속 진행하시겠습니까?(yes/no) ').lower()
    else:
        print(f'0개 이상 {num}개 이하 입력하시오.')