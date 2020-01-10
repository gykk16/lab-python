'''
while 반복문:

[초기식]
while 조건식:
    조건식이 참인 동안에 실행할 문장
    [조건을 변경 할 수 있는 식]

'''

# 1 2 3 .. 10
n = 1
while n <= 10:
    print(n, end=' ')
    n += 1

print()
print()

# 구구단 2단 출력
n = 1
while n < 10:
    print(f'2 * {n} = {2 * n}')
    n += 1
print()

# 구구간 9단까지 출력
# 2중 while문 사용
x = 2
while x < 10:
    n = 1
    while n < 10:
        print(f'{x} * {n} = {x * n}')
        n += 1
    x += 1
    print()
print()

x = 2
while x < 10:
    n = 1
    while n < 10:
        print(f'{x} * {n} = {x * n}')
        if x == n:
            break
        n += 1
    x += 1
    print()
print()

