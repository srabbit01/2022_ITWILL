# -*- coding: utf-8 -*-
"""
step03_RF_parameter_GridSearch.py

 1. RandForest parameters
 2. GridSearch : best parameters 
"""

from sklearn.ensemble import RandomForestClassifier # model 
from sklearn.datasets import load_digits # dataset 
from sklearn.model_selection import GridSearchCV # best parameters


# 1. dataset load
X, y = load_digits(return_X_y=True)


# 2. model 생성 
#help(RandomForestClassifier)
rfc = RandomForestClassifier(random_state=1) # default 적용 
'''
주요 hyper parameter(default) 
n_estimators=100 : 결정 트리 개수, 많을 수록 성능이 좋아짐
criterion='gini' : 중요변수 선정기준 : {"gini", "entropy"}
max_depth=None : min_samples_split의 샘플 수 보다 적을 때 까지 tree 깊이 생성
min_samples_split=2 : 내부 node 분할에 사용할 최소 sample 개수
max_features='auto' : 최대 사용할 x변수 개수 : {"auto", "sqrt", "log2"}
                      -> 최대 몇 개의 독립변수 이용하여 종속변수 분할?
                      -> sqrt(독립변수 개수), log2(독립변수 개수) 
min_samples_leaf=1 : leaf node를 만드는데 필요한 최소한의 sample 개수
n_jobs=None : cpu 사용 개수
'''

model = rfc.fit(X = X, y = y)


# 3. GridSearch model 
# - best parameters 

parmas = {'n_estimators' : [100, 150, 200],
          'max_depth' : [None, 3, 5, 7],
          'max_features' : ["auto", "sqrt"],
          'min_samples_split' : [2, 10, 20],
          'min_samples_leaf' : [1, 10, 20]} # dict 정의 

grid_model = GridSearchCV(model, param_grid=parmas, 
                          scoring='accuracy',cv=5, n_jobs=-1)
'''
- model: 분류기 객체 (적용하고자 할 모델)
- param_grid: hyper parameter
- scoring: 평가 방법
- cv: 교차 검정
- n_jobs: 사용되는 cpu 수
'''
grid_model = grid_model.fit(X, y)


# 4. Best score & parameters 
print('best score =', grid_model.best_score_)
# best score = 0.9438130609718354

print('best parameters =', grid_model.best_params_)
'''
best parameters = {'max_depth': None, 'max_features': 'auto',
                   'min_samples_leaf': 1, 'min_samples_split': 2,
                   'n_estimators': 200}
'''
# 5. best model 재생성
best_model = RandomForestClassifier(random_state=2,
                                    n_estimators=200).fit(X = X, y = y)
score=best_model.score(X,y)
print('best score :',score) # 최고 점수
# best score : 1.0