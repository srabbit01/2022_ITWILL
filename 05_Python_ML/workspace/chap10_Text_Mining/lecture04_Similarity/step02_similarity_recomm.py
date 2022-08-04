# -*- coding: utf-8 -*-
"""
step02_similarity_recomm.py

유사 문서 검색 
- 영화 검색(추천) 시스템 : 코사인 유사도 기반  
"""

import pandas as pd # csv file 
from sklearn.feature_extraction.text import TfidfVectorizer # 희소행렬 
from sklearn.metrics.pairwise import cosine_similarity # 유사도 계산 

# 1. dataset load 
path=r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML"
data = pd.read_csv(path+'/data/movie_reviews.csv') # 1990s ~ 2000s
print(data.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1492 entries, 0 to 1491
Data columns (total 3 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   reviews  1492 non-null   object : 영화후기 
 1   title    1492 non-null   object : 영화제목  
 2   label    1492 non-null   int64  : 긍정/부정 
'''
print(data.head())

    
# 2. 전처리 : 결측치 행 단위 제거 
data_df = data.dropna(axis = 0)
data_df.info()


# 3. Sparse matrix(DTM) : reviews 대상 
obj = TfidfVectorizer(stop_words='english') # 1) 단어생성기 
# stop_words='english': 영어 불용어 제거

# 2) 희소행렬 
movie_sm = obj.fit_transform(data_df['reviews'])
movie_sm.shape # (1492, 34641)

# scipy -> numpy array 
movie_sm_arr = movie_sm.toarray()
movie_sm_arr.shape # (1492, 34641)


title = data_df['title'] # 영화제목 칼럼 추출 

# 4. query 작성 -> DTM -> 유사도 계산 -> 영화 추천(검색) 
def movie_search(query) :
    # 1) query 작성
    query_data = [query] # 문장 -> list 변경 
    
    # 2) query DTM 
    query_sm = obj.transform(query_data)
    query_sm = query_sm.toarray() # scipy -> numpy array
    
    # 3) 유사도 계산 
    sim = cosine_similarity(query_sm, movie_sm_arr) # (query, raw doc)
    print(sim.shape) # (1, 1492)
    sim = sim.reshape(1492) # 2d -> 1d
    
    # 4) 내림차순 정렬 : index 정렬 
    sim_idx = sim.argsort()[::-1]
    print(sim_idx) # [1281 1304  373 ...  906  907    0]
    
    global title # 전역변수 사용 
    
    # 5) Top5 영화추천하기 
    for idx in sim_idx[:5] :
        print(f'similarity : {sim[idx]} \n movie title : {title[idx]}  ')
        
    
# 5. query 적용
movie_search(input('Query : '))
'''
Query : action
similarity : 0.20192921485638887 
 movie title : Soldier (1998)  
similarity : 0.1958404700223592 
 movie title : Romeo Must Die (2000)  
similarity : 0.18885169874338412 
 movie title : Aliens (1986)  
similarity : 0.18489066174805405 
 movie title : Speed 2: Cruise Control (1997)  
similarity : 0.16658803590038168 
 movie title : Total Recall (1990) 
 '''
 '''
 Query : drama
similarity : 0.1931737274266525 
 movie title : Apollo 13 (1995)  
similarity : 0.11796112357272329 
 movie title : Double Jeopardy (1999)  
similarity : 0.11374906390472769 
 movie title : Practical Magic (1998)  
similarity : 0.11037479275255738 
 movie title : Civil Action, A (1998)  
similarity : 0.09607905933279662 
 movie title : Truman Show, The (1998)  
 '''