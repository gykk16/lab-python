'''
명시적 데이터 타입 변환(casting): int(), float(), str()

'''

print('3.1' + '1.2')
# 문자열 + 문자열: concatenate(문자열 이어 붙이기)

print(3.1 + 1.2)
#   print('3.1' + 1.2)
# 문자열(str)과 숫자(float)은 산술 연산을 할 수 없음.
# 숫자 타입으로 변환 후 산술 연산을 실행.

print(float('3.1') + 1.2)


# 간단한 계산기
x = input('>>> 숫자(x) 입력:')  # x 는 문자열
y = input('>>> 숫자(y) 입력:')

print(x + y)    # 문자열 붙이기


# 문자열 -> 실수 변환
x = float(input('>>> 숫자(x) 입력:'))   # x 를 받아서 실수 변환
y = float(input('>>> 숫자(y) 입력:'))

# print(x + y)
print(f'{x} + {y} = {x + y}')
print(f'{x} - {y} = {x - y}')
print(f'{x} * {y} = {x * y}')
print(f'{x} / {y} = {x / y}')
# ctrl + D : 커서가 위치한 줄 복사

