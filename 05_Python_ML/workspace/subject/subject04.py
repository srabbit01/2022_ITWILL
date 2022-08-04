'''
과제4) DataFrame 문법을 적용한 2012년 미국 대선 후보자의 후원금 현황 자료 처리하기  
'''

import pandas as pd
path=r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML'
election = pd.read_csv(path+"/data/election_2012.csv", encoding='ms949')
print(election.info())
'''
RangeIndex: 1001731 entries, 0 to 1001730
Data columns (total 16 columns):

주요 변수 설명 
2. cand_id : 대선 후보자 id 
3. cand_nm : 대선 후보자 name
4. contbr_nm : 후원자 name
9. contbr_occupation : 후원자 직업 
10. contb_receipt_amt : 후원금액
'''

# [문제1] 위 5개 칼럼만을 대상으로 election_df 이름으로 subset 생성(iloc 또는 loc 속성 이용)
election_df=election.iloc[:,[1,2,3,8,9]]
election_df.info()

# [문제2] 결측치을 확인한 후 결측치의 행 모두 제거하기   
election_df.isnull().any()
# contbr_occupation 결측치 존재
election_df=election_df.dropna(subset=['contbr_occupation'])

# [문제3] 대선후보자 13명 이름 확인 : 출력 예시 참고 
'''
대선후보자 명단 : ['Bachmann, Michelle' 'Romney, Mitt' 'Obama, Barack'
 "Roemer, Charles E. 'Buddy' III" 'Pawlenty, Timothy' 'Johnson, Gary Earl'
 'Paul, Ron' 'Santorum, Rick' 'Cain, Herman' 'Gingrich, Newt'
 'McCotter, Thaddeus G' 'Huntsman, Jon' 'Perry, Rick']

대선후보자 : 13명 
''' 
election_df['cand_nm'].unique()

# [문제4] 'Romney, Mitt'와 'Obama, Barack' 대통령 후보자 별로 subset 생성
'''
   <조건1> 'Romney, Mitt' 후보자의 subset 저장 : romney
   <조건2> 'Obama, Barack' 후보자의 subset 저장 : obama  
   <조건3> 앞부분/뒷부분 5줄 관측치 출력 : 힌트) head()/tail()
'''
romney=election_df[election_df['cand_nm']=='Romney, Mitt']
romney.head()
obama=election_df[election_df['cand_nm']=='Obama, Barack']
obama.tail()

# [문제5] 각 후보자(romney, obama)별로 후원금액이 5000달러 이상인 후원자를 대상으로 subset 생성
'''
  <조건1> 결과 저장 : romney_5000over, obama_5000over
  <조건2> 각 후보자별로 후원자 수 출력 : 힌트) len()
          romney 후원자 수 = xxx
          obama 후원자 수 = xxx
'''
romney_5000over=romney[romney.contb_receipt_amt>=5000]
len(romney_5000over) # 613
obama_5000over=obama[obama.contb_receipt_amt>=5000]
len(obama_5000over) # 103

# [문제6] 각 후보자 별 서브셋(romney_sort, obama_sort)으로 후원자 직업군의
#           출현빈도수가 상위 5위에 해당하는 직업군 출력하기
import pandas as pd
romney_5000over['contbr_occupation'].value_counts()[:5]
'''
INFORMATION REQUESTED PER BEST EFFORTS    121
RETIRED                                    55
C.E.O.                                     32
PRESIDENT                                  32
ATTORNEY                                   24
'''
obama_5000over['contbr_occupation'].value_counts()[:5]
'''
RETIRED       28
OWNER          4
TEACHER        4
ATTORNEY       4
CONSULTANT     3
'''

# [문제7] 각 후보자 별 서브셋(romney_5000over, obama_5000over)별로 후원금 칼럼으로 내림차순 정렬하고 csv file 저장
'''
  <조건1> 각 후보자별로 후원금 칼럼으로 내림차순 정렬 : 힌트) sort_values('칼럼', ascending=False)
  <조건2> 내림차순 정렬한 결과를 다음과 같은 내용으로 csv 파일 저장
          저장 위치 : 현재 작업 위치
          파일명 : romney_5000over.csv, obama_5000over.csv
          행 번호 제외 
'''
path=r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/05. Python ML/workspace/subject'
# romney
romney_5000over_sort=romney_5000over.sort_values(by='contb_receipt_amt',ascending=False)
romney_5000over_sort.to_csv(path+'/romney_5000over.csv')

# obama
obama_5000over_sort=obama_5000over.sort_values(by='contb_receipt_amt',ascending=False)
obama_5000over_sort.to_csv(path+'/obama_5000over.csv')
