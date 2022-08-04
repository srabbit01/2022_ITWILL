# -*- coding: utf-8 -*-
"""
step02_surprise_movie.py

- 행렬곱 연산하기 위해 k * N의 전치행열 생성 (P 열 수와 Q 행 수 일치 위해)
- P와 Q는 SVD 내부 알고리즘에 의해 계산: 특이값 n개만 지정
- 값이 존재하는 경우에도, 특이값을 이용하여 변환
"""

import pandas as pd # csv file 
from surprise import SVD # SVD model 
from surprise import Reader, Dataset # SVD dataset 
# Reader,Dataset: SVD형 Dataset 생성 (SVD에 적합한 데이터 생성)

# 1. dataset loading 
path=r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML"
ratings = pd.read_csv(path+'/data/movie_rating.csv')
print(ratings) #  평가자[critic]   영화[title]  평점[rating]


# 2. pivot table 작성 : row(영화제목), column(평가자), cell(평점)
print('movie_ratings')
movie_ratings = pd.pivot_table(ratings,
               index = 'title',
               columns = 'critic',
               values = 'rating').reset_index()


# 3. SVD dataset: 모델 입력 전용 데이터셋 생성
# Reader
reader = Reader(rating_scale=(1, 5)) # 평점: 1 ~ 5
'''
rating_scale: 평점 범위 지정
'''
print(reader) # <surprise.reader.Reader object at 주소>

# Dataset
data = Dataset.load_from_df(ratings, reader)
'''
Dataset.load_from_df()
'''
print(data) # <surprise.dataset.DatasetAutoFolds object at 주소>

# 4. train/test set 생성 
# 훈련 데이터 생성
trainset = data.build_full_trainset() # 훈련셋 
# 학습 데이터 생성
testset = trainset.build_testset() # 검정셋 


# 5. SVD model 생성 
model = SVD(random_state=123).fit(trainset) # seed값 적용 


# 6. 전체 사용자 평점 예측치 
# .test 메서드: 입력 데이터에 대한 예측치 출력
all_pred = model.test(testset)
print(all_pred)
'''
Prediction(uid='Gene', iid='Superman', r_ui=5.0, est=3.9251706379498827, details={'was_impossible': False})
- uid: 사용자 이름(id)
- iid: 아이템 이름(id) = 영화 제목
- r_ui: 실제 값 = 실제 평점
- est: 예측 값 = 예측 평점
'''

# 7. Toby 사용자 미관람 영화 추천 예측 
user_id  = 'Toby' # 추천 대상자 지정
items = ['Just My','Lady','The Night'] # 미관람 영화
actual_rating = 0 # 실제 평점 없기 때문에 0으로 초기화

for item_id in items :
    # user_id: 사용자 id, item_id: 아이템 id, actual_rating: 실제 평점
    svd_pred = model.predict(user_id, item_id, actual_rating) # predict: 예측
    print(svd_pred)
'''
user: Toby       item: Just My    r_ui = 0.00   est = 2.88   {'was_impossible': False}
user: Toby       item: Lady       r_ui = 0.00   est = 3.27   {'was_impossible': False}
user: Toby       item: The Night  r_ui = 0.00   est = 3.30   {'was_impossible': False}

- user: 추천 대상자 이름
- item: 아이템 이름
- r_ui: 실제 값 (0.00이면 보통 결측치인 것으로 간주)
- est: 예측 값
'''
# 결과: The Night 영화 추천
'''
유사도(corr) 계산 방식과 비교
           rating      Toby  sim_rating   predict
title                                            
Just My       9.5  3.190366    8.074754  2.530981
Lady         11.5  2.959810    8.383808  2.832550
The Night    16.5  3.853215   12.899752  3.347790 -> 추천영화 
'''



