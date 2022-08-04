# -*- coding: utf-8 -*-
"""
step01_kNN.py

 - 알려진 범주로 알려지지 않은 범주 분류 
 - 유클리드 거리계신식 이용 
"""

from sklearn.neighbors import KNeighborsClassifier # class

# 1.dataset 생성 : ppt.6 참고 
# 이미 알려진 집단
grape = [8, 5]   # 포도[단맛,아삭거림] - 과일(0)
fish = [2, 3]    # 생성[단맛,아삭거림] - 단백질(1)
carrot = [7, 10] # 당근[단맛,아삭거림] - 채소(2)
orange = [7, 3]  # 오랜지[단맛,아삭거림] - 과일(0)
celery = [3, 8]  # 셀러리[단맛,아삭거림] - 채소(2)
cheese = [1, 1]  # 치즈[단맛,아삭거림] - 단백질(1)

# 알려진 집단(x변수) 
know_group = [grape,fish,carrot,orange,celery,cheese] 

# 알려진 집단의 클래스(y변수) 
y_class = [0, 1, 2, 0, 2, 1] 

# 알려진 집단의 클래스 이름 
class_label = ['과일', '단백질', '채소'] 
 

# 2. 분류기 
knn = KNeighborsClassifier(n_neighbors = 3)  # 객체 생성: 최근접이웃=3
model = knn.fit(X = know_group, y = y_class) 

# 3. 분류기 평가 
x1 = int(input('단맛(1~10): ')) # 단맛(1~10) 
X2 = int(input('아삭거림(1~10): ')) # 아삭거림(1~10) 

# 분류대상
# 입력 데이터가 중첩 리스트기 때문에, 중첩 리스트로 지정
test_X = [[x1, X2]] # 중첩 lsit: [[5, 9]]

# class 예측 
y_pred = model.predict(X = test_X)[0] # 값 반환
print(y_pred) # [2]
print('분류 결과 :',class_label[y_pred]) # 분류 결과 : 채소


##################################
## 유클리드안 거리 계산식 적용
##################################
# 알려진 집단 vs 분류 대상 간 거리
# 차(-) -> 제곱(**) -> 합(sum) _> 제곱근(sqrt)

import numpy as np

# 1) list -> numpy.array
know_group=np.array(know_group) # 기존 그룹 위치
non_know = np.array(test_X) # 새로운 데이터
y_class=np.array(y_class) # 기존 그룹 범주

# 2) 유클리드 거리 계산
# (1) 그룹 내 각 요소와 새로운 데이터 간 차이
diff=know_group-non_know
# (2) 차의 제곱
square=diff**2
# (3) 제곱의 합
square_sum=square.sum(axis=1)
# (4) 제곱근
distance=np.sqrt(square_sum)
print(distance)
# [5.         6.70820393 2.23606798 6.32455532 2.23606798 8.94427191]
# 가장 거리가 가까운 순서대로: 6(단백질) > 2(단백질) > 4(과일)

distance=np.sqrt(((know_group-non_know)**2).sum(axis=1))

# 3) 오름차순 정렬 -> index 반환
idx=distance.argsort()
print(idx) # [2 4 0 3 1 5]

# 4) 최근접 이웃 선정
# (1) k개 데이터 위치 선정
k=3
k_idx=idx[:k]
print(k_idx)
# (2) k개 데이터 선정
result=y_class[idx[:k]]
print(result) # [2 2 0]
# (3) 지정된 데이터 이름 출력
k_name=[]
for i in result:
    k_name.append(class_label[i])
# (4) 가장 많이 출력된 집단 확인
import pandas as pd
k_name=pd.Series(k_name)
k_name.mode().values[0] # '채소'
pd.Series(k_name).mode()
