# -*- coding: utf-8 -*-
"""
step01_RandomForest.py
"""

from sklearn.ensemble import RandomForestClassifier # model 
from sklearn.datasets import load_wine # dataset 
# 평가 도구 
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report


# 1. dataset load
wine = load_wine()

x_names = wine.feature_names
print(x_names)

X, y = wine.data, wine.target
X.shape # (178, 13)
# Label Encoding

# 2. model 생성 
#help(RandomForestClassifier)
'''
주요 hyper parameter(default)
 n_estimators=100 : tree 개수 
 criterion='gini' : 중요변수 선정 기준 
 max_depth=None : 트리 깊이 
 min_samples_split=2 : 내부 노드 분할에 필요한 최소 샘플 수
'''

obj = RandomForestClassifier() 
model = obj.fit(X = X, y = y) # full dataset 적용 


# 3. test set 생성 
import numpy as np

idx = np.random.choice(a=len(X), size=100, replace=False)
X_test, y_test = X[idx], y[idx]
X_test.shape # (100, 13)


# 4. model 평가 
y_pred = model.predict(X = X_test)

con_mat = confusion_matrix(y_test, y_pred)
print(con_mat)
'''
[[33  0  0]
 [ 0 44  0]
 [ 0  0 23]]
100% 예측했음을 볼 수 있음
'''
accuracy_score(y_test, y_pred) # 1.0

print(classification_report(y_test, y_pred))


# 5. 중요변수 시각화 
dir(model)
print('중요도 : ', model.feature_importances_)
'''
중요도 :  [0.1523359  0.03614263 0.01763674 0.02265849 0.02216607 0.05516696
 0.14588207 0.00995106 0.02636128 0.11678787 0.09245458 0.11171318
 0.19074318]
'''

x_names # x변수 이름  
x_size = len(x_names) # x변수 개수  

import matplotlib.pyplot as plt 

# 가로막대 차트 
plt.barh(range(x_size), model.feature_importances_) # (y, x)
plt.yticks(range(x_size), x_names) # y축 눈금  
plt.xlabel('feature_importances') 
plt.show()











