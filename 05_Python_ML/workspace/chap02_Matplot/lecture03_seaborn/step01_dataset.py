# -*- coding: utf-8 -*-
"""
step01_dataset.py

Seaborn : Matplotlib 기반 다양한 배경 테마, 통계용 차트 제공 
커널 밀도(kernel density), 카운트 플롯, 다차원 실수형 데이터,2차원 카테고리 데이터
2차원 복합 데이터(box-plot), heatmap, catplot 
"""

import seaborn as sn # 별칭 

# 1. 데이터셋 확인 
names = sn.get_dataset_names() # seaborn에서 제공하는 dataset 이름 확인
print(names) # list 형태로 제공
'''
['anagrams', 'anscombe', 'attention', 'brain_networks', 'car_crashes', 'diamonds', 'dots', 'exercise', 'flights', 'fmri', 'gammas', 'geyser', 'iris', 'mpg', 'penguins', 'planets', 'taxis', 'tips', 'titanic']
'''

# 2. 데이터셋 로드 
iris = sn.load_dataset('iris') # seaborn dataset 메모리상 로딩
type(iris) # pandas.core.frame.DataFrame
print(iris.info())
'''
 0   sepal_length  150 non-null    float64
 1   sepal_width   150 non-null    float64
 2   petal_length  150 non-null    float64
 3   petal_width   150 non-null    float64
 4   species       150 non-null    object 
'''

iris.head()
iris.tail()

# tips
tips=sn.load_dataset('tips')
tips.info()

# titanic
titanic=sn.load_dataset('titanic')
titanic.info()

