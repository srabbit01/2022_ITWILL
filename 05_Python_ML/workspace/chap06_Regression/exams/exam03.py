'''
문3) load_wine() 함수를 이용하여 와인 데이터를 다항분류하는 로지스틱 회귀모델을 생성하시오. 
  조건1> train/test - 7:3비율
  조건2> y 변수 : wine.target 
  조건3> x 변수 : wine.data
  조건4> 모델 평가 : confusion_matrix, 분류정확도[accuracy]
'''

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# 1. wine 데이터셋 
wine = load_wine()

# 2. 변수 선택 
wine_x = wine.data # x변수 
wine_y = wine.target # y변수: 0~2 -> 10진수(Label Encoding) 완료
# 만일 Label Encoding되지 않으면 전처리 후 진행

# 3. train/test split(7:3)
X_train,X_test,y_train,y_test=train_test_split(wine_x,wine_y,
                                               test_size=0.3,
                                               random_state=111)

# 4. model 생성  : solver='lbfgs', multi_class='auto'
model=LogisticRegression(random_state=111,max_iter=300,verbose=1)
model=model.fit(X=X_train,y=y_train) 

# 5. 모델 평가 : accuracy, confusion matrix

# 1) 분류 정확도
acc=model.score(X_test,y_test)
print('분류정확도 =',acc)
# 분류정확도 = 0.9444444444444444
# [해설] 분류 정확도가 매우 높음을 알 수 있음

# 2) confusion matrix
ytest_pred=model.predict(X=X_test) # y label 예측
ytest_true=y_test

con_mat=confusion_matrix(ytest_true,ytest_pred)
print(con_mat)
'''
[[15  2  0]
 [ 0 21  1]
 [ 0  0 15]]
'''
