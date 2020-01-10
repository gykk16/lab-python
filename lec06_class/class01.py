'''
클래스(class):
    프로그램에서 만들려고 하는 대상(객체)이 가져야 할 속성(데이터)과 기능(함수)을 묶은 "데이터 타입"

메소드(method): 클래스가 가지고 있는 함수
필드(field): 클래스가 가지고 있는 데이터(변수)

'''

# TV 소프트웨어 작성
# TV 속성(데이터): 채널, 음량, 전원
# TV 기능: 채널 변경, 음량 변경, 전원 on/off

class BasicTv:
    '''
    BasicTv 클래스
    '''
    # 생성자가 호출 되었을 때 자동으로 실행되는 메소드(함수)
    def __init__(self, power, channel, volume):
        print('BasicTv 생성자 호출')
        self.power = power
        self.channel = channel
        self.volume = volume
        self.ch_max = 5
        self.ch_min = 1
        self.vol_max = 5
        self.vol_min = 0


    def powerOnOff(self):
        if self.power:  # power가 True이면(TV가 켜져 있으면)
            self.power = False  # TV를 끔

            print('TV Off')
        else:   # TV가 꺼져 있으면
            self.power = True   # TV를 켬

            print('TV On')


    def channelUp(self):
        if self.power:
            self.channel += 1
            if self.channel > self.ch_max:
                self.channel = self.ch_min

            print('Channel:', self.channel)
        else:
            print('전원 꺼짐')


    def channelDown(self):
        if self.power:
            self.channel -= 1
            if self.channel < self.ch_min:
                self.channel = self.ch_max

            print('Channel:', self.channel)
        else:
            print('전원 꺼짐')


    def volumeUp(self):
        if self.power:
            self.volume += 1
            if self.volume > self.vol_max:
                self.volume = self.vol_max

            print('Volume :', self.volume)
        else:
            print('전원 꺼짐')


    def volumeDown(self):
        if self.power:
            self.volume -= 1
            if self.volume < self.vol_min:
                self.volume = self.vol_min

            print('Volume :', self.volume)
        else:
            print('전원 꺼짐')


# 클래스 설계(정의)

# 클래스 객체(인스턴스)를 생성해서 변수에 저장
# 생성자(constructor) 호출 -> 객체(object) 생성

tv1 = BasicTv(power = False, channel = 0, volume = 0)
print(tv1)
print()
tv1.powerOnOff()    # TV 켬
print()
tv1.channelUp()
tv1.channelUp()
tv1.channelUp()
print()
tv1.powerOnOff()
print()
tv1.channelUp()
tv1.channelUp()
print()
tv1.powerOnOff()
print()
tv1.channelUp()
tv1.channelUp()
tv1.channelUp()
tv1.channelUp()
print()
tv1.channelDown()
tv1.channelDown()
tv1.channelDown()
print()
tv1.volumeUp()
tv1.volumeUp()
tv1.volumeUp()
tv1.volumeUp()
tv1.volumeUp()
tv1.volumeUp()
print()
tv1.volumeDown()
tv1.volumeDown()
tv1.volumeDown()
tv1.volumeDown()
tv1.volumeDown()
tv1.volumeDown()
print()
tv1.powerOnOff()