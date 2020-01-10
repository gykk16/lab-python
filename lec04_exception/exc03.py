'''
try-except 구문 활용

'''

while True:
    try:
        n = int(input('정수 입력 >> '))
        print('n =', n)
        break
    except ValueError:
        print('입력 값은 정수이어야 합니다.')


print('프로그램 정상 종료')