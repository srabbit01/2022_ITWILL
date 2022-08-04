'''
 문3) login.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오.
    조건1> id="login_wrap" 선택자의  하위 태그  전체 출력 
    조건2> id="login_wrap" 선택자  > form > table 태그 내용 출력
    조건3> find_all('tr') 함수 이용  th 태그 내용 출력  
'''

from bs4 import BeautifulSoup 

path = 'C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap10_Crawling\\data'

# 1. html source 가져오기 
file = open(path + "/login.html", mode='r', encoding='utf-8')
source = file.read()

# 2. html 파싱
soup=BeautifulSoup(source,'html.parser')

# 3. 선택자 이용 태그 내용 가져오기 
logId=soup.select_one('#login_wrap') # <div id="login_wrap">
# soup.select_one('div[id="login_wrap"]')
logId2=logId.select_one('form>table')
tr=logId2.find_all('tr')
for t in tr:
    th=t.find_all('th')
    for t2 in th:
        print(t2.string)

'''
 아이디 
 비밀번호 
 '''
