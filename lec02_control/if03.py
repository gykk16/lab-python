'''
    가위(1), 바위(2), 보(3)

'''
import numpy as np

rsp = ['가위', ' 바위', '보']

print('가위 바위 보 게임')
print('''
    [1] 가위
    [2] 바위
    [3] 보
''')
print('-----------------')
print('선택>> ')

user = int(input())

computer = np.random.randint(1, 4)  # 1 <= com < 4 난수
print(computer)


if user > 3:
    print('User 반칙')

elif user == computer:
    print('Draw')
elif user == 1 and computer == 3:
    print('Player Win')
elif user > computer:
    print('Player Win')
else:
    print('Player Lose')


