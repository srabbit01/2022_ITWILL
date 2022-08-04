'''
공분산 vs 상관계수 
 
1. 공분산 : 두 확률변수 간의 분산(평균에서 퍼짐 정도)를 나타내는 통계 
  - 식 : Cov(X,Y) = sum( (X-x_bar) * (Y-y_bar) ) / n
 
  - Cov(X, Y) > 0 : X가 증가할 때 Y도 증가
  - Cov(X, Y) < 0 : X가 증가할 때 Y는 감소
  - Cov(X, Y) = 0 : 두 변수는 선형관계 아님(서로 독립적 관계) 
  - 문제점 : 값이 큰 변수에 영향을 받는다.(값 큰 변수가 상관성 높음)
    
2. 상관계수 : 공분산을 각각의 표준편차로 나눈어 정규화한 통계
   - 공분산 문제점 해결 
   - 부호는 공분산과 동일, 값은 절대값 1을 넘지 않음(-1 ~ 1)    
   - 식 : Corr(X, Y) = Cov(X,Y) / std(X) * std(Y)
'''

import pandas as pd 
score_iq = pd.read_csv(r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML/data/score_iq.csv')
print(score_iq)


# 1. 피어슨 상관계수 행렬 
corr = score_iq.corr(method='pearson')
print(corr)
'''
              sid     score        iq   academy      game        tv
sid      1.000000 -0.014399 -0.007048 -0.004398  0.018806  0.024565
score   -0.014399  1.000000  0.882220  0.896265 -0.298193 -0.819752
iq      -0.007048  0.882220  1.000000  0.671783 -0.031516 -0.585033
academy -0.004398  0.896265  0.671783  1.000000 -0.351315 -0.948551
game     0.018806 -0.298193 -0.031516 -0.351315  1.000000  0.239217
tv       0.024565 -0.819752 -0.585033 -0.948551  0.239217  1.000000
'''
type(corr) # pandas.core.frame.DataFrame
corr.loc['score']
'''
sid       -0.014399
score      1.000000
iq         0.882220
academy    0.896265
game      -0.298193
tv        -0.819752
Name: score, dtype: float64
'''
score_iq.corr(method='pearson').loc['score']
 
# 2. 공분산 행렬 
cov = score_iq.cov()
print(cov)
'''
                 sid      score         iq   academy      game        tv
sid      1887.500000  -4.100671  -2.718121 -0.231544  1.208054  1.432886
score      -4.100671  42.968412  51.337539  7.119911 -2.890201 -7.214586
iq         -2.718121  51.337539  78.807338  7.227293 -0.413691 -6.972975
academy    -0.231544   7.119911   7.227293  1.468680 -0.629530 -1.543400
game        1.208054  -2.890201  -0.413691 -0.629530  2.186309  0.474899
tv          1.432886  -7.214586  -6.972975 -1.543400  0.474899  1.802640
'''

# 특정 칼럼 기준 공분산 혹은 상관계수 적용
score_iq['score'].corr(score_iq['iq']) # 0.88222034461347

# 3. 공분산 vs 상관계수 식 적용 

#  1) 공분산 : Cov(X, Y) = sum( (X-x_bar) * (Y-y_bar) ) / n(N)
X = score_iq['score']
Y = score_iq['iq']

# 표본평균 
x_bar = X.mean()
y_bar = Y.mean()

# 표본의 공분산 
Cov = sum((X - x_bar)  * (Y - y_bar)) / (len(X)-1) # (N-1)
print('Cov =', Cov) 
# Cov = 51.33753914988811

# 2) 상관계수 : Corr(X, Y) = Cov(X,Y) / std(X) * std(Y)
# 표준편차 구하기
stdX = X.std()
stdY = Y.std()
# 표본의 상관계수
Corr = Cov / (stdX * stdY)
print('Corr =', Corr) 
# Corr = 0.8822203446134699
# 상관계수 수정


