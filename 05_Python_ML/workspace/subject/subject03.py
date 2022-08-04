"""
문) 영행렬(zero matrix)을 이용하여 희소행렬(sparse matrix) 만들기

     [단계1] 단어 생성
     [단계2] 영행렬(zeros matrix) 만들기
     [단계3] 데이터프레임(DataFrame) 만들기
     [단계4] 희소행렬(sparse matrix) 만들기 

 <출력결과 예시> 
   홍길동   정력  우리나라  대한민국   최고  보험료  비아그라   평생   사람   만세   나는   마감   임박   보장
0  0.0  0.0   2.0   2.0  0.0  0.0   0.0  0.0  0.0  1.0  0.0  0.0  0.0  0.0
1  0.0  1.0   0.0   0.0  1.0  0.0   1.0  1.0  0.0  0.0  0.0  0.0  0.0  1.0
2  0.0  0.0   0.0   1.0  0.0  0.0   0.0  0.0  1.0  0.0  1.0  0.0  0.0  0.0
3  0.0  0.0   0.0   0.0  0.0  1.0   0.0  1.0  0.0  0.0  0.0  1.0  1.0  1.0
4  1.0  0.0   0.0   1.0  1.0  0.0   0.0  0.0  0.0  0.0  1.0  0.0  0.0  0.0
"""

# 사용할 수 있는 패키지 
import numpy as np # 영향렬(zeros matrix) 만들기 
import pandas as pd  # 데이터프레임(DataFrame) 만들기


## 주어진 texts : texts.txt(카페에서 다운로드)
path=r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML'
file=open(path+r'\data\texts.txt')
pd_text=pd.DataFrame(file)
print(pd_text)

# 전처리
texts = pd_text[0]

print('전처리 전')
print(texts)

# << texts 전처리 함수 >> 
import string 
def text_prepro(texts): 
    # Lower case: 소문자
    texts = [x.lower() for x in texts]
    # Remove punctuation: 문장부호 제거  
    texts = [''.join(ch for ch in st if ch not in string.punctuation) for st in texts]
    # Remove numbers: 숫자 제거
    texts = [''.join(ch for ch in st if ch not in string.digits) for st in texts]
    # Trim extra whitespace: 2칸 이상 공백 -> 1칸 변경
    texts = [' '.join(x.split()) for x in texts]
    return texts

# 함수 호출
texts = text_prepro(texts)
print('전처리 후 ')
print(texts)

## 단계1 : 단어 생성 
from sklearn.feature_extraction.text import TfidfVectorizer
obj = TfidfVectorizer() # 단어 생성기 
fit = obj.fit(texts)
voca = fit.vocabulary_
print(voca)

## 단계2 : 영행렬(zeros matrix) 만들기
zmat=np.zeros((len(texts),len(voca)))

# 단계3 : DataFrame 만들기 
zmat_df=pd.DataFrame(zmat)
print(zmat_df)

# 단계4 : 희소행렬 만들기 
sparse_mat=obj.fit_transform(texts)
print(sparse_mat)

# spicy -> array
sparse_arr=sparse_mat.toarray()
print(sparse_arr)

# DataFrame

sparse_df=pd.DataFrame(sparse_arr,columns=voca.keys())
print(sparse_df)
'''
       우리나라      대한민국       만세     비아그라  ...      보험료        마감        임박       홍길동
0  0.000000  0.513870  0.00000  0.38365  ...  0.00000  0.000000  0.000000  0.000000
1  0.000000  0.000000  0.00000  0.00000  ...  0.50298  0.405801  0.405801  0.000000
2  0.556816  0.462208  0.00000  0.00000  ...  0.00000  0.000000  0.000000  0.000000
3  0.000000  0.000000  0.48214  0.00000  ...  0.00000  0.000000  0.388988  0.000000
4  0.486484  0.403826  0.00000  0.00000  ...  0.00000  0.486484  0.000000  0.602985  
'''

# DataFrame 대상, 각 문서의 단어 출현 빈도수 확인
for idx, st in enumerate(texts): # 문장번호, 문장내용
    for word in st.plit(): # 단어 생성
        sparse_df.loc[idx,word]+=1 # 기존 출현 단어
