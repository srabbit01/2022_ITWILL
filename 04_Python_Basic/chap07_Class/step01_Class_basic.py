'''
클래스(class)?
 - 여러 개의 함수와 자료를 묶어서 객체(object) 생성 역할
 - 구성 : 멤버변수 + 메서드 + 생성자
 - 멤버: 멤버변수 + 메서드
 - class 자체에는 return 없음
 
 형식)
 class 클래스 :
     멤버변수
     def 메서드(self) :
         자료 처리 
     def 생성자(self) :
          멤버변수 초기화   
'''

# 1. 중첩 함수
def calc_func(a, b): # outer 함수: 자료 생성
    # (a,b) -> 생성자
    # class의 멤버변수    
    x = a # 10
    y = b # 20
    
    # inner 함수: 자료 처리 -> class의 매소드
    def plus():
        p = x + y
        return p
    
    def minus():
        m = x - y
        return m
    return plus, minus

# outer 함수 실행
p, m = calc_func(10, 20) # 자료 생성
# inner 함수 반환
# plus 내부 함수
p() # 30
# minus 내부 함수
m() # -10

# 2. 클래스 : 중첩 함수 -> 클래스 변환 

class calc_class: # outer 함수 -> 클래스 대체
    # 멤버 변수 정의: outer 함수 변수 -> 멤버변수 대체
    # 클래스 선언부에 선언
    x = y = 0 # 자료 저장
    # 클래스 생성 시, 정의만 됨
    # 객체가 만들어져야 할당
    
    # 생성자: 객체 생성 [+ 멤버 번수 초기화(선택사항)]
    def __init__(self,a,b): # 필요 시, 외부에서 넘겨 받음
        self.x=a # plus = 30
        self.y=b # y = 20
    # 사용자가 생성자를 만들지 않을 경우
    '''
    # 생략 가능
    def __init__(self):
        pass
    '''
    
    # 메서드 정의: inner 함수 -> 매서드 대체
    def plus(self): # self: 멤버(멤버변수+매서드) 참조 객체
        p = self.x + self.y # self: 멤버변수에 접근하기 위한 매개체
        return p
    
    def minus(self): # 반드시 self 넣어야 함
        m = self.x - self.y
        return m
    
    # object 출력 내용 정의하는 특수 매서드
    def __str__(self):
        string='%d + %d = %d'%(self.x,self.y,self.plus())
        return string
      
# 1) 객체 생성: 함수 호출 대체
obj=calc_class(10,20) # 생성자 -> 객체(맴버변수+매서드) 생성
# 객체.멤버(멤버변수+매소드)
print(obj) # <__main__.calc_class object at 0x000002209A55EB20>
# 객체 정보 문자열: <__main__클래스명 object at 주소>
# 기본 정보도 나타남


a = [1,2,3]
b = [2,3,4]

c = zip(a, b)
print(c)

# 메서드 호출: object.method()
print('plus =',obj.plus()) # plus = 30
print('minus =',obj.minus()) # minus = -10

# 멤버 변수 호출: object.멤버변수
print('x =', obj.x) # x = 10
print('y =',obj.y) # y = 20

# 2) 객체2 생성: 객체의 주소가 위 객체와 다름
obj2=calc_class(100,200) # 출처(클래스)는 같으나, 객체는 다름
print('plus =',obj2.plus()) # plus = 300
print('minus =',obj2.minus()) # minus = -100
print('x =', obj2.x) # x = 100
print('y =',obj2.y) # y = 200

# 같은 클래스를 가져도 각 객체는 주소 다름
id(obj) # 1679471948704
id(obj2) # 1679471860944

'''
중첩함수 vs 클래스
- 공통점: 자료 + 다수의 함수(inner OR method) 하나로 묶을 수 있음
- 중첩함수: 함수만 반환 -> 자료는 함수 호출 이후 메모리에서 소멸 (자료 참조 불가능)
 -> 함수 종료 시 소멸
- 클래스: 자료+함수 반환 -> 자료 메모리 상주(참조 가능)
 -> 메모리에 계속 남음
'''

##
# 생성자 없이 클래스 생성: 인수 기입 불가능
class calc_class: # outer 함수 -> 클래스 대체
    # 멤버 변수 정의: outer 함수 변수 -> 멤버변수 대체
    x=20
    y=10 # 자료 저장
    
    # 메서드 정의: inner 함수 -> 매서드 대체
    def plus(self): # self: 멤버(멤버변수+매서드) 참조 객체
        p = self.x + self.y
        return p
    
    def minus(self):
        m = self.x - self.y
        return m
obj2=calc_class()
obj2.plus() # 30
obj2.minus() # 10
obj2.x
