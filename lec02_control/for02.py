from typing import List, Union

import numpy as np
from math import sqrt

# 빈 리스트(scores)를 선언
from numpy.core._multiarray_umath import ndarray

scores = []

# 난수 (0 <= x <= 100) 10개를 리스트에 저장

for i in range(10):
    scores.append(np.random.randint(0, 101))

print(scores)
print()

# 리스트에 저장된 시험 점수 10개의 평균을 계산, 출력
# 리스트에 저장된 시험 점수 10개 중에서 최대값, 최소값을 찾아서 출력

print('sum =', sum(scores))
print(f'avg = {sum(scores) / len(scores)}')
print(f'max = {max(scores)} \n'
      f'min = {min(scores)}')
print(f'std = {np.std(scores)}')

print()

# 총점
s_sum = 0
for i in scores:
    s_sum += i
print('s_sum =', s_sum)

# 평균
s_avg = s_sum / len(scores)
print('s_avg =', s_avg)

# 최대값, 최소값
s_max = 0
s_min = 100
for i in scores:
    if i > s_max:
        s_max = i

    if i < s_min:
        s_min = i
print('s_max =', s_max)
print('s_min =', s_min)



# 표준편차
s_std = 0
for i in scores:
    s_std += (i - s_avg) ** 2
s_std = sqrt(s_std / (len(scores)))
print('s_std =', s_std)
print()

sorted_scores = sorted(scores)
print(sorted_scores)
