'''
1. GaussianNB  : x변수가 연속형이고, 정규분포인 경우 
  - X변수를 대상으로 z-score 표준화 방식으로 스케일링 필요  

관련 문서 : 
https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html
'''

#사후확률 : 사전확률에 대한 조건부 확률  
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
# naive_bayes 모듈: GaussianNB, BernoulliNB, MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# classification_report: 분류 결과 평가

# 콘솔 환경 설정 
import sys
import numpy as np
import pandas as pd
np.set_printoptions(threshold=sys.maxsize) # 배열 전체 출력(배열 내용 일부분 보일때) 
pd.set_option('display.max_columns', 100) # 최대 칼럼수 지정 


# 1. dataset load 
X, y = load_iris(return_X_y=True)
print(X)
# y: 꽃의 종

from sklearn.preprocessing import StandardScaler, MinMaxScaler

# z-score 표준화 : 평균=0, 표준편차=1 - 정규분포를 이루고 있는 x변수 대상 스케일링 
# X = StandardScaler().fit_transform(X) # fit + transform 

# 최대-최소 정규화
X = MinMaxScaler().fit_transform(X) 

# 2. train/test data set 구성 
X_train, X_test, y_train, y_test = train_test_split(
     X, y, test_size=0.3, random_state=123) # seed값 

print(X_train.shape) # (105, 5)
print(X_test.shape) # (45, 5)


# 3. NB model 생성 
gnb = GaussianNB() 
model = gnb.fit(X_train, y_train) # y 집단변수 

# 4. model 예측치 
y_pred = model.predict(X_test)


# 5. model 평가 
# 1) accuracy
y_true = y_test
acc = accuracy_score(y_true, y_pred)
print('accuracy =', acc) # accuracy = 0.9555555555555556

# 2) confusion matrix
con_mat = confusion_matrix(y_true, y_pred)
print(con_mat)
'''
[[18  0  0]
 [ 0 10  0]
 [ 0  2 15]]
'''

# 3) classification_report: 평가 결과 종합적으로 출력
report=classification_report(y_true,y_pred) 
print(report)
'''
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        18
           1       0.83      1.00      0.91        10
           2       1.00      0.88      0.94        17

    accuracy                           0.96        45
   macro avg       0.94      0.96      0.95        45
weighted avg       0.96      0.96      0.96        45
- precision: 정밀도, recall: 재현율
- f1-score: F-측정치
- support: 범주 별 빈도수
- accuracy: 정확도
- macro avg = precision, recall, f1-score 각 평균 (score에 대한 평균)
- weighted avg: 가중평균 (출현 빈도수를 가중치로 두고 계산) = sum(범주별score*support) / sum(support)
'''
