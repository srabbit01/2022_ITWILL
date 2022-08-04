# -*- coding: utf-8 -*-
"""
step02_text_preprocessing.py

텍스트 전처리 : 특수문자, 불용어 처리 
"""
import re # re 모듈 가져오기 

# 전처리 텍스트  
texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,  A124&***$?']
type(text) # list
type(text[-1]) # str

# 단계1 : 소문자 변경 

# list 내포 : 변수 = [실행문 for]
texts_re = [ st.lower() for st in texts] # 변수.lower(): 모든 영문자의 대문자 -> 소문자로 변환
'''
# list + for
texts_re=[]
for st in texts:
    texts_re.append(st.lower)
'''
print(texts_re)
# ['afab54747,asabag?', 'abtta $$;a12:2424.', 'uysfsfa,  a124&***$?']

# 단계2 : 숫자 제거 : sub('pattern', rep, string)
texts_re2 = [re.sub('[0-9]', '', st) for st in texts_re]
print(texts_re2)
# ['afab,asabag?', 'abtta $$;a:.', 'uysfsfa,  a&***$?']

# 단계3 : 문장부호 제거 
punc_str = '[,.?!:;]'
texts_re3 = [re.sub(punc_str, '', st) for st in texts_re2]
print(texts_re3)
# ['afabasabag', 'abtta $$a', 'uysfsfa  a&***$']

# 단계4 : 특수문자 제거 
spec_str = '[@#$%^&*()]'
texts_re4 = [re.sub(spec_str, '', st) for st in texts_re3]
print(texts_re4)
# ['afabasabag', 'abtta a', 'uysfsfa  a']

# 단계5: 공백 한칸으로 만들기 -> 공백(white space) 제거
texts_re5=[re.sub('[\s]+',' ',st) for st in texts_re4] # 'uysfsfa  a' -> 'uysfsfa a'
texts_re5=[' '.join(st.split()) for st in texts_re4]
print(texts_re5)
# ['afabasabag', 'abtta a', 'uysfsfa a']