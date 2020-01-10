import numpy as np

def user_input():
    '''
    가위바위보 게임
    사용자에게 1, 2, 3 중 하나의 숫자를 입력하도록 안내.
    사용자가 입력한 숫자를 return.
    사용자가 숫자로 변활 할 수 없는 문자를 입력하면, 안내문 출력 후 재입력 받음.
    사용자가 1, 2, 3 이외의 숫자를 입력하면, 안내문 출력후에 재입력 받음.

    :return: 1, 2, 3 중 하나
    '''
    print('''
    1 : 가위
    2 : 바위
    3 : 보
    ''')

    while True:
        try:
            x = int(input('1, 2, 3 입력 >>> '))
            if x in (1, 2, 3):
                return x
            else:
                raise ValueError()
        except ValueError:
            print('1, 2, 3 중에 입력하세요.')


user = user_input()
print('user =', user)
print('computer =', np.random.randint(1, 4))

