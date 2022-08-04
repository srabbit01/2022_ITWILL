"""
step04_selector.py

선택자(selector) 이용 자료 수집 
 - 웹문서 디자인용으로 사용   
 - 유형: tag, id, class
     id : 중복 불가 (#id이름)
     class: 중복 허용 (.class이름)
 - 형식
     html.select_one('선택자') 
     html.select('선택자')
"""

from bs4 import BeautifulSoup # html 파싱 

path = 'C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap10_Crawling\\data'

# 1. html source 가져오기 
file = open(path + '/html03.html', mode='r', encoding='utf-8')
src = file.read()
print(src)

# 2. html 파싱
html = BeautifulSoup(src, 'html.parser')
print(html)


# 3. 선택자 이용 태그 내용 가져오기 
print('>> table 선택자 <<')

# 1) id 선택자: 1개 element 수정 
table = html.select_one('#tab') # <table id='tab'> </table>
print(table) # 1개 element

# 2) class 선택자: 2개 이상 element 수집
table2=html.select("table > .odd")
type(table2)
print(table2)
len(table2) # 2

new_table2=[tab.find_all('td') for tab in table2]
for tab in table2:
    tds=tab.find_all('td') # bs4.element.ResultSet
    for td in tds:
        print(td)
        
# 3) select("태그[속성='값']")
html.select("tr[class='odd']")
