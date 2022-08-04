# -*- coding: utf-8 -*-
"""
문3) 한국영화 후기(review_data.csv) 파일을 대상으로 아래와 같은 조건으로
키워드를 입력하여 관련 영화 후기를 검색하는 함수를 정의하시오.   

 <조건1> 사용할 칼럼 : review2 
 <조건2> 사용할 문서 개수 : 1번째 ~ 5000번째   
 <조건3> 코사인 유사도 적용 - 영화 후기 검색 함수
         -> 검색 키워드와 가장 유사도가 높은 상위 3개 review 검색  
 <조건4> 검색 키워드 : 액션영화, 시나리오, 중국영화 
        -> 위 검색 키워드를 하나씩 입력하여 관련 후기 검색   
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. dataset load 
path=r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML"
data = pd.read_csv(path+"/data/review_data.csv")
data.info() 
'''
 0   id       34525 non-null  int64 
 1   review   34525 non-null  object
 2   label    34525 non-null  int64 
 3   review2  34525 non-null  object -> 사용할 칼럼 
'''
print(data.head())


# 사용할 문서 5,000개 제한  
review = data.review2[:5000] # 1번째 ~ 5000번째 문서 


# 2. sparse matrix 생성 : overview 칼럼 대상 
odj=TfidfVectorizer()
sparse_mat=obj.fit_transform(review)
sparse_arr=sparse_mat.toarray()


# 3. cosine 유사도 : 영화 후기 검색 함수  
def review_search(query) : 
    query=[query]
    new_sparse_mat=obj.transform(query)
    new_sparse_arr=new_sparse_mat.toarray()
    sim=cosine_similarity(new_sparse_arr,sparse_arr)
    sim=sim.reshape(len(review))
    # sim=sim.squeeze(): 차원수가 1인 차원 제거
    sim_idx=sim.argsort()[::-1]
    for i in sim_idx[:3]: # 유사도 top 3
        print(f'similarity : {sim[i]}, sentences : {review[i]}')


# 4. 검색 키워드 : 액션영화, 시나리오, 중국영화   
review_search(input('검색할 키워드 입력 : '))
'''
검색할 키워드 입력 : 액션영화, 시나리오, 중국영화
similarity : 0.3456726236541288, sentences : 최고의영화죠 시나리오 굿
similarity : 0.34278550647701705, sentences : 스웨덴식 액션영화 강추
similarity : 0.2689603738342434, sentences : 시나리오 쓰신 분 정말 존경스럽네요 
'''




