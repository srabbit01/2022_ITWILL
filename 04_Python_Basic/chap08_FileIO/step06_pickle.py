'''
pickle 파일 
 - 파이썬 객체(list, dict)를 이진파일(binary)로 저장
 - 객체 입출력
'''

# 1. file read 
path = 'C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap08_FileIO\\data'
rfile = open(path + '/clean_texts.txt', mode = 'r', encoding='utf-8') # 전처리 후 파일
texts = rfile.readlines() # 줄 단위 list 형태로 반환
print(texts)

# 2. word count 
words = []
wc = {}

# word 추출 & word count 
for line in texts : # list
    for word in line.split() : # str
        words.append(word)
        wc[word] = wc.get(word, 0) + 1
    
print(wc) 
print(type(wc)) # <class 'dict'> - 객체 출처 
    

# 3. pickle: object(list, dict) <-> binary file
import pickle 
'''
- .dump(): 저장하기(save) = object(list, dict) -> binary file
- .load(): 읽어오기 = binary file -> object(list, dict) 
'''
# binary file save
file = open(path+'/wc_data.pickle', mode='wb') # write binary
# .pickle: 바이너리 형식으로 저장된 파일 형식
# pickle.dump(대상,파일)
pickle.dump(wc, file) # list object
file.close()

# binary file load
file = open(path+'/wc_data.pickle', mode='rb') # read binary
wc_data_new=pickle.load(file)
type(wc_data_new) # dict: 저장하기 전 객체 그대로 저장
print(wc_data_new)
'''
저장 전 그대로 출력
{'우리나라': 2, '대한민국': 2, '만세': 1, '비아그라': 1, 'gram': 1, '정력': 1, '최고': 1, '나는': 2, '사람': 1, '보험료': 1, '원에': 1, '평생': 1, '보장': 1, '마감': 1, '임박': 1, '홍길동': 1}
'''
file.close()

print(words)
words[0]
'''
['우리나라', '대한민국', '우리나라', '만세', '비아그라', 'gram', '정력', '최고', '나는', '대한민국', '사람', '보험료', '원에', '평생', '보장', '마감', '임박', '나는', '홍길동']
'''
# 만일 텍스트로 저장하면? 왜 텍스트로 저장하지 않음? -> 리스트 그대로 활용하기 위해
file = open(path+'/word.txt', mode='w')
file.write(str(words)) # list -> string으로 형변환 하여 저장
file.close()
file = open(path+'/word.txt', mode='r')
words_txt=file.read()
file.close()
words_txt[0] # '[' list가 아닌 문자형(string)으로 인식
print(words_txt)
print(type(words_txt)) # <class 'str'>
