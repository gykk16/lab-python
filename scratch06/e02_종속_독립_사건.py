'''
사건의 종속성 vs 독립성

사건 A의 발생 여부가 사건 B의 발생 여부에 대한 정보를 제공한다면,
사건 A와 사건 B는 종속 사건(dependent event)

사건 A의 발생 여부가 사건 B의 발생 여부와 상관이 없다면,
사건 A와 사건 B는 독립 사건(independent event)

동전 2개를 던지는 경우,
A: 첫번재 동전이 앞면
B: 두번재 동전이 뒷면
C: 두 동전 모두 앞면

A와 B는 독립 사건
A와 C는 종속 사건

P(A): 사건 A가 일어날 확률
P(B): 사건 B가 일어날 확률
P(A, B): 사건 A와 사건 B의 교집합이 일어날 확률 (동시에 일어날 확률)

P(A, B) = P(A) * P(B) 이 성립하면, 두 사건은 독립 사건


'''
import random

# 자녀가 2명인 경우,
# A: 첫째가 딸인 경우
# B: 둘째가 아들인 경우
# C: 둘 다 딸인 경우
# A와 B가 독립 사건, A와 C는 종속 사건임을 증명
# P(A), P(B), P(C), P(A, B), P(A, C)


childs = ['M', 'F']
trials = 10_000

def test(n, childs, trials):

    cases = []
    for _ in range(trials):
        case = []
        for _ in range(n):
            x = random.choice(childs)
            case.append(x)
        cases.append(tuple(case))

    return cases

exp = test(2, childs, trials)

A, B, C, AB, AC = 0, 0, 0, 0, 0
for i, j in exp:
    if i == 'F':
        A += 1
    if j == 'M':
        B += 1
    if i + j == 'FF':
        C += 1
    if i == 'F' and j == 'M':
        AB += 1
    if i == 'F' and j == 'F':
        AC += 1

r_A = A / trials
r_B = B / trials
r_C = C / trials
r_AB = AB / trials
r_AC = AC / trials

print('P(A) =', r_A)
print('P(B) =', r_B)
print('P(C) =', r_C)
print()
print(f'P(A, B) = {r_AB} , P(A) * P(B) = {r_A * r_B}')
print(f'P(A, C) = {r_AC} , P(A) * P(C) = {r_A * r_C}')

