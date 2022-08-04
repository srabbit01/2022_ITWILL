# -*- coding: utf-8 -*-
"""
문제2) 웹문서 파일(test.htm)를 대상으로 <li> 내용 </li> 형식을 갖는 태그만
      추출하여 다음과 같이 출력하시오.
  
  <출력 예시>  
정상 태그 : ['<li> header : 문서의 머리말(사이트 소개, 제목, 로그 )</li>', '<li> nav : 네이게이션(메뉴) </li>', '<li> section : 웹 문서를 장(chapter)으로 볼 때 절을 구분하는 태그</li>', '<li> aside : 문서의 보조 내용(광고, 즐겨찾기, 링크) </li>', '<li> footer : 문서의 꼬리말(작성자, 저작권, 개인정보보호) </li>']
예외 태그 : ['<!DOCTYPE html>', '<html>', '<head>', '<meta charset="UTF-8">', '<title> html5 - 시멘틱 태그 </title>', '</head>', '<body>', '<h1> 시멘틱 태그 ?</h1>', '<p> html5에서 웹문서에 의미를 부여하는 태그를 의미 </p>', '<h2> 주요 시멘틱 태그 </h2>', '<ul>', '</ul>', '</body>', '</html>', '', '']
"""

from re import search
import os
os.chdir('C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap08_FileIO\\data')

Ori_tag=[]
Err_tag=[]

try :
    # file 읽기 
    file = open("test.html", mode = 'r', encoding='utf-8')
    lines = file.readlines() #  줄 단위 전체 읽기 - list 반환    
    for l in lines:
        try:
            re.search('<li>.+</li>',l).group()
            Ori_tag.append(l)
        except:
            Err_tag.append(l)
    
except Exception as e:
    print('Error 발생 : ', e)
finally:
    file.close()
    
print(f'''
1) 정상 태그 : {Ori_tag}

2) 예외 태그 : {Err_tag}
    ''')








