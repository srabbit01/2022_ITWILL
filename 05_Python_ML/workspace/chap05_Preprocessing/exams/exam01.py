# 문1) dataset 자료를 이용하여 다음과 같은 단계로 결측치를 처리하시오.

import pandas as pd 
pd.set_option('display.max_columns', 50) # 최대 50 칼럼수 지정

# 데이터셋 로드 
path=r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML'
dataset = pd.read_csv(path+'/data/dataset.csv')
dataset.info()
dataset

# 단계1 : 전체 칼럼 중에서 가장 많은 결측치를 갖는 칼럼 찾기 
result=dataset.isnull().sum()
'''
resident     0
gender       0
job         12
age          0
position     9
price        0
survey       0
dtype: int64
'''
# job와 position 칼럼의 결측치 처리
type(result)
result.values # array([ 0,  0, 12,  0,  9,  0,  0], dtype=int64)
column=result.values.max() # 결측치가 제일 많은 칼럼 12개 존재
print(f'결측치가 가장 많은 칼럼: {column}')
# 결측치가 가장 많은 칼럼: 12
dataset.shape # (217,7)

# 단계2. position 칼럼 기준으로 결측치 제거하여 new_dataset 만들기
new_dataset=dataset.dropna(subset=['position'],axis=0) # 행축
new_dataset.shape # (208,7)
# 217 -> 208: 9개 제거

# 단계3. 전체 칼럼을 대상으로 결측치를 제거하여 new_dataset2 만들기
new_dataset2=dataset.dropna()
new_dataset2.shape # (198,7)
# 217 -> 198: 19개 제거

# 단계4. dataset의 job 칼럼의 결측치를 0으로 대체하여 dataset 객체 반영하기
dataset['job'].fillna(0,inplace=True)
dataset.shape # (217,7) -> 행의 수 줄어들지 않음
dataset['job'].value_counts()
'''
3.0    77
2.0    74
1.0    54
0.0    12
'''