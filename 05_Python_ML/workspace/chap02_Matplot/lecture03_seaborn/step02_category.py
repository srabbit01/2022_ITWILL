# -*- coding: utf-8 -*-
"""
step02_category.py

1. object vs category = 범주형 변수
    - 공통점: 자료형 모두 문자열(string)
    - object: 셀 수 없는 문자열
    - category: 셀 수 있는 문자열 -> level 순서 (숫자배열 순서)
2. 범주형 자료 시각화 
"""

import matplotlib.pyplot as plt
import seaborn as sn


# 1. object vs category

# dataset load
titanic = sn.load_dataset('titanic')

print(titanic.info())
'''
 #   Column       Non-Null Count  Dtype   
---  ------       --------------  -----   
 0   survived     891 non-null    int64   
 1   pclass       891 non-null    int64   
 2   sex          891 non-null    object  
 3   age          714 non-null    float64 
 4   sibsp        891 non-null    int64   
 5   parch        891 non-null    int64   
 6   fare         891 non-null    float64 
 7   embarked     889 non-null    object  
 8   class        891 non-null    category
 9   who          891 non-null    object  
 10  adult_male   891 non-null    bool    
 11  deck         203 non-null    category
 12  embark_town  889 non-null    object  
 13  alive        891 non-null    object  
 14  alone        891 non-null    bool  
 '''
# object vs category
# 공통점: 문자형
# 차이점
# - object: 일반 문자
# - category: 범주형(집단화된 객체) -> 순서(level 존재)
titanic['class']
# Categories (3, object): ['First', 'Second', 'Third'] -> level로 수치화 가능
# 필요에 따라 레벨 수정 가능

# subset 만들기 
df = titanic[['survived','age','class','who']]
df.info()
'''
 0   survived  891 non-null    int64   
 1   age       714 non-null    float64 
 2   class     891 non-null    category
 3   who       891 non-null    object 
'''
df.head()
'''
   survived   age  class    who
0         0  22.0  Third    man
1         1  38.0  First  woman
2         1  26.0  Third  woman
3         1  35.0  First  woman
4         0  35.0  Third    man
'''

# category형 정렬 -> 레벨에 따라 정렬 가능
df.sort_values(by = 'class') # category 오름차순
# Level: First > Second > Third

# object형 정렬 -> 영문자 우선순위에 따라 정렬
df.sort_values(by = 'who') # object 오름차순 
# 영문자 순서: child > man > woman

# object -> category 변경
df['who']=df['who'].astype('category')
df.info()
#  3   who       891 non-null    category

# level 순서 변경: man > woman > child
# cat 멤버 내 set_categories 함수 호출
df['who']=df['who'].cat.set_categories(['man','woman','child'])
# Categories (3, object): ['man', 'woman', 'child'] = Level
df.sort_values(by='who') # 위 순서대로 정렬

# 2. 범주형 자료 시각화 

# 1) 배경 스타일 
sn.set_style(style='darkgrid')
tips = sn.load_dataset('tips')
print(tips.info())

# 2) category형 자료 시각화 
sn.countplot(x = 'smoker', data = tips) # 2개 범주 
plt.title('smoker of tips')
plt.show()

# 범주 별 빈도수
tips['smoker'].value_counts()
'''
No     151
Yes     93
'''

tips['day'].value_counts()
'''
Sat     87
Sun     76
Thur    62
Fri     19
'''
sn.countplot(x = 'day', data = tips) # 2개 범주 
plt.title('day of tips')
plt.show()





