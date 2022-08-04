# -*- coding: utf-8 -*-
"""
step02_distribution_test.py

확률분포와 검정(test)

1. 연속확률분포와 정규성 검정 
  - 연속확률분포 : 셀 수 없는 실수값을 갖는 분포
  - 연속확률분포 유형 : 정규분포, 균등분포, 카이제곱, T/Z/F 분포 등
2. 이산확률분포와 이항 검정 
  - 이산확률분포 : 셀 수 있는 정수값을 갖는 분포
  - 이산확률분포 유형 : 베르누이분포, 이항분포, 포아송분포 등 
"""
from scipy import stats # 확률분포 + 검정
import numpy as np # vector data -> 확률분포 곡선을 위한 벡터 데이터 만들기
import matplotlib.pyplot as plt  # 확률분포의 시각화
'''
연속확률분포(Continuous distributions) 생성 메서드
stats.beta : 알파()와 베타() 구간의 연속확률분포
stats.chi2 : 극단값을 허용하는 멱분포이며, 표본 수가 많을수록 대칭 모양을 갖는 확률분포 
stats.f : 두 chi2분포를 각각의 자유도(d.f)로 나눈 비율을 나타낸 분포
stats.norm : 정규분포, 좌우 대칭분포 
stats.t : 표본수가 작은 경우(30개 미만) 정규분포 대신 사용하는 확률분포
stats.uniform : 균등하게 나타나는 확률분포
========================
이산확률분포(Discrete distributions)
stats.bernoulli(베루누이) : 독립시행 1번, 
stats.binom(이항) : 독립시행 n번  
stats.geom(기하):최초 성공할 때 까지 실패한 횟수를 갖는 분포, 
stats.poisson(포아송) : 특정한 사건의 발생 가능성이 매우 작은 확률분포((예 : 특정 시점에서 번개에 맞을 확률))
======================
'''

# 1. 정규분포의 검정(정규성 검정)

# 1) 표준정규분포 객체 생성 
mu, sigma = 0, 1 # 평균=0, 표준편차=1
# 정규분포: N(0,1)
norm_obj = stats.norm(mu, sigma) # stats.norm(평균,표준편차)
print(norm_obj) 

# 2) 확률변수 X : 시행횟수 N을 이용하여 정규분포의 확률변수 
N = 1000 # sample 수 
X = norm_obj.rvs(size = N) # N번 시뮬레이션 : 표본 추출 
# .rvs(size): random value sample -> 표본의 사이즈 만큼 표본 추출
len(X) # 1000
print(X)

# 3) 확률분포 시각화 
from scipy.stats import norm # 확률밀도함수(pdf)

# 확률변수 x의 분포곡선 vector data 
line = np.linspace(min(X), max(X), 100) # -3.2 ~ 3.2
# 최댓값과 최솟값 사이 100개 생성
# np.arange와 비슷
'''
np.arange vs np.linspace
np.arange: 최소 ~ 최대 사이 step 단위 출력 (최대 숫자 제외)
np.linspace: 최소 ~ 최대 사이 n개 균등 분할하여 출력 (최대 숫자 포함)

'''

# 확률밀도함수(pdf): 확률변수 X의 크기 추정
dline=norm.pdf(line, mu, sigma) # norm.pdf(곡선변수,평균,표준편차) 

# 히스토그램 : 단위(밀도)
plt.hist(X, bins='auto', density=True) # 밀도단위 히스토그램
plt.plot(line, dline, color='red') # 확률밀도분포 곡선
# 선분이 밀도분포 곡선으로 계산됨
plt.show()

# 4) 정규성 검정 
# 귀무가설(H0) : 정규분포와 차이가 없다.
print(stats.shapiro(X)) # 정규성 검정
# ShapiroResult(statistic=0.9978905320167542, pvalue=0.23978953063488007)
# statistic: 검정통계량, pvalue: 유의확률
# p-value > 0.05일 수록 정규분포를 띰 -> 1에 가까울 수록 정규분포 지지
statistic, pvalue = stats.shapiro(X)
print('검정통계량 = ', statistic)
print('유의확률 =',pvalue)
'''
검정통계량 =  0.9978905320167542
유의확률 = 0.23978953063488007 -> 가설 지지 확률
'''
# 유의수준 알파
alpha=0.05 # 유의수준 = 1-신뢰수준
# 만일 95% 신뢰수준이면, 유의수준은 0.05
if pvalue>=alpha:
    print('정규분포와 차이가 없다.') # 채택
else:
    print('정규분포와 차이가 있다.')
# 정규분포와 차이가 없다.

# 2. 이항분포 검정 : 이항분포를 이용한 가설검정 
# - 이항분포 : 2가지 범주(성공 or 실패)를 갖는 이산확률분포
# - 이항분포 : 베르누이분포(독립시행 1번), 이항분포(독립시행 여러번) -> 비슷함
'''
베르누이분포 vs 이항분포
- 공통점: 이항분포
- 차이점
  - 베르누이분포: B(N=1,P) -> 독립시행 1번
  - 이항분포: B(N=n,P) -> 독립시행 2번 이상 n번
'''
# 1) 표본 추출(random sampling)

