# -*- coding: utf-8 -*-
"""
step01_logisticRegression_ROC.py

 - 이항분류기(binary class classifier)
 - 이항분류기 평가 도구: ROC curve
"""

from sklearn.datasets import load_breast_cancer # dataset
from sklearn.linear_model import LogisticRegression # model 
from sklearn.model_selection import train_test_split # dataset split 
from sklearn.metrics import confusion_matrix, accuracy_score # model 평가 


################################
### 이항분류(binary class) 
################################

# 1. dataset loading 
X, y = load_breast_cancer(return_X_y=True)

print(X.shape) # (569, 30)
print(y) # 0 or 1(악성) -> 이항


# 2. train/test split 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.3, random_state=123)


# 3. model 생성 
lr = LogisticRegression(solver='lbfgs', max_iter=3000,random_state=123,verbose=1)  
help(LogisticRegression)
'''
C=1.0 : 비용함수(Cost Function), 0~1 범위 - 수렴속도 지정 (적을 수록 오차 작음) -> 오차 조정
 -> 1에 가까울 수록 수렴 속도 빠름
random_state=None, : 난수 seed값 지정 
solver='lbfgs', : 최적화에 사용되는 기본 알고리즘(solver) (기본: lbfgs)
max_iter=100,  : 반복학습횟수 
multi_class='auto' : 다항분류(multinomial) 
'''
model = lr.fit(X=X_train, y=y_train)
# Increase the number of iterations (max_iter) or scale the data as shown in:
# -> 수렴 정도가 낮아 반복횟수를 늘리기

dir(model)
'''
predict: 예측치 구하는 메서드(class 예측치)
predict_proba: 확률 예측치 (나올 수 있는 확률)
score: 결정계수(분류 정확도 제공)
'''

# 4. model 평가 
y_pred = model.predict(X = X_test) # class 예측치 

y_true = y_test # 관측치 

# 1) 혼동행렬(confusion_matrix)
con_max = confusion_matrix(y_true, y_pred)
print(con_max)
'''
0: 양성, 1: 악성
관측치\예측치 0(N) 1(P)
      0(N) [[ 64   4]
      1(P)  [  1 102]]
- 왼쪽 대각선: 정분류
- 오른쪽 대각선: 오분류
'''

# 2) 분류정확도 
acc = (con_max[0,0]+con_max[1,1]) / con_max.sum()
print('accuracy =',acc) # accuracy = 0.9707602339181286
accuracy_score(y_true,y_pred) # 분류 정확도 함수 사용: 0.9707602339181286

train_score = model.score(X=X_train, y=y_train)
train_score # 0.949748743718593

test_score = model.score(X=X_test, y=y_test)
test_score # 0.9707602339181286

# 보통 train > test

# 3) F-Measure: 비율이 불균형인 자료 평가지표 
# 만일 0과 1의 출현빈도 차이가 매우 크면 정확도가 아닌, F-Measure 사용
# 정밀도(Precision) = TP / (TP + FP)
Preci=con_max[1,1]/con_max[:,1].sum()
# 재현율(Recall) = TP / (TP + FN)
Recall=con_max[1,1]/con_max[1,:].sum()
# F-측정치(F-Measure) = 2*((Precision*Recall)/(Precision+Recall))
F_measure=2*((Preci*Recall)/(Preci+Recall))
print('F_measure =',F_measure) # F_measure = 0.9760765550239234
# 비교적 높은 값으로 출력


#############################
# ROC curve 시각화
#############################


# 1) 혼동행렬 
con_max = confusion_matrix(y_true, y_pred)
print(con_max) # 행 : 관측치 vs 열 : 예측치 
'''
0: 양성, 1: 악성
      0(N) 1(P)
0(N) [[ 64   4]
1(P)  [  1 102]]
'''

# 2) 확률 예측치
y_pred_proba = model.predict_proba(X = X_test) 
y_pred_proba.shape # (171, 2) -> 0과 1 예측확률 
# [9.99999998e-01, 2.10549266e-09] = [0이 나올 확률, 1이 나올 확률]
y_pred_proba = y_pred_proba[:, 1] # 1이 나올 예측확률 추출  


# 3) ROC curve 
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt 

# 임계값(thresholds)에 따른 FPR, TPR 반환
fpr, tpr, thresholds = roc_curve(y_true, y_pred_proba) # x축(FPR), y축(TPR), 임계값(thresholds)
# y_pred_proba: y 예측치 확률
'''
fper: False Positive Rate
tper: True Positive Rate
- 임계값(thresholds): 예측값을 결정하는 확률(범위:1~0)의 기준으로 사용
  -> 1 ~ 0 으로 가는데 벡터가 되는 기준 값
- TPR: 임계값이 0에 가까울 수록 TPR의 최대값을 나타냄
- FPR: 임계값이 0에 가까울 수록 FPR의 최대값을 나타냄
[결론]
ROC Curve는 임계값을 1부터 0까지 변화시켜 FPR을 구하고,
FPR값의 변화에 따라 TPR값을 나타내는 곡선
'''
import numpy as np
print(np.round(thresholds,5))
print(np.round(tpr,5))
print(np.round(fpr,5))
''' -> 확률의 변화를 벡터값으로 나타낸 것
[2.      1.      0.99532 0.99517 0.76086 0.37446 0.28606 0.     ]
[0.      0.00971 0.64078 0.64078 0.99029 0.99029 1.      1.     ]
[0.      0.      0.      0.01471 0.01471 0.07353 0.07353 1.     ]
'''

plt.plot(fper, tper, color = 'red', label='ROC curve')
plt.plot([0, 1], [0, 1], color='green', linestyle='--', label='AUC')
plt.legend()
plt.show()


##################################
### TPR vs FPR 관계
##################################

# TPR (True Postitive Rate): 실제 양성을 양성으로 예측할 비율 = TP / (TP + FN)
# FPR (False Positive Rate): 실제 음성을 양성으로 예측할 비율 = FP / (FP + TN)
con_max = confusion_matrix(y_true, y_pred)
print(con_max) # 행 : 관측치 vs 열 : 예측치 
'''
      0(N) 1(P)
0(N) [[ 64(TN)   4(FP)] = 68
1(P)  [  1(FN) 102(TP)]] = 103
'''

# 교차행렬
TPR = con_max[1,1]/con_max[1,:].sum() # 0.9902912621359223
FPR = con_max[0,1]/con_max[0,:].sum() # 0.058823529411764705

print('TPR =',TPR,',','FPR =',FPR)
# TPR = 0.9902912621359223 , FPR = 0.058823529411764705
# TPR 높은 예측력 (1에 수렴정도), FPR 높은 예측력 (0에 수렴정도)
