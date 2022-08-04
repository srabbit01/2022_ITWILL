# -*- coding: utf-8 -*-
"""
data source : https://www.kaggle.com/uciml/student-alcohol-consumption

포루투갈의 2차교육과정에서 학생들의 음주에 영향을 미치는 요소는 무엇인가? 
영향을 미친다면 그 정도는 어떠한가?
What are the factors influencing drinking in Portuguese secondary education? 
If it does, what is its degree?
"""

import pandas as pd

## student-mat.csv : 카페에서 파일 다운로드 
path=r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML' 
student = pd.read_csv(path+r'\data\student-mat.csv')
student.info()

'''
학생들의 음주에 미치는 영향을 조사하기 위해 6가지의 변수 후보 선정
독립변수(X) : sex(성별), age(15~22), Pstatus(부모거주여부), failures(수업낙제횟수), famrel(가족관계), grade(G1+G2+G3 : 연간성적) 
          grade : 0~60(60점이 고득점), Alcohol : 0~500(100:매우낮음, 500:매우높음)으로 가공
종속변수(Y) : Alcohol = (Dalc+Walc)/2*100 : 1주간 알코올 섭취정도  
'''

# 1. subset 만들기 
df = student[['sex','age','Pstatus','failures','famrel','Dalc','Walc','G1','G2','G3']]
df.info()
'''
RangeIndex: 395 entries, 0 to 394
Data columns (total 10 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   sex       395 non-null    object : 성별(F, M) -> 범주형
 1   age       395 non-null    int64  : 나이(15 ~ 22) -> 정수형(연속형)
 2   Pstatus   395 non-null    object : 부모거주여부(T, A) -> 범주형
 3   failures  395 non-null    int64  : 수업낙제횟수(0,1,2,3) -> 낙제 최대 3회 (이산)
 4   famrel    395 non-null    int64  : 가족관계(1,2,3,4,5) -> 수량적 친밀도(이산)
 5   Dalc      395 non-null    int64  : 1일 알콜 소비량(1,2,3,4,5) -> 이산
 6   Walc      395 non-null    int64  : 1주일 알콜 소비량(1,2,3,4,5) -> 이산
 7   G1        395 non-null    int64  : 첫번째(1) 학년(0~20) -> 점수
 8   G2        395 non-null    int64  : 두번째(2) 학년(0~20) -> 점수
 9   G3        395 non-null    int64  : 마지막(3) 학년(0~20) -> 점수
'''

# 각 변수 통계량과 빈도수 확인 
df.describe() # 숫자형 변수 통계
# 문자형/논리형/범주형 등 제외하고 숫자형에 대한 통계량만 제시
'''
              age    failures      famrel  ...          G1          G2          G3
count  395.000000  395.000000  395.000000  ...  395.000000  395.000000  395.000000
mean    16.696203    0.334177    3.944304  ...   10.908861   10.713924   10.415190
std      1.276043    0.743651    0.896659  ...    3.319195    3.761505    4.581443
min     15.000000    0.000000    1.000000  ...    3.000000    0.000000    0.000000
25%     16.000000    0.000000    4.000000  ...    8.000000    9.000000    8.000000
50%     17.000000    0.000000    4.000000  ...   11.000000   11.000000   11.000000
75%     18.000000    0.000000    5.000000  ...   13.000000   13.000000   14.000000
max     22.000000    3.000000    5.000000  ...   19.000000   19.000000   20.000000
'''
df.sex.value_counts() # 문자형 변수 (범주형 빈도수)
'''
# 성별 확인 (F: 여자, M: 남자)
F    208
M    187
''' 
df.Pstatus.value_counts() # 문자형 변수 (범주형 빈도수)
'''
# 부모 거주 여부 확인 (T: 부모 O, A: 혼자)
T    354
A     41
'''
# 문자형 범주 변수는 반드시 인코딩 필요

# 2. 파생변수 만들기 
grade = df.G1 + df.G2 + df.G3 # 성적 
grade.describe() # 4 ~ 58 
# 평균: 32 -> 정규분포 형태를 띰
'''
count    395.000000
mean      32.037975
std       11.090357
min        4.000000
25%       25.000000
50%       32.000000
75%       40.000000
max       58.000000
'''

# 알콜 소비량 계산
Alcohol = (df.Dalc + df.Walc) / 2 * 100 # 알콜 소비량 
Alcohol.describe() # 100 ~ 500(100: 매우낮음, 500: 매우높음)
'''
count    395.000000
mean     188.607595
std       99.219469
min      100.000000
25%      100.000000
50%      150.000000
75%      250.000000
max      500.000000
'''

# 1) 파생변수 추가 
df['grade'] = grade 
df['Alcohol'] = Alcohol