# (1) 동전 확률실험 : 베르누이분포(n=1, p=0.5) 모집단에서 표본 추출 
# 독립시행 1번  
bernoulli_obj = stats.bernoulli(p=0.5)  # p: 성공 확률
sample1 = bernoulli_obj.rvs(size=10) # N번 시뮬레이션: 표본 추출
print('sample1 =', sample1) 
# sample1 = [0 0 0 0 0 1 1 0 0 0]
# 1: 성공, 2: 실패

# (2) 동전 확률실험 : 이항분포(n=5, p=0.5) 모집단에서 표본 추출  
# 독립시행 여러번(n번)
binom_obj = stats.binom(n=5, p=0.5) 
sample2 = binom_obj.rvs(size=10) # N번 시뮬레이션: 표본 추출
print('sample2 =', sample2) 
# sample2 = [3 4 4 3 2 3 1 0 2 2]

# 한 줄 표현: object + rvs(표본)
sample3 = stats.binom.rvs(n=5, p=0.5,size=10) # n번 독립시행
print('sample3 =',sample3)
# sample3 = [2 1 1 3 1 2 2 2 5 3]

sample4 = stats.bernoulli.rvs(p=0.5,size=10) # 1번 독립시행
print('sample4 =',sample4)
# sample4 = [0 0 0 0 0 0 0 0 1 1]

# [문제] 주사위 확률실험: 베르누이 독립시행 10회와 성공확률 p=1/6을 갖는 50개 표본 추출하기
dice=stats.binom.rvs(n=10,p=1/6,size=50)
'''
array([1, 2, 1, 2, 0, 0, 2, 1, 4, 0, 3, 1, 2, 0, 2, 2, 1, 1, 1, 0, 4, 1,
       4, 0, 3, 3, 4, 2, 2, 2, 3, 1, 1, 2, 4, 0, 2, 2, 1, 1, 1, 1, 2, 1,
       4, 0, 2, 3, 4, 3])
'''

# 2) 이항검정(binom test) : 이항분포에 대한 가설검정 
'''
# 연구환경 : 게임에 이길 확률(p)이 40%이고, 게임의 시행회수가 50 일 때 95% 신뢰수준에서 검정 
# 귀무가설 : 게임에 이길 확률(p)는 40%와 차이가 없다.
# 대립가설 : 게임에 이길 확률(p)는 40%와 차이가 있다.
'''
# seed값 활용
import numpy as np
np.random.seed(123) # 항상 동일한 값 난수 생성 (저장)

# (1) 베르누이분포 : B(1, p)에서 표본추출(100개) 
n = 1 # 시행회수 
p = 0.4 # 모수(p)

# 베르누이분포 표본 추출 
X_binom = stats.binom.rvs(n=n, p=p, size=50) # B(1,0.4,50)
# X_binom = stats.bernoulli.rvs(p=p, size=50) # B(1,0.4,50)
X_binom

# (2) 성공 회수 반환 : zero 제외  
print('binom 성공회수 =', np.count_nonzero(X_binom)) 
# binom 성공회수 = 18

# (3) 이항검정 
x = np.count_nonzero(X_binom) # 성공횟수

## 유의확률 구하기 
# 이항검정 수행
pvalue = stats.binom_test(x=x, n=50, p=0.4, alternative='two-sided') 
# alternative='two-sided' 양측검정
print('x = %d, pvalue= %.5f'%(x, pvalue)) # x = 18, pvalue= 0.66547
'''
x : 성공횟수
n : 표본수(시행횟수)
p : 성공확률
alternative : 단/양측검정
'''
# 따라서, 귀무가설 채택

# (4) 가설검정 : 유의확률와 유의수준 비교  
alpha = 0.05 # 95%신뢰수준 : alpha = 1-신뢰수준 

if pvalue>=alpha:
    print('게임에 이길 확률(p)는 40%와 차이가 없다.')  # 채택
else:
    print('게임에 이길 확률(p)는 40%와 차이가 있다.') 
# 게임에 이길 확률(p)는 40%와 차이가 없다.

######################### 
# 이항검정 example  
#########################
'''
1. 연구환경 
  150명의 합격자 중에서 남자 합격자가 62명일 때 99% 신뢰수준에서 
  남여 합격률에 차이가 있다고 할수 있는가?

2. 귀무가설 : 남여 합격률에 차이가 없다.(P=0.5)
'''
x=62 # 성공횟수
n=150 # 표본수
p=0.5
pvalue2=stats.binom_test(x=62, n=150, p=0.5, alternative='two-sided') 
pvalue2 # 0.040868493866493945

alpha=0.01 # 99% 신뢰수준: alpha=1-0.99
if pvalue>=0.01:
    print('남여 합격률 차이가 없다.') # 채택
else:
    print('남여 합격률 차이가 있다.')

# 만일, alpha=0.05인 95% 신뢰수준 기각
# alpha=0.01인 99% 신뢰수준 채택