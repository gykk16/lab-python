'''
확률

사건 공간(universe of events)
사건(event)
확률(probability)

'''

import random
from collections import Counter

coin = ['H', 'T']
dice = [1, 2, 3, 4, 5, 6]
print(random.choice(coin))

# 동전 1개를 10,000번 던지는 실험
# 앞면(H)이 나올 확률과 뒷면(T)이 나올 확률이 1/2 임을 증명

coin = ['H', 'T']
trials = 100_000
head, tail = 0, 0
for i in range(trials):
    x = random.choice(coin)
    if x == 'H':
        head += 1
    else:
        tail += 1

p_H = head/trials
p_T = tail/trials
print('앞면(H)이 나올 확률 =', p_H)
print('뒷면(T)이 나올 확률 =', p_T)

print()

# 동전 2개를 던지는 실험 (10,000번)
# 1) 앞면의 갯수가 1개일 확률 (HT, TH)
# 2) 첫번째 동전이 앞면일 확률 (HH, HT)
# 3) 적어도 한 개의 동전이 앞면일 확률 (HH, HT, TH)

coin = ['H', 'T']
trials = 10_000

hh, tt = 0, 0
ht, th = 0, 0
for i in range(trials):
    coin1 = random.choice(coin)
    coin2 = random.choice(coin)
    x = coin1 + coin2
    if x == 'HH':
        hh += 1
    elif x == 'HT':
        ht += 1
    elif x == 'TH':
        th += 1
    else:
        tt += 1
hh /= trials
ht /= trials
th /= trials
tt /= trials

print('앞면의 갯수가 1개일 확률 (HT, TH) =', ht + th)
print('첫번째 동전이 앞면일 확률 (HH, HT) =', hh + ht)
print('적어도 한 개의 동전이 앞면일 확률 (HH, HT, TH) =', hh + ht + th)


print()
# 동전 3개를 던지는 실험 (10,000번)
# 앞면의 개수가 1개일 확률


def find_h1(_list_):
    count = Counter(_list_)
    for i, j in count.items():
        if i == 'H' and j == 1:
            return 1


coin = ['H', 'T']
trials = 10_000
r = 0
for i in range(trials):
    coin1 = random.choice(coin)
    coin2 = random.choice(coin)
    coin3 = random.choice(coin)
    x = [coin1, coin2, coin3]
    # print(x)

    # if x == ['H', 'T', 'T'] or x == ['T', 'H', 'T'] or x == ['T', 'T', 'H']:
    #     r += 1
    if find_h1(x) == 1:
        r += 1


print('앞면의 개수가 1개 일 확률 =', r / trials)

print()
print()
print()

################################
################################

def experiment(n, trials, item):
    '''

    :param n: 동전, 주사위 등의 개수
    :param trials: 실험 횟수
    :param item : 동전, 주사위 등
    :return: list
    '''

    cases = []  # 동전 던지기 실험 결과를 저장
    for _ in range(trials):
        case = []   # 각 실험의 결과를 저장
        for _ in range(n):
            rand = random.choice(item)
            case.append(rand)
        cases.append(tuple(case))
        # Counter 클래스는 tuple의 개수는 셀 수 있지만 list의 개수는 셀 수 없다

    return cases


coin = ['H', 'T']
trials = 10_000

coin_exp = experiment(3, trials, coin)
print(coin_exp)

coin_event_counts = Counter(coin_exp)
print('coin_event_counts =', coin_event_counts)
print()


def how_many_heads(x):
    counter = Counter(x)
    # print('counter =', counter)
    return counter['H']


num_of_cases = 0
for i, j in coin_event_counts.items():
    if how_many_heads(i) == 1:
        num_of_cases += j

p_h1 = num_of_cases / trials
print('P(앞면이 1개 일 확률) =', p_h1)

num_of_cases = 0
for i, j in coin_event_counts.items():
    if i[0] == 'H':
        num_of_cases += j

p_h_first = num_of_cases / trials
print('P(첫번째 동전이 앞면일 확률) =', p_h_first)

num_of_cases = 0
for i, j in coin_event_counts.items():
    if how_many_heads(i):
        num_of_cases += j

p_h_has = num_of_cases / trials
print('P(적어도 한 개의 동전이 앞면일 확률) =', p_h_has)


print()
print()

# 주사위 2개를 던졌을 때, 두 눈의 합이 8일 확률
# 주사위 2개를 던졌을 때, 적어도 하나가 짝수가 나올 확률

dice = [1, 2, 3, 4, 5, 6]
trials = 1_000_000

exp = experiment(2, trials, dice)
print(exp)

# 1)
x = 0
for i, j in exp:
    if i + j == 8:
        x += 1
r = x / trials
print('주사위 2개를 던졌을 때, 두 눈의 합이 8일 확률 =', r)

# 2)
x = 0
for i, j in exp:
    if i % 2 == 0 or j % 2 == 0:
        x += 1
r = x / trials
print('주사위 2개를 던졌을 때, 적어도 하나가 짝수가 나올 확률 =', r)


