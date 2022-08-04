
# class 정의
class TV :
    
    # 생성자 
    def __init__(self):
        # 동적 멤버변수(상태) 초기화 
        self.power = False # off/on(True)
        self.channel = 10
        self.volume = 5     
        # 동적 멤버 변수는 매소드에 의해 관리
        # 매소드: 변수 조작 용도

    
    # 멤버 함수(기능) 
    def changePower(self):
        self.power = not(self.power) # 반전(F->T->F)

    def volumeUp(self):
        self.volume += 1
        
    def volumeDown(self):
        self.volume -= 1        
       
    def channelUp(self):
        self.channel += 1 
        
    def channelDown(self):
        self.channel -= 1
        
    def display(self):
        print(f'전원 상태: {self.power}, 채널번호: {self.channel}, 볼륨: {self.volume}')
                  
tv1 = TV()

# 객채 상태 확인
tv1.power
tv1.channel
tv1.volume

# 객체 기능 이용
tv1.changePower()
tv1.volumeUp()
tv1.channelDown()

# tv 상태 확인
tv1.display()
# 전원 상태: True, 채널번호: 9, 볼륨: 6

 