# -*- coding: utf-8 -*-
"""
step01_datasets_linearRegression.py

sklearn 패키지 
 - python 기계학습 관련 도구 제공 
"""

# 대부분 Class는 첫 글자 대문자

from sklearn.datasets import load_diabetes # 당뇨병 관련 데이터셋 로딩
# datasets: 기본 데이터셋 제공
from sklearn.linear_model import LinearRegression # 선형 모델 생성
# linear_model: 선형 회귀모델 생성 도구 모듈
# LinearRegression: 선형 회귀모델 생성 클래스
from sklearn.model_selection import train_test_split
# train_test_split: 훈련/평가 데이터 분할 함수 (7:3 비율 등)
from sklearn.metrics import mean_squared_error, r2_score
# metrics: 모델의 평가 도구(함수) 제공 -> 평균 제곱 오차, 회귀계수^2 정수화 등

##########################
## load_diabetes
##########################

diabetes = load_diabetes() # 객체 반환 : X변수, y변수, 관련자료    
dir(diabetes)
'''
['DESCR',: 설명문
 'data', : x변수
 'data_filename',
 'feature_names',: X변수 각 칼럼 이름
 'frame',
 'target',: y변수 
 'target_names': y변수 범주 이름 (범주형인 경우만 사용 가능)
 'target_filename']: y변수 파일 이름
'''
diabetes.feature_names # ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
X=diabetes.data # 정규화(스케일링 O)
X.shape # (442, 10) = 칼럼(X변수) 10개 존재 의미
diabetes.target_filename
y=diabetes.target
y.shape # (442,)

# 1. dataset load 
X, y = load_diabetes(return_X_y = True) # X변수, y변수 반환  
type(X) # numpy.ndarray
X.shape # (442, 10) = 칼럼(X변수) 10개 존재 의미 - 2d
y.shape # (442,) - 1d

# 2. 변수 특징 
# X변수 : 정규화(0)
# 표준화 여부 확인
X.mean() # -1.6638274468590581e-16
# 정규화 여부 확인
X.min() # -0.137767225690012
X.max() # 0.198787989657293

# y변수 : 정규화(x)
y.mean() # 152.13348416289594
y.min() # 25.0
y.max() # 346.0


# 3. train_test_split(70% vs 30%)
X_train,X_test,y_train,y_test = train_test_split(X, y, 
                                    test_size=0.3, # 기본: 0.25
                                    random_state=123) 
# test_size: 평가 데이터 비율 (기본값: 25%)
# random_state: seed값 지정 (동일한 값으로 랜덤 샘플링)

X_train.shape # 훈련 데이터: (309, 10)
X_test.shape # 평가 데이터: (133, 10)
y_train.shape # (309,)
y_test.shape # (133,)

# 4. model 생성 
lr = LinearRegression() # object
model = lr.fit(X=X_train, y=y_train) # 지도학습 

# 한 문장으로 표현
type(LinearRegression())
model=LinearRegression().fit(X=X_train,y=y_train)
dir(model)
'''
- 'coef_': 회귀계수(X 기울기)
- 'intercept_': y절편
- 'predict': 모델을 이용한 훈련 데이터(y) 예측치
- 'score': 결정계수의 점수

'''
model.coef_ # 10개의 각 X변수 별 기울기
'''
array([  10.45384922, -261.16601105,  538.84541221,  280.72544466,
       -855.21447839,  472.17305267,  166.51881384,  309.88763264,
        684.0489522 ,  102.37723262])
'''
model.intercept_ # y절편
'''152.61083063288848'''

# 5. model 평가  
y_pred = model.predict(X=X_test) # 예측치 
y_true = y_test # 관측치(정답)

