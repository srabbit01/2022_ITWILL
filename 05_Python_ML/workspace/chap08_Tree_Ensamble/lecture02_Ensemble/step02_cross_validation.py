'''
교차검정(cross validation)
 - 전체 dataset을 n등분 
 - 검정셋과 훈련셋을 서로 교차하여 검정하는 방식 
 홀드아웃검정
 - train set과 test set 하나만 만들어 train으로 모델 생성 후, test로 모델 평가
'''

from sklearn.datasets import load_digits # 0~9 손글씨 이미지 
from sklearn.model_selection import cross_validate # cross validation 
# model_selection: train_test_split(홀드아웃검정), cross_validate(교차검정)
# -> 검정수행 도구 들어있음
from sklearn.ensemble import RandomForestClassifier # RM
from sklearn.metrics import accuracy_score # 평가 

# 1. dataset load 
digits = load_digits()

X = digits.data
y = digits.target

X.shape # (1797, 64) = (image size, pixel)
y.shape # (1797,) = 10진수 정답
y # array([0, 1, 2, ..., 8, 9, 8]) = Label Encoding


# 2. model 생성 
rfc = RandomForestClassifier() # default 적용(100개 tree) 
model = rfc.fit(X, y) # fulldata 적용  

# 예측치 : class 
y_pred = model.predict(X = X) # image -> 10진수(class) 
y_pred # array([0, 1, 2, ..., 8, 9, 8])

# model 평가 
acc = accuracy_score(y_pred, y)
print(acc) 


# 3. 교차검정 : 균등분할 -> 교차검정 
score = cross_validate(model, X, y, cv=5) # 5겹 교차검정 
print(score)
'''
{'fit_time': array([0.56067705, 0.40079379, 0.42175603, 0.55967712, 0.52971792]),
 'score_time': array([0.02000976, 0.0209868 , 0.01901054, 0.02298903, 0.01898932]),
 'test_score': array([0.93333333, 0.91666667, 0.94986072, 0.96657382, 0.91643454])}
'''
# fit_time: 피팅 시간
# score_time: 점수 매기는 시간
# test_score: 매 실행마다 분류 정확도 (1에 가까울 수록 유리)
acc=score['test_score']
print(acc)
type(acc)

print('최종 산술평균 :',acc.mean())
# 최종 산술평균 : 0.9376911173011452
# 최종결과: 산술 평균


