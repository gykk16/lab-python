'''
for-in 연습 구문
'''

# 피보나치 수열(fibonacci sequence)
# f[0] = 0, f[1] = 1
# f[n] = f[n-1] + f[n-2], n >= 2

# 피보나치 수열 원소 20개짜리 리스트 생성

f = [0, 1]
for n in range(2, 20):
    f.append(f[n - 1] + f[n - 2])
print(f)
print()
# 소수(prime number): 1과 자기자신으로만 나우어지는 정수
# 2부터 10까지

for n in range(2, 11):
    isPrime = True
    for x in range(2, n):
        if n % x == 0:
            isPrime = False
            print(f'{n} / {x} = {n / x}')
            break
    if isPrime:
        print(f'{n}은 소수')
print()

# for/while 반복문과 else가 함께 사용되는 경우:
# 반복문이 break 를 만나지 않고 범위 전체를 반복했을 때
# else 블록이 실행
# 반복문 중간에 break 를 만나면 else는 실행되지 않음
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print('모든 반복을 끝냄')
print()
# print('모든 반복을 끝냄')

# for-else 구문을 이용한 소수 찾기
for n in range(2, 11):
    for x in range(2, n):
        if n % x == 0:
            print(f'{n} / {x} = {n / x}')
            break
    else:   # break를 만나지 않았을 때
        print(f'{n}은(는) 소수')
print()