'''
csv, excel file read
 - 칼럼 단위로 작성된 excel 파일 유형 읽기
'''

import pandas as pd # csv, excel file I/O

# 1. csv file
path = 'C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap08_FileIO\\data'

# R: read.csv()
bmi_data = pd.read_csv(path + '/bmi.csv', encoding='utf-8')
type(bmi_data) # pandas.core.frame.DataFrame
bmi_data.info() # R: str(data) -> 파일 정보 확인
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20000 entries, 0 to 19999 -> 행 개수
Data columns (total 3 columns): -> 열 개수
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   height  20000 non-null  int64 -> 정수형 
 1   weight  20000 non-null  int64 
 2   label   20000 non-null  object -> 문자형(char)
dtypes: int64(2), object(1)
memory usage: 468.9+ KB
'''
print(bmi_data.head()) # R: head(data) -> 앞 5개 데이터 확인
print(bmi_data.tail()) # R: tail(data)

# 변수 선택     
height = bmi_data.height # R: df$column = 변수$칼럼
weight = bmi_data.weight
label = bmi_data.label
type(height) # pandas.core.series.Series

# 평균 구하기
print('height mean :', sum(height)/len(height)) # height mean : 164.9379
print('weight mean :', sum(weight)/len(weight)) # weight mean : 62.40995

# 최대/최소 구하기
max(height) # 190
max(weight) # 85

# 메서드 호출
# 객체 내 자동 통계처리 가능
height.mean() # 평균 구하기 = 164.9379
weight.mean() # 62.40995
# 출현 빈도수 확인
label.value_counts() # R: table(label)
'''
normal    7677
fat       7425
thin      4898
Name: label, dtype: int64
'''

# 2. excel file 
'''
xlrd 패키지 설치 : pip install xlrd
'''
ex = pd.ExcelFile(path + '/sam_kospi.xlsx')
type(ex)
print(ex) # object info
# parse: 특정 워크시트 가져오기
kospi = ex.parse('sam_kospi') # 워크시트 지정
print(kospi)
'''
          Date     Open     High      Low    Close  Volume # 행
0   2015-10-30  1345000  1390000  1341000  1372000  498776 # head 5개
1   2015-10-29  1330000  1392000  1324000  1325000  622336
2   2015-10-28  1294000  1308000  1291000  1308000  257374
3   2015-10-27  1282000  1299000  1281000  1298000  131144
4   2015-10-26  1298000  1298000  1272000  1292000  151996
..         ...      ...      ...      ...      ...     ...
242 2014-11-07  1218000  1218000  1195000  1206000  107688 # tail 5개
243 2014-11-06  1198000  1210000  1193000  1204000  168497
244 2014-11-05  1215000  1225000  1194000  1202000  187182
245 2014-11-04  1219000  1242000  1205000  1217000  237045
246 2014-11-03  1250000  1252000  1216000  1235000  263940
행 번호
[247 rows x 6 columns]
'''
kospi.info()
'''
<class 'pandas.core.frame.DataFrame'> # pandas 데이터프레임 형식의 객체 (R과 비슷)
RangeIndex: 247 entries, 0 to 246
Data columns (total 6 columns):
 #   Column  Non-Null Count  Dtype  -> 칼럼명 행개수 Null/Non-Null 자료형       
---  ------  --------------  -----         
 0   Date    247 non-null    datetime64[ns]
 1   Open    247 non-null    int64         
 2   High    247 non-null    int64         
 3   Low     247 non-null    int64         
 4   Close   247 non-null    int64         
 5   Volume  247 non-null    int64         
dtypes: datetime64[ns](1), int64(5)
memory usage: 11.7 KB
'''
# 칼럼 추출
High = kospi.High # DF.column
Low = kospi['Low'] # DF['column']

# 파생변수
diff = High - Low # 새로운 파생변수 생성
# 행/열 개수가 같기 때문에 동일 행 내 가능 = pandas 1:1 연산 가능 (for문 필요 없음)
diff
# 파생변수 추가: 데이터프레임 칼럼 추가
kospi['Diff']=diff
# Data columns (total 7 columns):
    
kospi.head()
High.value_counts()

# 3. csv 파일 저장
type(kospi) # pandas.core.frame.DataFrame 객체 (행렬 구조)
# csv 파일로 변환 및 저장
kospi.to_csv(path+'/kospi.csv',index=False,encoding='utf-8') # csv 형식으로 변환: 콤마(,)로 나뉜 구조
# index(행번호) 저장 여부 = False(저장하지 않음=제외=None)/True(저장함)
# encoding='utf-8'

# csv 파일 읽기
kospi_new=pd.read_csv(path+'/kospi.csv',encoding='utf-8')
print(kospi_new.info())