# 1) 평균제곱오차(MSE): 0 수렴 정도로 모델 평가 (0에 가까울 수록 예측력 좋음)
# mean((y_true-y_pred)^2)
# 값이 높은 것은 평균 제곱 오차가 높은 것으로 표현
# 스케일링되지 않은 큰 값의 경우, 평가지표로 평균제곱오차는 부적절함
MSE = mean_squared_error(y_true, y_pred)
print('MSE =', MSE)
# MSE = 2926.800577246883

# 2) 결정계수(R-제곱): 1 수렴 정도로 모델 평가 (1에 가까울 수록 예측력 좋음)
score = r2_score(y_true, y_pred) # (관측치,예측치)
print('r2 score =', score) 
# r2 score = 0.5078285584893742
# 모델의 예측력이 중간정도

# 결정계수 제곱 제공 메서드
model.score(X=X_train, y=y_train) # 0.5174979976746197
model.score(X=X_test, y=y_test) # 0.5078285584893742
# train이 test보다 결정계수 높음
# 그러나 두 train과 test 간 차이가 적어 overfitting(과적합) 없이 모델이 생성되었음을 알 수 있음
# 모델의 훈련과 평가 셋 간 결정계수 제곱 차이가 없으면 일반화가 되었음을 알 수 있음


################################
## iris
################################

iris=datasets.load_iris()
dir(iris)
'''
['DESCR',: 설명
 'data',: x변수
 'feature_names',: x변수 칼럼명
 'filename',
 'frame',
 'target',: y벼수
 'target_names']: y변수 범주형
'''

# 1. dataset load
X, y = datasets.load_iris(return_X_y=True)
X.shape # (150, 4)
y.shape # (150,)

# 2. 변수 선택: X(4) -> y=X(3), x=X(1,2,4)
y=X[:,2]
X=X[:,[0,1,3]]
X.shape # (150, 3)

y.mean() # 3.7580000000000005
X.mean() # 3.3666666666666667

# 3. dataset split (70% vs 30%)
X_train,X_test,y_train,y_test=train_test_split(X,y,
                                               test_size=0.3,
                                               random_state=123)

# 4. model 생성: train set 이용
model=LinearRegression().fit(X=X_train,y=y_train)
dir(model)

# 독립변수(X) 기울기
model.coef_ # array([ 0.75572271, -0.6715641 ,  1.43222782])
# y 절편
model.intercept_ # -0.3150495624708074

# 5. model 평가: test set 이용

y_true=y_test
y_pred=model.predict(X=X_test)

# 1) MSE: 0에 수렴정도
# 정규화된 변수만 사용 가능
MSE = mean_squared_error(y_true, y_pred)
print('MSE =', MSE)
# MSE = 0.12397491396059149

# 2) 결정계수 (R^2): 1에 수렴정도 -> 1에 가까울 수록 예측력이 좋음
# 어떤 변수도 상관 없음
score = r2_score(y_true, y_pred)
print('r2 score =', score) 
# r2 score = 0.9643540833169767

# 3) model.score(): 두 훈련 및 평가 데이터 결정계수 비교 (과적합 검증)
train_score=model.score(X=X_train, y=y_train) # r2 score와 동일
test_score=model.score(X=X_test, y=y_test) 
print('train_score =',train_score,',','test_score =',test_score)
# train_score = 0.9694825528782403 , test_score = 0.9643540833169767
# 과적합 없음
# [해설] 모델의 예측력이 매우 좋으며, 모델의 일반화가 가능함을 알 수 있다.

# 4) 시각화 도구 사용
import matplotlib.pyplot as plt
plt.plot(y_pred,color='r',linestyle='--',label='y_predict')
plt.plot(y_true,color='b',linestyle='-.',label='y_true')
plt.legend(loc='best')
plt.show()

# 5) 상관계수 평가: 예측치와 관측치 이용 DF 생성
df = pd.DataFrame({'y_pred':y_pred, 'y_true': y_true})
# 상관계수 : 모델 평가
corr = df['y_pred'].corr(df['y_true'])
print('corr : ', corr) # 0.982389096596606
