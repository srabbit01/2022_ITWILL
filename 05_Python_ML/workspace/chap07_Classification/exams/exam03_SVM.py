# -*- coding: utf-8 -*-
"""
문3) 다음 조건에 맞게 비선형 SVM 모델과 선형 SVM 모델을 생성하시오. 
  <조건1> 비선형 SVM 모델과 선형 SVM 모델 생성
  <조건2> GridSearch model을 이용하여 best score와 best parameters 구하기  
"""

from sklearn.svm import SVC # svm model 
from sklearn.datasets import load_iris # dataset 
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import accuracy_score # 평가 

# 1. dataset load 
X, y = load_iris(return_X_y= True)
X.shape # (569, 30)

X.var() # 52119.70516752481

# 2. train/test split 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123)


# 3. 비선형 SVM 모델 
nonli_model=SVC(kernel='rbf').fit(X=X_train,y=y_train)

# 4. 선형 SVM : 선형분류 가능한 데이터(noise 없는 데이터) 
li_model=SVC(kernel='linear').fit(X=X_train,y=y_train)

# 5. Grid Search : best parameter 찾기 
parmas = {'kernel' : ['rbf', 'linear'],
          'C' : [0.01, 0.1, 1.0, 10.0, 100.0],
          'gamma': ['scale', 'auto']} # dict 정의 

grid_model = GridSearchCV(model, param_grid=parmas, 
                   scoring='accuracy',cv=5, n_jobs=-1).fit(X, y)

# 1) Best score 
print('best score =', grid_model.best_score_)
# best score = 0.9800000000000001

# 2) Best parameters 
print('best parameters =', grid_model.best_params_)
# best parameters = {'C': 1.0, 'gamma': 'scale', 'kernel': 'linear'}

# 3) Best parameters 적용 model 생성
best_model = SVC(C=1.0, kernel='linear', gamma='scale').fit(X=X_train, y=y_train)
# model 평가 
y_pred=best_model.predict(X = X_test)
acc = accuracy_score(y_test,y_pred)
print('accuracy =',acc)
# accuracy = 0.9555555555555556