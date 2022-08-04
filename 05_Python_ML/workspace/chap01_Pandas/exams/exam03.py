'''
step02 관련문제
문3) wdbc_data.csv 파일을 읽어와서 단계별로 x, y 변수를 생성하시오.
     <단계1> : 파일 가져오기, 정보 확인 
     <단계2> : y변수 : diagnosis 
              x변수 : id 칼럼 제외  나머지 30개 칼럼
'''
import pandas as pd

# file 경로 변경 
path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data' # 경로 지정

# <단계1> : 파일 가져오기, 정보 확인 
wdbc=pd.read_csv(path+'/wdbc_data.csv')
wdbc.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 569 entries, 0 to 568
Data columns (total 32 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   id                 569 non-null    int64  
 1   diagnosis          569 non-null    object 
 2   radius_mean        569 non-null    float64
 3   texture_mean       569 non-null    float64
 4   perimeter_mean     569 non-null    float64
 5   area_mean          569 non-null    float64
 6   smoothness_mean    569 non-null    float64
 7   compactness_mean   569 non-null    float64
 8   concavity_mean     569 non-null    float64
 9   points_mean        569 non-null    float64
 10  symmetry_mean      569 non-null    float64
 11  dimension_mean     569 non-null    float64
 12  radius_se          569 non-null    float64
 13  texture_se         569 non-null    float64
 14  perimeter_se       569 non-null    float64
 15  area_se            569 non-null    float64
 16  smoothness_se      569 non-null    float64
 17  compactness_se     569 non-null    float64
 18  concavity_se       569 non-null    float64
 19  points_se          569 non-null    float64
 20  symmetry_se        569 non-null    float64
 21  dimension_se       569 non-null    float64
 22  radius_worst       569 non-null    float64
 23  texture_worst      569 non-null    float64
 24  perimeter_worst    569 non-null    float64
 25  area_worst         569 non-null    float64
 26  smoothness_worst   569 non-null    float64
 27  compactness_worst  569 non-null    float64
 28  concavity_worst    569 non-null    float64
 29  points_worst       569 non-null    float64
 30  symmetry_worst     569 non-null    float64
 31  dimension_worst    569 non-null    float64
dtypes: float64(30), int64(1), object(1)
memory usage: 142.4+ KB
'''

# <단계2> : y변수, x변수 선택
# y변수 : diagnosis 
wdbc_x=wdbc.diagnosis
wdbc_x

# x변수 : id 칼럼 제외  나머지 30개 칼럼
wdbc_li=list(wdbc.columns)
wdbc_y=wdbc[wdbc_li[2:]]
wdbc_y.info()
