'''
문제1) ftest.txt 파일을 읽어서 다음과 같이 줄 수와 단어를 카운트 하시오. 


문단 내용 
['programming is fun', 'very fun!', 'have a good time', 'mouse is input device', 'keyboard is input device', 'computer']
문장 수 :  6

단어 내용 
['programming', 'is', 'fun', 'very', 'fun!', 'have', 'a', 'good', 'time', 'mouse', 'is', 'input', 'device', 'keyboard', 'is', 'input', 'device', 'computer']
단어 수 :  22
'''

 
import os

# 파일 읽기 
os.getcwd()
os.chdir('C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap08_FileIO\\data')
file = open("ftest.txt", mode = 'r')
texts = file.readlines()
# print(texts)
'''
['programming is fun\n', 'very fun!\n', 'have a good time\n', 'mouse is input device\n', 'keyboard is input device\n', 'computer is input output system']
'''

# 문단 내용
line=[t.replace('\n','') for t in texts]

# 단어 내용
word=[]
for l in line:
    l=l.split()
    word.extend(l)

# 결과 출력
print(f'''
# 문단 내용 
{line}
문장 수 :  {len(line)}

# 단어 내용 
{word}
단어 수 :  {len(word)}''')
