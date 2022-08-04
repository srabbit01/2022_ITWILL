'''
Naive Bayes 이론에 근거한 통계적 분류기
 1. GaussianNB  : x변수가 연속형이고, 정규분포인 경우 
 2. BernoulliNB  : x변수가 이진(binary) 데이터인 경우(x변수가 0과 1인 더미변수)
 3. MultinomialNB : x변수가 단어 빈도수(텍스트 데이터)를 분류할 때 적합

관련 문서 : 
https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html
https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.BernoulliNB.html 
https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html
'''


# <조건부 확률> 
# 사건A 발생 확률 -> 사건B 발생 영향  
# 두 사건의 발생확률 사이의 관계 표현 
# ex) 사건 A가 발생한 경우 사건 B가 읽어날 확률 
# P(B|A) = P(A|B).P(B) / P(A) : 확률의 곱셈 법칙 


# example : 날씨와 비 관계 ppt-15참고 
'''
      yes   no    합  
맑은날  2     8    10
흐린날  6     4    10
 합    8     12   20
''' 

# 1. 사전확률 : 사전에 알고 있는 확률 
# 비가 온 확률 
Pyes = 8/20 # 0.4

# 비가 안온 확률 
Pno = 12/20 # 0.6= 1-p_yes(~p_yes)

# 2. 배반사건(둘 중 하나의 상태만 가능한 경우) 전체 합 = 1 
p_tot = Pyes + Pno # 1.0 

 
# 3. 조건부확률 : P(B|A) = P(A|B).P(B) / P(A) 

# ex1) 맑은날(A) 비가 온(B) 확률
# p(yes|맑은날) = p(맑은날|yes) * p(yes) / p(맑은날)
'''
p(맑은날|yes) : 비가 온 경우 맑은 날 = 2/8
p(yes) = 8/20 : 사전확률 
p(맑은날) = 10/20 : 사전확률  
'''
p = (2/8) * (8/20) / 0.5 #(10/20)
p # 0.2
# [해설] 맑은날에 비가 올 확률 : 20%

# ex2) 흐린날(A) 비가 온(B) 확률
# p(yes|흐린날) = p(흐린날|yes) * p(yes) / p(흐린날)

p = (6/8) * Pyes / 0.5 # (10/20)
p # 0.6
# [해설] 흐린 날에 비가 올 확률 : 60%