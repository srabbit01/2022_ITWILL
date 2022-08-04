'''
1. 동적 멤버변수 생성
  - 생성자 또는 메서드에서 동적으로 멤버 변수 생성 
  - self: 인스턴스 = 클래스 내 멤버(멤버변수+메서드) 호출 객체 역할
'''

class Car :
    # 멤버변수 정의
    # 필요에 따라 멤버변수 만들 수 있음
    # 굳이 정의하지 않아도 동적멤버변수 생성 시 -> 멤버변수 정의됨
    '''
    # 정적 멤버변수: 클래스 선언부에 선언
    door = 0
    cc = 0
    name = None # NULL
    ''' # 없어도 됨
    
    # 생성자 
    def __init__(self, name, door, cc):
        # 생성자에 멤버변수 입력하는 순간 멤버변수 생성
        self.name = name # 동적멤버변수 = 지역변수
        self.door = door
        self.cc = cc
    
    # 메서드 정의: 자동차 정보 
    def info(self):
        # self.kind='' # 동적 멤버변수 생성 (생략 가능)
        # 멤버변수 사용 의미
        if self.cc >= 3000:
            self.kind='대형'
        else:
            self.kind='중소형' # return하지 않아도 자동 생성
    
    # 메서드 정의 : 자동차 정보 
    def display(self):         
        self.info() # 자동으로 info 함수 먼저 실행
        print("%s는 %d cc(%s)이고, 문짝은 %d개 이다."
              %(self.name, self.cc, self.kind, self.door))
    
# 객체1
car1 = Car('소나타',4,2000) # 생성자 -> 객체
car1.info() # 메서드 내부에서도 'self.멤버변수=값' 할당하면 새로운 멤버변수 생성 가능
car1.display() # 타 메서드에서 생성된 멤버변수 사용하기 위해 우선, info() 매서드 먼저 실행

# 객체2
car2 = Car('그랜저',4,3000)
car2.display()

'''
# 생성자 = 객체 생성 + [변수 초기화]

2. 기본 생성자(묵시적 생성자)
  - 생성자를 생략하면 기본 생성자가 만들어진다. 
'''

class default :     
    # 생성자 없음
    '''
    def __init__: # 객체만 생성하는 기본 생성자
        pass
    '''
    def data(self, x, y):
        self.x = x
        self.y = y
        
    def mul(self):
        return self.x * self.y
    
obj=default()
obj.data(10,20) # 자료 생성       
obj.mul()        
         


