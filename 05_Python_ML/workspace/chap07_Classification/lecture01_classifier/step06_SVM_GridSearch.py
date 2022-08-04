# -*- coding: utf-8 -*-
"""
step06_SVM_GridSearc.py
 - Grid Search : best parameger 찾기 
"""

from sklearn.svm import SVC # svm model 
from sklearn.datasets import load_breast_cancer # dataset 
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import accuracy_score # 평가 

# 1. dataset load 
X, y = load_breast_cancer(return_X_y= True)
X.shape # (569, 30)


# 2. train/test split 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123)


# 3. 비선형 SVM 모델 
obj = SVC(C=1.0, kernel='rbf', gamma='scale')
'''
기본 parameter
 C=1.0 : cost(오분류) 조절 : 결정경계 위치 조정
 kernel='rbf' : 커널트릭 함수 
  -> kernel : {'linear', 'poly', 'rbf', 'sigmoid', 'precomputed'}
 gamma='scale' : 결정경계 모양 조절 조정 
  -> {'scale', 'auto'} or float
  -> gamma='scale' : 1 / (n_features * X.var())
  -> gamma='auto' : 1 / n_features
'''

model = obj.fit(X=X_train, y=y_train)


# model 평가 
y_pred = model.predict(X = X_test)

acc = accuracy_score(y_test, y_pred)
print('accuracy =',acc)


# 4. 선형 SVM : 선형분류 
obj2 = SVC(C=1.0, kernel='linear', gamma='scale')

model2 = obj2.fit(X=X_train, y=y_train)

# model 평가 
y_pred = model2.predict(X = X_test)

acc = accuracy_score(y_test, y_pred)
print('accuracy =',acc)


###############################
### Grid Search 
###############################

from sklearn.model_selection import GridSearchCV 

parmas = {'kernel' : ['rbf', 'linear'],
          'C' : [0.01, 0.1, 1.0, 10.0, 100.0], # e^(-2) ~ e^(+2)
          'gamma': ['scale', 'auto']} # dict 정의 

# 5. GridSearch model   
grid_model = GridSearchCV(model, param_grid=parmas, 
                   scoring='accuracy',cv=5, n_jobs=-1).fit(X, y)
'''
- scoring: 분류 평가 기준 (accuracy: 분류 정확도)
- cv: k겹 교차검정 = 5등분
- n_jobs: 사용되는 cpu 개수 지정 (모든 cpu 지정: -1)
- X, y: k겹 교차검정을 사용하기 때문에 train, test 사용하지 않고 원본 데이터 입력
'''

# 호출 가능한 멤버변수 및 메서드
dir(model)
'''
- best_score_: 최적의 파라미터에 의해 학습된 모델의 평가 점수
- best_params_: 최적의 파라미터 조합 
'''

# 1) Best score 
print('best score =', grid_model.best_score_)
# best score = 0.9631268436578171

# 2) Best parameters 
print('best parameters =', grid_model.best_params_)
# best parameters = {'C': 100.0, 'gamma': 'scale', 'kernel': 'linear'}

# 3) Best parameters 적용 model 생성
obj3 = SVC(C=100.0, kernel='linear', gamma='scale')
model3 = obj3.fit(X=X_train, y=y_train)
# model 평가 
y_pred3=model3.predict(X = X_test)
acc = accuracy_score(y_test,y_pred3)
print('accuracy =',acc)
# accuracy = 0.9766081871345029