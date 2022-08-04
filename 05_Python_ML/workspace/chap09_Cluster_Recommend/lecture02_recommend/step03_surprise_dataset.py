'''
surprise Dataset 이용 
'''
import pandas as pd
from surprise import SVD, accuracy # 모델 생성과 평가
from surprise import Dataset  # SVD용 dataset 생성

############################
## suprise Dataset
############################

# 1. dataset download
data = Dataset.load_builtin('ml-100k') # user: 943명, item: 1682개
# Dataset ml-100k could not be found. [Y/n] Enter

# 2. rating dataset 
# .raw_ratings: 정보만 추출
dataset = data.raw_ratings # list 내 tuple
print(len(dataset)) # 100000 
dataset[:10]
'''
   user  item  rating    id
[('196', '242', 3.0, '881250949'),
 ('186', '302', 3.0, '891717742'),
 ('22', '377', 1.0, '878887116'),
 ('244', '51', 2.0, '880606923'),
 ('166', '346', 1.0, '886397596'),
 ('298', '474', 4.0, '884182806'),
 ('115', '265', 2.0, '881171488'),
 ('253', '465', 5.0, '891628467'),
 ('305', '451', 3.0, '886324817'),
 ('6', '86', 3.0, '883603013')]
'''
# pivot table 만들기
# 행: user, 열: item, 값: rating

# 3. train/test split
# 다운로드한 자료가 Reader와 Dataset.load_from_df( )를
# 사용하지 않아도 되는 데이터
from surprise.model_selection import train_test_split

# Dataset 자료이용: 기본 75 vs 25
trainset, testset = train_test_split(data, random_state=0)
# shape은 알 수 없음

# 다른 방법
trainset2 = data.build_full_trainset() # 훈련셋 
testset2 = trainset.build_testset() # 검정셋 

# 4. svd model
svd_model= SVD(random_state=123).fit(trainset)
svd_model2= SVD(random_state=321).fit(trainset2)
dir(svd_model)
'''
test vs predict
- test: 전체 user 평점 예측
- predict: 특정 user 평점 예측 -> item 추천
  - user, item, real rating 모두 입력
'''

# 5. 전체 testset 평점 예측
preds = svd_model.test(testset)
print(len(preds)) # 20,000

# 예측결과 출력 
print('user\tmovie\trating\test_rating')
for p in preds[:5] : 
    print(p.uid, p.iid, p.r_ui, p.est, sep='\t\t')
'''
user    item    실제rat  예측rat
269		17		2.0		2.697369252580903
704		382		4.0		3.425149329906973
829		475		4.0		3.8548670627807327
747		274		4.0		3.9399633165611663
767		98		5.0		4.8264822102570335
'''


# 6. model 평가 
accuracy.mse(preds) # 평균제곱오차 - MSE
# MSE: 0.8976
accuracy.rmse(preds) # 제곱근평균제곱오차
# RMSE: 0.9474


# 7.추천대상자 평점 예측 

# movie rating 만들기 : list -> DF
df = pd.DataFrame(dataset, columns=["user","item","rating","id"])
df.drop("id", axis = 1, inplace = True)
df.head()
'''
  user item  rating
0  196  242   3.0
1  186  302   3.0
2   22  377   1.0
3  244   51   2.0
4  166  346   1.0
'''
df.shape # (100000, 3)

# 행: user, 열: item, 셀: rating
movie_rating = pd.pivot_table(df, 
               values='rating', index='user', columns='item')
print(movie_rating)
movie_rating.shape # (943, 1682)
# 5명의 user와 10개의 item
movie_rating.iloc[:5,:10]
'''
item    1   10  100  1000  1001  1002  1003  1004  1005  1006
user                                                         
1     5.0  3.0  5.0   NaN   NaN   NaN   NaN   NaN   NaN   NaN
10    4.0  NaN  5.0   NaN   NaN   NaN   NaN   NaN   NaN   NaN -> 추천 대상자
100   NaN  NaN  NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN
101   3.0  NaN  NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN
102   3.0  NaN  NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN
# NaN: 평점 정보 없음
# 희소행렬과 비슷
'''

# 10번 사용자 평점 추천
uid='10' # 추천 대상지
iid= movie_rating.columns[:10] # 추천 item: 1 ~ 1006 (10개)
r_ui=movie_rating.iloc[1,:10].fillna(0) # 실제 평점 (NaN -> 0)
print(f'user: {uid}')
for i_id,rat_ui in zip(iid,r_ui): # item 및 real rating 출력
    predict=svd_model.predict(uid, i_id, rat_ui)
    # print(predict)
    print('item: {0:4s}, real rating: {1:.2f}, pred rating: {2:.2f}'.format(predict[1],predict[2],predict[3]))
'''
user             item number      real rating    predict rating
user: 10         item: 1          r_ui = 4.00    est = 4.49   {'was_impossible': False}
user: 10         item: 10         r_ui = 0.00    est = 4.37   {'was_impossible': False}
user: 10         item: 100        r_ui = 5.00    est = 4.47   {'was_impossible': False}
user: 10         item: 1000       r_ui = 0.00    est = 3.66   {'was_impossible': False}
user: 10         item: 1001       r_ui = 0.00    est = 2.94   {'was_impossible': False}
user: 10         item: 1002       r_ui = 0.00    est = 3.10   {'was_impossible': False}
user: 10         item: 1003       r_ui = 0.00    est = 3.40   {'was_impossible': False}
user: 10         item: 1004       r_ui = 0.00    est = 3.71   {'was_impossible': False}
user: 10         item: 1005       r_ui = 0.00    est = 4.09   {'was_impossible': False}
user: 10         item: 1006       r_ui = 0.00    est = 3.49   {'was_impossible': False}
'''
# 2개 이상 변수를 입력하려면 zip 함수 사용
# 양식을 이용한 결과 출력
'''
user: 10
item: 1   , real rating: 4.00, pred rating: 4.49
item: 10  , real rating: 0.00, pred rating: 4.37
item: 100 , real rating: 5.00, pred rating: 4.47
item: 1000, real rating: 0.00, pred rating: 3.66
item: 1001, real rating: 0.00, pred rating: 2.94
item: 1002, real rating: 0.00, pred rating: 3.10
item: 1003, real rating: 0.00, pred rating: 3.40
item: 1004, real rating: 0.00, pred rating: 3.71
item: 1005, real rating: 0.00, pred rating: 4.09 -> 추천 item
item: 1006, real rating: 0.00, pred rating: 3.49
'''
# [결과] item 1005 추천