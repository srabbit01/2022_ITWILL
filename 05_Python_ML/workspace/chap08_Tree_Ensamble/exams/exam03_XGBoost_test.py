'''
 문3) iris dataset을 이용하여 다음과 같은 단계로 XGBoost model을 생성하시오.
'''

import pandas as pd # file read
from xgboost import XGBClassifier # model 생성 
from xgboost import plot_importance # 중요변수 시각화  
import matplotlib.pyplot as plt # 중요변수 시각화 
from sklearn.model_selection import train_test_split # dataset split
from sklearn.metrics import confusion_matrix, accuracy_score,classification_report # model 평가 
from sklearn.preprocessing import LabelEncoder

# 단계1 : data set load 
path=r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML"
iris = pd.read_csv(path+"/data/iris.csv")

# 변수명 추출 
cols=list(iris.columns)
col_x=cols[:4] # x변수명 : ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']
col_y=cols[-1] # y변수명 : Species -> 레이블 인코딩 필요 (하지 않을 시 오류 발생)

# labael encoding
iris['Species']=LabelEncoder().fit_transform(iris.Species)

# 단계2 : 훈련/검정 데이터셋 생성
train_set, test_set = train_test_split(iris, test_size=0.25)


# 단계3 : model 생성 : train data 이용
xgb = XGBClassifier(objective='multi:softprob') # 다항 분류기
eval_set=[(test_set[col_x],test_set[col_y])] # 평가셋
model = xgb.fit(train_set[col_x], train_set[col_y], eval_metric='merror',verbose=True,
                eval_set=eval_set)
print(model)

# 단계4 :예측치 생성 : test data 이용  
y_pred=model.predict(test_set[col_x])

# 단계5 : 중요변수 확인 & 시각화  
# 1) 중요변수 확인
fscore = model.get_booster().get_fscore()
print("fscore:",fscore) 
'''
fscore: {'Sepal.Length': 113.0, 'Sepal.Width': 101.0,
         'Petal.Length': 114.0, 'Petal.Width': 109.0}
'''
# 2) 시각화
plot_importance(model)
plt.show()

# 단계6 : model 평가 : confusion matrix, accuracy, report

# 1) confusion matrix
con_mat=confusion_matrix(y_pred,test_set[col_y])
print(con_mat)
'''
[[12  0  0]
 [ 0 11  1]
 [ 0  0 14]]
'''

# 2) accuracy
y_pred = model.predict(test_set[col_x]) 
acc = accuracy_score(test_set[col_y], y_pred)
print('분류정확도 =', acc)
# 분류정확도 = 0.9736842105263158

# 3) report
report=classification_report(test_set[col_y], y_pred) # 중요변수: "Petal Width"
print(report)
'''
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        12
           1       0.92      1.00      0.96        11
           2       1.00      0.93      0.97        15

    accuracy                           0.97        38
   macro avg       0.97      0.98      0.97        38
weighted avg       0.98      0.97      0.97        38
# 2번째 3번째 종이 겹치는 부분이 있어 분류가 조금 어렵다.
'''