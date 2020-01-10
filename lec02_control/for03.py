# for 구문 연습

##### 구구단 2단부터 9단까지 출력

for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}')
    print()

##### 구구단 2단은 2 * 2, 3단은 3 * 3, 4단은 4 * 4, ... 출력

for i in range(2, 10):
    for j in range(1, i + 1):
        print(f'{i} * {j} = {i * j}')
    print()

for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j}')
        if i == j:
            break   # break가 포함된 가장 가까운 반복문 종료
    print()

for i in range(1, 10):
    if i == 5:
        break
        # 반복문 빠저나가기
    print(i, end = ' ')
print()

for i in range(1, 10):
    if i == 5:
        continue
        #  반복문 처음 부분으로 이동해서 계속 실행
    print(i, end = ' ')
print()