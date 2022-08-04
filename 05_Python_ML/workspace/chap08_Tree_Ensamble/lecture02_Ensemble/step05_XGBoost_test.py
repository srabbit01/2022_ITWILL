'''
step05_XGBoost_test.py

pip install xgboost

 - XGBoost 분류트리 예
'''

from xgboost import XGBClassifier # 분류트리, 회귀트리
from xgboost import plot_importance # 중요변수 시각화
# xgboost는 자체적으로 중요변수 시각화 도구 제공
from sklearn.datasets import make_blobs # dataset
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import accuracy_score, classification_report # 평가 도구
import matplotlib.pyplot as plt

# 1. 데이터셋 로드 : blobs
X, y = make_blobs(n_samples=2000, n_features=4, centers=3, 
                   cluster_std=2.5, random_state=123)
'''
- n_samples: 샘플 수(크기)
- n_features: 독립변수(X) 개수 (크기)
- centers: 종속변수(y)의 범주 (2: 이항 분류기, 3 이상: 다항 분류기)
- cluster_std: 편차 (편차가 클 수록 오분류 증가=복잡, 작으면 분류 잘 됨)
               = 샘플 데이터 복잡도
- random_state: 난수 생성
'''

X.shape # (2000, 4)
y.shape
y # array([1, 1, 0, ..., 0, 0, 2]) = 3개 범주

# blobs 데이터 분포 시각화 
plt.title("three cluster dataset")
plt.scatter(X[:, 0], X[:, 1], s=100, c=y,  marker='o') # color = y범주
plt.xlabel("X1")
plt.ylabel("X2")
plt.show()
# 버블이 많이 겹칠 수록 분류 정확도 감소

# 2. 훈련/검정 데이터셋 생성
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3)


# 3. XGBOOST model 
xgb = XGBClassifier(objective='multi:softprob') # objective='binary:logistic'
# xgb = XGBClassifier(objective='multi:softprob')
'''
objective: 종속변수(y)에 따른 종속변수 '활성함수' 지정
- binary:logistic: 범주 2개 (이항 분류기) -> logistic: sigmoid 함수
- multi:softprob: 범주 3개 이상인 경우 (다항 분류기) -> softmax 활성함수
'''

# train data 이용 model 생성 
eval_set=[(X_test,y_test)] # 평가셋
model = xgb.fit(X_train, y_train, eval_metric='merror',verbose=True,
                eval_set=[(X_test,y_test)]) # eval_metric='error'
# model = xgb.fit(X_train, y_train, eval_metric='error') # error 생략 가능
'''
eval_metric: 평가 방법(도구) 지정 (모델 성능 평가)
- error: 이항 분류 평가 도구 (범주 2개) (binary:logistic)
- merror: 다항 분류 평가 도구 (범주 3개 이상) (multi:softprob)
verbose: True면 과정 표시, False면 표시하지 않음 -> 오차 화면 출력
eval_set=[(X_test,y_test)]: 성능 평가 데이터 지정 -> test_set (eval: evaluation 평가)
'''
# [90]	validation_0-merror:0.09000
# [n번째 트리] validation_0-merror:오차 (by 평가셋)
print(model) # 파라미터 정보 출력
'''
XGBClassifier(base_score=0.5, booster='gbtree', callbacks=None,
              colsample_bylevel=1, colsample_bynode=1, colsample_bytree=1,
              early_stopping_rounds=None, enable_categorical=False,
              eval_metric=None, gamma=0, gpu_id=-1, grow_policy='depthwise',
              importance_type=None, interaction_constraints='',
              learning_rate=0.300000012, max_bin=256, max_cat_to_onehot=4,
              max_delta_step=0, max_depth=6, max_leaves=0, min_child_weight=1,
              missing=nan, monotone_constraints='()', n_estimators=100,
              n_jobs=0, num_parallel_tree=1, objective='multi:softprob',
              predictor='auto', random_state=0, reg_alpha=0, ...)
- max_depth: 최대 트리 깊이
- min_child_weight
- n_estimators: 생성 트리 개수
- objective: 종속변수 활성함수
'''

# 4. model 평가 
y_pred = model.predict(X_test) 
acc = accuracy_score(y_test, y_pred)
print('분류정확도 =', acc)
# 분류정확도 = 0.9183333333333333
# 데이터 복잡도 증가할 수록 분류 정확도 감소

report = classification_report(y_test, y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       0.90      0.88      0.89       208
           1       0.99      0.99      0.99       200
           2       0.86      0.89      0.87       192

    accuracy                           0.92       600
   macro avg       0.92      0.92      0.92       600
weighted avg       0.92      0.92      0.92       600
'''
# 이항 분류기가 다항 분류기보다 분류 정확도가 높음

dir(model)
model.score(X_test,y_test)

# 5. fscore 중요변수 시각화  
fscore = model.get_booster().get_fscore()
print("fscore:",fscore) 
# fscore: {'f0': 884.0, 'f1': 842.0, 'f2': 960.0, 'f3': 735.0} # f위치
# 각 독립변수 별 중요 점수 추출
# f2으 중요도 제일 높음

# 중요변수 시각화
plot_importance(model) # 가장 중요한 독립변수 상단
# 가장 중요한 변수 순서대로 출력
plt.show()



