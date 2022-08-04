'''  
문5) irsi.csv 데이터셋을 이용하여 다중선형회귀모델을 생성하시오.
   <조건1> 칼럼명에 포함된 '.' 을 '_'로 수정   
      iris.columns = iris.columns.str.replace('.', '_')   
   <조건2> model의 formula 구성 
      y변수 : 1번째 칼럼, x변수 : 2 ~ 3번째 칼럼       
   <조건3> 회귀계수 확인    
   <조건4> 회귀모델 결과 확인 및 해석  : summary()함수 이용 
'''

import pandas as pd
import statsmodels.formula.api as sm # 다중회귀모델 
from statsmodels.formula.api import ols

path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data'


# dataset 가져오기  
iris = pd.read_csv(path + '/iris.csv')
print(iris.head())

# 1. iris 칼럼명 수정 
iris.columns = iris.columns.str.replace('.', '_')
iris.info()

# 2. formula 구성 및 다중회귀모델 생성  
obj = ols(formula='Sepal_Length~Sepal_Width+Petal_Length', data = iris)
model=obj.fit()

# 3. 회귀계수 확인 
model.params
'''
Intercept       2.249140
Sepal_Width     0.595525
Petal_Length    0.471920
'''

# 4. 회귀모델 결과 확인 및 해석 
y_pre=model.fittedvalues
y_real=iris.Sepal_Length

df=pd.DataFrame({'y_true':y_real,'y_pred':y_pre},columns=['y_true','y_pred'])
df.head()
'''
   y_true    y_pred
0     5.1  4.994165
1     4.9  4.696402
2     4.7  4.768315
3     4.6  4.803147
4     5.0  5.053717
'''

import matplotlib.pyplot as plt
plt.plot(y_pre[:50],label='predicted values')
plt.plot(y_real[:50],label='real values')
plt.legend(loc='best')
plt.show()