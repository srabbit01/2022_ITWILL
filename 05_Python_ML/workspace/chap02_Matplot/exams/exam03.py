# -*- coding: utf-8 -*-
'''
문3) seaborn의  titanic 데이터셋을 이용하여 다음과 같이 단계별로 시각화하시오.
  <단계1> 'survived','pclass', 'age','fare' 칼럼으로 서브셋 만들기
  <단계2> 'survived' 칼럼을 집단변수로 하여 'pclass', 'age','fare' 칼럼 간의 산점도행렬 시각화
  <단계3> 산점도행렬의 시각화 결과 해설하기              

문4) seaborn의 tips 데이터셋을 이용하여 다음과 같이 단계별로 시각화하시오.
   <단계1> 'total_bill','tip','sex','size' 칼럼으로 서브셋 만들기 
   <단계2> 성별(sex) 칼럼을 집단변수로 하여 total_bill, tip, size 칼럼 간의 산점도행렬 시각화 
   <단계3> 산점도행렬의 시각화 결과 해설하기 
'''

import matplotlib.pyplot as plt
import seaborn as sn

# 문3) seaborn의  titanic 데이터셋을 이용하여 다음과 같이 단계별로 시각화하시오.
titanic = sn.load_dataset('titanic')
print(titanic.info())

# 칼럼명 수정 : 'survived','pclass', 'age','fare'
#  <단계1> 'survived','pclass', 'age','fare' 칼럼으로 서브셋 만들기  
tit_sub=titanic[['survived','pclass', 'age','fare']]

# <단계2> 'survived' 칼럼을 집단변수로 하여 'pclass', 'age','fare' 칼럼 간의 산점도행렬 시각화
sn.pairplot(data=tit_sub,hue='survived')

# <단계3> 산점도행렬에서 pclass, age, fare와 survived 변수의 관계 해설
# pclass: 클래스가 낮을 수록 사망자 증가
# age: 어릴 수록 사망률 및 생존률 증가
# fare: 비용 낮을 수록 사망률 매우 증가


# 문4) seaborn의 tips 데이터셋을 이용하여 다음과 같이 단계별로 시각화하시오.
tips = sn.load_dataset('tips')
print(tips.info())

# <단계1> 'total_bill','tip','sex','size' 칼럼으로 서브셋 만들기
tips_sub=tips[['total_bill','tip','sex','size']]

# <단계2> 성별(sex) 칼럼을 집단변수로 산점도행렬 시각화 
sn.pairplot(data=tips_sub,hue='sex')

# <단계3> 산점도행렬에서 total_bill과 tip의 관계를 설명하고 추가로 sex 변수의 관계 해설
# total_bill and tip: tip이 증가할 수록 total_bill 증가
# total_bill and tip 둘 다 남성의 비율이 여성보다 높음


