'''
문제4) 서울 지역을 대상으로 '동' 이름만 추출하여 다음과 같이 출력하시오.
  단계1 : 'ooo동' 문자열 추출 : 예) '개포1동 경남아파트' -> '개포1동'
  단계2 : 중복되지 않은 전체 '동' 개수 출력 : 힌트) 중복 제거 set 이용
  단계3 : 번호와 동이름으로 데이터프레임을 만들고 data 폴더에 csv file 저장하기 
  
  <출력 예시>  
중복 포함 전체 동 개수 : 8080
서울시 전체 동 개수 = 797

데이터프레임 & csv file 저장 
      no        dong
0      1         대치동
1      2        신길1동
2      3      영등포동2가
3      4        남가좌동
4      5        신월4동
..   ...         ...
792  793         장안동
793  794   영등포우체국사서함
794  795       양평동6가
795  796  서울동작우체국사서함
796  797        암사3동

[797 rows x 2 columns]
'''

import pandas as pd
path = 'C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap08_FileIO\\data'
import re  

try :
    file = open(path + "/zipcode.txt", mode='r', encoding='utf-8')
    lines7 = file.readline() # 첫줄 읽기 
    dong = [] # 서울시 동 저장 list
    while lines7 != '':
        line=lines7.split('\t')
        if line[1]=='서울':
            line_d=line[3].split()
            dong.append(line_d[0])
        lines7 = file.readline()
    newdong=list(set(dong))
    file.close()
    # DataFrame 생성
    no=list(range(1,len(newdong)+1))
    df=pd.DataFrame({'no':no,'dong':newdong})
    # save cav file
    df.to_csv(path+'SeoulDong.csv',header=True,encoding='utf-8')    
       
except Exception as e :
    print('예외발생 :', e)
    
    
print('중복 포함 전체 동 개수 :',len(dong))
print('서울시 전체 동 개수 =',len(newdong))
print(df)
    