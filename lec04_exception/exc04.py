'''
시용자 정의 오류 발생시키는 방법

'''

try:
    age = int(input('나이 입력 >> '))
    if age < 0:
        raise ValueError('나이는 0 또는 양의 정수이어야 합니다.')
    print('입력한 나이:', age)
except ValueError as e:
    print(e.args)

