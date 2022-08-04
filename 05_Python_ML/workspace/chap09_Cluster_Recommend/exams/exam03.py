# -*- coding: utf-8 -*-
"""
문) food 데이터셋을 대상으로 작성된 피벗테이블(pivot table)을 보고 'g' 사용자가 아직
    섭취하지 않은 음식을 대상으로 추천하는 모델을 생성하고, 추천 결과를 확인하시오. 
"""

import pandas as pd
from surprise import SVD # SVD model 생성 
from surprise import Reader, Dataset # SVD data set 생성 


# 1. 데이터 가져오기 
path=r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML"
food = pd.read_csv(path+'/data/food.csv')
print(food.info()) #    uid(user)  menu(item) count
'''
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   uid     61 non-null     object
 1   menu    61 non-null     object
 2   count   61 non-null     int64 
dtypes: int64(1), object(2)
'''

# 2. 피벗테이블 작성 
ptable = pd.pivot_table(food, 
                        values='count',
                        index='uid',
                        columns='menu', 
                        aggfunc= 'mean') # 평균
'''
aggfunc: 함수 적용 시, 함수 이름 입력
'''
ptable
max(ptable.describe().max())
min(ptable.describe().min())

# 3. rating 데이터셋 생성    
help(Reader)
reader = Reader(rating_scale=(0.99,6))
data = Dataset.load_from_df(food, reader)

# 4. train/test set 생성 
from surprise.model_selection import train_test_split
trainset, testset = train_test_split(data, random_state=0)


# 5. model 생성 : train set 이용 
svd_model= SVD(random_state=123).fit(trainset)


# 6. 'g' 사용자 대상 음식 추천 예측 
uid='g'
iid=ptable.columns
r_rat=ptable.iloc[-1,:]
for i_id, rrat in zip(iid,r_rat):
    result=svd_model.predict(uid,i_id,rrat)
    print(result)
'''
user: g          item: 감자         r_ui = 1.00   est = 2.99   {'was_impossible': False}
user: g          item: 달걀후라이   r_ui = 3.00   est = 3.08   {'was_impossible': False}
user: g          item: 식빵         r_ui = nan   est = 3.50   {'was_impossible': False}
user: g          item: 우유         r_ui = nan   est = 3.15   {'was_impossible': False}
user: g          item: 치킨         r_ui = nan   est = 3.26   {'was_impossible': False}
'''
# '식빵' 추천

