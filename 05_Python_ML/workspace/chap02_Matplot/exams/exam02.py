'''
문2) dataset.csv 파일을 이용하여 교차테이블과 누적막대차트를 그리시오.
  <조건1> 성별(gender)과 만족도(survey) 칼럼으로 교차테이블  작성 
  <조건2> 교차테이블 결과를 대상으로 만족도 1,3,5만 선택하여 데이터프레임 생성   
  <조건3> 생성된 데이터프레임 대상 칼럼명 수정 : ['seoul','incheon','busan']
  <조건4> 생성된 데이터프레임 대상  index 수정 : ['male', 'female']     
  <조건5> 생성된 데이터프레임 대상 누적가로막대차트 그리기
'''

import pandas as pd
import matplotlib.pyplot as plt


path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data' # 경로 지정

dataset = pd.read_csv(path + '/dataset.csv')
dataset.info()
'''
 0   resident  217 non-null    int64  
 1   gender    217 non-null    int64  
 2   job       205 non-null    float64
 3   age       217 non-null    int64  
 4   position  208 non-null    float64
 5   price     217 non-null    float64
 6   survey    217 non-null    int64 
'''

# <조건1> 성별(gender)과 만족도(survey) 칼럼으로 교차테이블  작성 
tab=pd.crosstab(index=dataset['gender'],columns=dataset['survey'])
tab
'''
survey   1   2   3   4  5
gender                   
1       10  51  44  13  5
2        4  36  42  11  1
'''

# <조건2> 교차테이블 결과를 대상으로 만족도 1,3,5만 선택하여 데이터프레임 생성   
new_tab=tab.iloc[:,[0,2,4]]
new_tab
'''
survey   1   3  5
gender           
1       10  44  5
2        4  42  1
'''

# <조건3> 생성된 데이터프레임 대상 칼럼명 수정 : ['seoul','incheon','busan']
new_tab.columns=['seoul','incheon','busan']
'''
        seoul  incheon  busan
gender                       
1          10       44      5
2           4       42      1
'''

# <조건4> 생성된 데이터프레임 대상  index 수정 : ['male', 'female']     
new_tab.index=['male', 'female']     
'''
        seoul  incheon  busan
male       10       44      5
female      4       42      1
'''

# <조건5> 생성된 데이터프레임 대상 누적가로막대차트 그리기
new_tab.plot(kind='barh',stacked=True)

