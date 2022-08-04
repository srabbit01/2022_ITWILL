'''
모듈 클래스: 이미 만들어진 클래스
 - 파이썬에서 제공하는 클래스
 - 유형
   1) builtins 모듈 클래스 : 내장 클래스 
   2) import 모듈 클래스 : 가져오기 클래스 
- 모듈: 이미 만들어진
'''

# 1. builtins 모듈 클래스
import builtins
dir(builtins) # 함수 + 클래스
'''
1) 에러 종류
 'ValueError',
 'Warning',
 'WindowsError',
 'ZeroDivisionError',
2) 특수 메소드: __init__ 등과 같음
 '__IPYTHON__',
 '__build_class__',
 '__debug__',
 '__doc__',
3) 함수 혹은 클래스: 구분은 도움말 이용
 'abs',
 'all',
 'any',
 'ascii',
 'bin',
 'bool',
'''
# 모듈 함수
a=abs(-10) # 10

# 모듈 클래스 (내장): 자료구조 혹은 형변환 클래스
# 형변환: int(), float(), str(), bool()
i=int(10.5) # 정수 변환 클래스
# int() # 생성자 의미 -> 클래스 뒤에 괄호 있으면 생성자 의미 -> 객체 반환

# 자료구조: list(), tuple(), set(), dict() 생성 -> 객체 변환
l=list((1,2,3,4,5,6))
# list(): 객체를 생성하는 클래스


# 2. import 모듈 클래스: 내장 클래스
from statistics import mean # 모듈 함수
mean([10,20,30]) # 20 -> 값만 반환
import datetime
from datetime import date # 날짜 객체 생성 모듈 클래스 
'''
class date:
    """Concrete date type. # 생성자 의미

    Constructors:

    __new__()
    fromtimestamp()
    today()
    fromordinal()

    Operators:

    __repr__, __str__
    __eq__, __le__, __lt__, __ge__, __gt__, __hash__
    __add__, __radd__, __sub__ (add/radd only with timedelta arg)

    Methods: # 함수(메소드)

    timetuple()
    toordinal()
    weekday()
    isoweekday(), isocalendar(), isoformat()
    ctime()
    strftime()

    Properties (readonly):
    year, month, day
    """
    
    # 생성자: 특수 메소드 사용 -> 객체 생성 (cls -> self 대신)
    def __new__(cls, year, month=None, day=None):
    
    # 메소드
    def fromordinal(cls, n):
'''
# object 생성
today=date.today() # 오늘 날짜 확인: datetime.date(2022, 4, 14)
# 인수 넣기 + 객체 생성하여 변수에 입력
tomarr=date(2022,4,15) #날짜 객체 생성
print(tomarr)

# 객체 = 생성자
type(tomarr) # 출처 확인 -> datetime.date이란 모듈.클래스에 의해 만들어짐을 의미
# 04는 인식 X 순수 4만 넣기
print(type(tomarr)) # <class 'datetime.date'> 클래스 객체가 무엇인지 표기
# 객체의 클래스 표기

# object.member(값을 저장하는 멤버변수 or 메소드)
dir(today) # 해당 객체의 멤버 확인
'''
['__add__',
 '__class__',
 '__delattr__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__ne__',
 '__new__',
 '__radd__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rsub__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__sub__',
 '__subclasshook__',
 'ctime',
 'day',
 'fromisocalendar',
 'fromisoformat',
 'fromordinal',
 'fromtimestamp',
 'isocalendar',
 'isoformat',
 'isoweekday',
 'max',
 'min',
 'month', # 월
 'replace',
 'resolution',
 'strftime',
 'timetuple',
 'today', # 오늘
 'toordinal',
 'weekday', # 요일
 'year'] # 년도
'''
# 멤버변수 호출(실제 데이터 자료): object.멤버변수
today.year # 2022: 년도 정보 확인
today.month # 4: 월 정보 확인
today.day # 14: 일 정보 확인
# 메서드 호출(동작): object.메서드()
today.weekday() # 3: 요일 계산 행위 (0: 월요일 ~ 6: 일요일)



import importlib
importlib.reload(date)

