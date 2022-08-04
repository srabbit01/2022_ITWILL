# -*- coding: utf-8 -*-
"""
step03_func_app.py

함수 응용 
1. 텍스트 전처리 함수 정의 
2. 통계 계산 함수 : 표본의 분산/표준편차 
"""

# 전처리 대상 텍스트
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']
print(texts)
# 1. 텍스트 전처리 함수 정의 
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
clean_text(texts)
'''
['우리나라 대한민국 우리나라 만세',
 '비아그라 gram 정력 최고',
 '나는 대한민국 사람',
 '보험료 원에 평생 보장 마감 임박',
 '나는 홍길동']
'''

# 2. 통계 처리 함수 : 표본의 분산/표준편차 계산 함수
dataset = [2,4,5,6,1,8]

# 표본 분산과 표준편차 
from statistics import mean, variance, sqrt
from statistics import *

print('표본 분산 =', variance(dataset))
# 표본 분산 = 6.666666666666666
print('표본 표준편차 =', sqrt(variance(dataset)))
# 표본 표준편차 = 2.581988897471611
'''
표본 분산 = sum((x변량-산술평균)**2) / n-1
         = sum([(d-a)**2 for d in 변수])/(len(변수)-1)
표본 표준편차 = sqrt(표본분산)
'''
def avg(dataset):
    return mean(dataset) # 평균 반환
def var_sd(dataset):
    a=avg(dataset) # 함수 -> 외부 함수 호출
    # print('avg =',a) # avg = 4.33333333
    diff=[(data-a)**2 for data in dataset] # list 내포
    var=sum(diff)/(len(dataset)-1)
    sq=sqrt(var)
    return var, sq
var, sq = var_sd(dataset)
print('분산: ',var,'표준편자: ',sq)
# 분산:  6.666666666666666 표준편자:  2.581988897471611



# 이외 함수 사용
max(dataset)
min(dataset)
median(dataset)
quantiles(dataset) # [1.75, 4.5, 6.5]
data=[1,1,1,1,2,2,3,4,3,3,4,3,4]
mode(data)
