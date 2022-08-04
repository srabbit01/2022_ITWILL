'''
문4) score 데이터셋을 이용하여 단순선형회귀모델을 이용하여 가설검정으로 수행하시오.

   귀무가설 : academy는 score에 영향을 미치지 않는다.
   대립가설 : academy는 score에 영향을 미친다.

   <조건1> y변수 : score, x변수 : academy      
   <조건2> 회귀모델 생성과 결과확인(회귀계수, 설명력, pvalue, 표준오차) 
   <조건3> 회귀선 적용 시각화 
'''

from scipy import stats
import pandas as pd

path=r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data'

# dataset 가져오기 
score = pd.read_csv(path + '/score_iq.csv')
print(score.info())
'''
 0   sid      150 non-null    int64
 1   score    150 non-null    int64
 2   iq       150 non-null    int64
 3   academy  150 non-null    int64
 4   game     150 non-null    int64
 5   tv       150 non-null    int64
 '''
print(score.head())

# 1. x,y 변수 선택
x=score.academy
y=score.score

# 2. 단순 선형회귀분석(stats)
model=stats.linregress(x=x,y=y)
'''
LinregressResult(slope=4.847829398324446, intercept=68.23926884996192, rvalue=0.8962646792534938, pvalue=4.036716755167992e-54, stderr=0.1971936807753301, intercept_stderr=0.4551145851500148)
'''

# 3. 회귀선 시각화  
from scipy import polyval
from pylab import plot, title, legend, show

# 산점도 
plot(x,y,'b.')
# 회귀선 
y_pre=model.slope*x+model.intercept
plot(x,y_pre, 'r.-')
title('line regression') # 제목 
legend(['x y scatter', 'line regression']) # 범례 
show()
