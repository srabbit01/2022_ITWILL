# -*- coding: utf-8 -*-
"""
step07_DataFrame_save.py

1. DataFrame 생성
2. csv file save
"""
import pandas as pd # 별칭

path = 'C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap08_FileIO\\data'

# 1. csv file read
spam_data = pd.read_csv(path+'/spam_data.csv',header=None,encoding='ms949') # 칼럼명 행 없음
# encoding = 'utf-8' or 'ms949' 중 하나가 많음
spam_data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4 -> 5행
Data columns (total 2 columns): -> 2열
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   0       5 non-null      object
 1   1       5 non-null      object
dtypes: object(2)
memory usage: 208.0+ bytes
'''
# 칼럼명이 따로 없으면 자동으로 인덱스 번호 부여
spam_data
'''
      0                        1            -> 칼럼명
0   ham    우리나라    대한민국, 우리나라 만세
1  spam      비아그라 500GRAM 정력 최고!
2   ham               나는 대한민국 사람
3  spam  보험료 15000원에 평생 보장 마감 임박
4   ham                   나는 홍길동
0 = Y, 1 = X (형태소 분석을 하여 어떤 것이 spam인지 ham인지 구별)
'''
target=spam_data[0] # 칼럼명이 숫자(인덱스 번호)인 경우 따옴표 붙이지 않음
print(target)
texts=spam_data[1]
print(texts)
'''
0      우리나라    대한민국, 우리나라 만세
1        비아그라 500GRAM 정력 최고!
2                 나는 대한민국 사람
3    보험료 15000원에 평생 보장 마감 임박
4                     나는 홍길동
-> 자동으로 색인(인덱스 번호) 생성
'''
# Target(Y) 변수 -> 범주형(더미변수)로 만들기
target=[1 if i=='spam' else 0 for i in target]
print(target)

# X변수: 텍스트 -> 텍스트 전처리
# 텍스트 전처리 함수
def clean_text(texts) :        
    from re import sub # re 모듈 가져오기
    
    # 단계1 : 소문자 변경   
    texts_re = [ st.lower() for st in texts]
        
    # 단계2 : 숫자 제거 
    texts_re2 = [sub('[0-9]', '', st) for st in texts_re]    
    
    # 단계3 : 문장부호 제거 
    punc_str = '[,.?!:;]'
    texts_re3 = [sub(punc_str, '', st) for st in texts_re2]    
    
    # 단계4 : 특수문자 제거 
    spec_str = '[@#$%^&*()]'
    texts_re4 = [sub(spec_str, '', st) for st in texts_re3]    
    
    # 단계5 : 2칸 이상 공백(white space) 제거 
    texts_re5 = [' '.join(st.split()) for st in texts_re4 ]
    
    return texts_re5
# 전처리 후
texts_ret=clean_text(texts)
print(texts_ret)

# DataFrame 생성: target, texts
clean_df=pd.DataFrame({'target':target,'texts_ret':texts_ret})
clean_df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 2 columns):
 #   Column     Non-Null Count  Dtype 
---  ------     --------------  ----- 
 0   target     5 non-null      int64 
 1   texts_ret  5 non-null      object
dtypes: int64(1), object(1)
memory usage: 208.0+ bytes
'''
type(clean_df)
print(clean_df)

# csv file save
clean_df.to_csv(path+'/clean_data.csv', index=None, encoding='utf-8')

# csv file read
clean_data_new=pd.read_csv(path+'/clean_data.csv',encoding='utf-8')
print(clean_data_new)

# close() 지원 X -> 'del 파일명'으로 메모리상 제거 의미
# 별도 close 없음 -> file 객체가 아닌 pandas 객체이기 때문
# text 파일은 close 필요