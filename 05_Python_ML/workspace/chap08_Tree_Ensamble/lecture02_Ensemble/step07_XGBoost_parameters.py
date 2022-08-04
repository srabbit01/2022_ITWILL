# -*- coding: utf-8 -*-
"""
step07_XGBoost_parameters.py

1. XGBoost Hyper parameters 
2. model 학습 조기 종료 
3. Best Hyper parameters
"""

from xgboost import XGBClassifier # model 
from sklearn.datasets import load_breast_cancer # dataset 
from sklearn.model_selection import train_test_split # dataset split 
from sklearn.metrics import accuracy_score, classification_report # 평가


# 1. XGBoost Hyper parameters 

# 1) dataset load 
cancer = load_breast_cancer()

x_names = cancer.feature_names
print(x_names, len(x_names)) # 30
y_labels = cancer.target_names
print(y_labels) # ['malignant' 'benign'] : 이항

X, y = load_breast_cancer(return_X_y=True)


# 2) train/test split 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3)


# 3) model 생성 
xgb = XGBClassifier() # default 
model = xgb.fit(X_train, y_train)

print(model) # default parameters
'''
1. colsample_bytree=1 : 트리 모델 생성 시 훈련셋 샘플링 비율(보통 : 0.6 ~ 1)
2. learning_rate=0.3 : 학습율(보통 : 0.01~0.1) = 0의 수렴속도
   -> 숫자 클 수록 수렴 속도 빠름, 작을 수록 수렴 속도 느림
3. max_depth=6 : 트리의 깊이(클 수록 성능이 좋아짐, 과적합 영향)
4. min_child_weight=1 : 자식 노드 분할을 결정하는 가중치(Weight)의 합
  - 값을 작게하면 더 많은 자식 노드 분할(과적합 영향)
5. n_estimators=100 결정 트리 개수(default=100), 많을 수록 고성능
6. objective='binary:logistic'(기본), 'multi:softprob'
과적합 조절 : max_depth 작게, min_child_weight 크게 
'''               

## 2. model 학습 조기 종료
xgb = XGBClassifier(colsample_bytree=1, # 전체가 훈련 데이터
                    learning_rate=0.3, # 학습율
                    max_depth=6, # 최대 트리 깊이
                    min_child_weight=1, # 가중치 합
                    n_estimators=500) 

eval_set = [(X_test, y_test)]  

model = xgb.fit(X=X_train, y=y_train, 
                eval_set=eval_set,
                eval_metric='error',
                early_stopping_rounds=80, # 1 ~ 80
                verbose=True)
'''
훈련셋: X_train, y_train
평가셋: eval_set
평가방법: eval_metric
종기종료 횟수: early_stopping_rounds -> 과적합 예방
학습과정 출력 여부: verbose
'''
# early_stopping_rounds: 조기 중지
# -> 지정한 트리 개수까지 무조건 만들고 그 이후 오차율이 변화가
#    없으면 중간에 중단 (전체 지정한 개수까지 만들지 않음)
# 따라서, [89] validation_0-error: 0.02924 -> 89번째 학습에서 조기 종료

# 3. model 평가 
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(acc) # 0.9766081871345029

report = classification_report(y_test, y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       0.98      0.95      0.97        66
           1       0.97      0.99      0.98       105

    accuracy                           0.98       171
   macro avg       0.98      0.97      0.98       171
weighted avg       0.98      0.98      0.98       171
'''


# 4. Best Hyper parameters: 민감한 파라미터 입력
from sklearn.model_selection import GridSearchCV # class 

# default parameters 
xgb = XGBClassifier()

params = {'colsample_bytree': [0.5, 0.7, 1],
          'learning_rate' : [0.01, 0.3, 0.5],
          'max_depth' : [5, 6, 7],
          'min_child_weight' : [1, 3, 5],
          'n_estimators' : [100, 200, 300]} # dict


gs = GridSearchCV(estimator = xgb, 
             param_grid = params,  cv = 5)

model = gs.fit(X=X_train, y=y_train, eval_metric='error',
       eval_set = eval_set, verbose=True)


print('best score =', model.best_score_)
# best score = 0.9648101265822785

print('best parameters :', model.best_params_)
'''
best parameters : {'colsample_bytree': 0.7,
                   'learning_rate': 0.5,
                   'max_depth': 5,
                   'min_child_weight': 3,
                   'n_estimators': 100,}
'''