# 2) 기존 변수 제거
new_df = df.drop(['Dalc','Walc','G1','G2','G3'], axis = 1) # 칼럼 기준 제거 
new_df.info()
'''
Data columns (total 7 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   sex       395 non-null    object - 범주형(문자형)
 1   age       395 non-null    int64  - 연속형
 2   Pstatus   395 non-null    object - 범주형(문자형)
 3   failures  395 non-null    int64  - 범주형(이산형)
 4   famrel    395 non-null    int64  - 범주형(이산형)
 5   grade     395 non-null    int64  - 연속형 
 6   Alcohol   395 non-null    float64- 연속형(y변수)  
''' 

import seaborn as sn
import matplotlib.pyplot as plt # data 시각화 

# 3. EDA : 종속변수(Alcohol) vs 독립변수 탐색 

### 1) 연속형 vs 범주형 : 빈도수와 막대차트 
# 범주형 이산변수: 막대/파이차트

# (1) Alcohol vs Sex
new_df.sex.value_counts() # 여성과 남성 출현 빈도수 확인
'''
F    208
M    187
'''
sn.countplot(x='sex',data=new_df) # 범주형 변수 출현 빈도수 시각화

# 연속형 변수 vs 범주형 변수
sn.barplot(x='sex',y='Alcohol',data=new_df)
# [해설] 남학생의 음주 소비량이 많다.

# (2) Alcohol vs Pstatus
sn.countplot(x='Pstatus',data=new_df)

# 연속형 변수 vs 범주형 변수
sn.barplot(x='Pstatus',y='Alcohol',data=new_df)
# [해설] 부모 거주 상태와 음수 소비량과 큰 차이가 없다.

# 그룹별 평균 통계량 시각화: barplot
group=new_df.groupby('Pstatus')
group.size()
group['Alcohol'].describe()
'''
         count        mean         std    min    25%    50%    75%    max
Pstatus                                                                  
A         41.0  191.463415  117.740413  100.0  100.0  150.0  250.0  500.0
T        354.0  188.276836   97.036088  100.0  100.0  150.0  250.0  500.0
'''
new_df.groupby('Pstatus')['Alcohol'].mean() # Pstatus 별 Alcohol 평균 시각화
'''
#
A    191.463415
T    188.276836
'''

# (3) Alcohol vs failures(0,1,2,3) = 낙제 횟수
sn.countplot(x='failures',data=new_df)

# 연속형 변수 vs 범주형 변수
sn.barplot(x='failures',y='Alcohol',data=new_df)
# [해설] 낙제 과목이 많을 수록 음주 소비량이 많다.

# (4) Alcohol vs famrel(1,2,3,4,5) = 가족 간 관계
sn.countplot(x='famrel',data=new_df)

# 연속형 변수 vs 범주형 변수
sn.barplot(x='famrel',y='Alcohol',data=new_df)
# [해설] 가족 친밀도가 낮을 수록 음주 소비량이 많다.

### 1) 연속형 vs 연속형 : 산점도 이용 
# 연속형 숫자변수: 산점도/히스토그램

# 1) Alcohol vs age (15~22)
sn.scatterplot(x='age',y='Alcohol',data=new_df)
# 20살 이상의 학생은 정상이 아닌 특이 경우로 분류 (연력대가 많음) -> 분포 희박
# y축으로 분산: 각 연령별 빈도수 많음
# -> 연령대 별로 그룹을 형성하여 평균을 내는 것이 더 좋음
new_df.age.value_counts()
# 동일 연령 별 그룹화 -> 평균 구하기
group=new_df.groupby('age')
group.size() # value counts와 결과 동일
group_alcohol=group.Alcohol.mean() # 각 연령 별 평균 구하기
'''
age
15    162.804878
16    185.576923
17    204.591837
18    198.170732
19    170.833333
20    216.666667
21    300.000000
22    500.000000
'''
# 연령별 평균 시각화
plt.plot(group_alcohol,'ro')
plt.show()
# [해설] 전반적으로 연령이 증가할 수록 음주 소비량이 많다.

# 2) Alcohol vs grade (4~58)
sn.scatterplot(x='grade',y='Alcohol',data=new_df)
# x축으로 분산: 각 점수별 빈도수 적음
# -> 점수 별 그룹을 형성하여 평균을 내는 것이 더 좋음
# 동일 grade 별 그룹화 -> 평균 구하기
group2=new_df.groupby('grade')
# 점수별 음주량 평균
group2_alcohol=group2['Alcohol'].mean()
# 점수별 평균 시각화
plt.plot(group2_alcohol,'ro')
plt.show()
'''
[해설]
0 ~ 20점대: 점수 증가에 따른 음주량 증가
20 ~ 40점대: 점수 증가에 따른 음주량 변화 없음
40 ~ 60점대: 점수 증가에 따른 음주향 감소
'''

# 4. EDA 분석 결과
'''
포루투갈 학생들의 음주는 나이의 증가와 강한 연관성을 가지고 있으며,
성별이 남자이고, 낙제 과목이 많아질 수록, 가족 간 관계가 안 좋을수록
음주량이 증가한다. 부모의 거주 상태는 큰 영향이 없으며, 40점 이상의 연간 성적의 
범주에서는 성적과 음주량이 반비례, 30점 이하에서는 성적과 음주량이 비례하는
것으로 나타난다.
'''