# -*- coding: utf-8 -*-
"""
step02_module_func.py

모듈(module)
- 파이썬에서 제고하는 파일 (*.py)
- 경로: ~\anaconda3\Lib
- 파일 내부: 함수 및 클래스 제공

모듈 함수
- 모듈에서 제공하는 함수
- 유형
  1) built-in 모듈: 내장함수 (import 필요 없음)
  2) import 모듈: 메모리상 로딩 필요
"""

# 1. built-in 모듈
dataset=list(range(1,6))
print(dataset) # [1,2,3,4,5]

'''
built-in 모듈 제공 함수
'''
sum(dataset) # 합계
max(dataset) # 최댓값
min(dataset) # 최솟값
len(dataset) # 길이

help(len)
# Help on built-in function len in module builtins:

dir(statistics) # 함수 혹은 클래스 확인
    
# 2. import 모듈
# 방법 1
import statistics as stat # 수학/통계 함수 제공
# 방법2
from statistics import mean, median, stdev
'''
open source 확인: ctrl + 클릭
'''

# for 패키지.모듈 import 함수1, 함수2, ...
from statistics import mean, median, stdev # 방법2

print('평균 =',stat.mean(dataset)) # 평균 = 3
print('평균 =',mean(dataset)) # 평균 = 3

median(dataset) # 중앙값
stdev(dataset) # 표준편차