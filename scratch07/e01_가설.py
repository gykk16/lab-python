'''
가설(Hypothesis)와 통계적 추론(Interface)

귀무가설(영가설, null hypothesis), H0

대립가설(alternative hypothesis), H1

(예)
H0: 동전을 던졌을 때 앞면이 나올 확률 p = 1/2
H1: 동전을 던졌을 때 앞면이 나올 확률은 1/2이 아니다(p != 1/2)

(예)
H0: 동전을 던졌을 때 앞면이 나올 확률은 p > 1/2
H1: 동전을 던졌을 때 앞면이 나올 확률은 p <= 1/2

제1종 오류(type I error):
   실제는 가설이 참인데, 가설을 기각하는 오류
제2종 오류(type II error):
   실제는 가설이 거짓인데, 가설을 기각하지 않는 오류
유의 수준(significance level): alpha
   제1종 오류가 발생할 확률의 최대 허용 한계
   alpha = 0.05(5%), 0.01(1%), ...
   유의 수준에 따라서 가설을 기각할 것인지, 아닌지를 결정
beta: 가설이 거짓인데 기각하지 못하는 확률
검정력(power): 1 - beta
   귀무가설의 잘못을 찾아낼 확률


'''

import math

from scratch06.e06_연속확률분포 import normal_cdf, inverse_normal_cdf


def normal_approximation_to_binomial(n, p):
    """ 이항분포(n, p)를 정규 분포로 근사했을 때 mu(평균)과 sigma(표준편차) """
    mu = n * p
    sigma = math.sqrt(n * p * (1 - p))
    return mu, sigma


# 확률 변수가 어떤 구간 안(밖)에 존재할 확률
# P(X <= b), P(X >= a), P(a <= X <= b)
# scratch06 에서 작성했던 normal_cdf 함수를 이용

# P(X <= high): 확률 변수 값이 특정 값보다 작(거나 같)을 확률 = cdf(high)
normal_probability_below = normal_cdf

# P(X > low): 확률 변수 값이 특정 값보다 클 확률 = 1 - P(X < low)
def normal_probability_above(low, mu = 0.0, sigma = 1.0):
    return 1 - normal_cdf(low, mu, sigma)


# P(low < X < high): 확률 변수 값이 특정 범위 안에 있을 확률
# = P(X < high) - P(X < low)
def normal_probability_between(low, high, mu = 0.0, sigma= 1.0):
    return normal_cdf(high, mu, sigma) - normal_cdf(low, mu, sigma)


# P(X < low or X > high): 확률 변수가 특정 범위 밖에 있을 확률 (low < high)
# =1 - P(low < X < high)
def normal_probability_outside(low, high, mu = 0.0, sigma = 1.0):
    return 1 - normal_probability_between(low, high, mu, sigma)


# 확률이 주어졌을 때, 상한(upper bound) 또는 하한(lower bound)
# 또는 범위(lower ~ upper bound)를 찾는 함수들

# P(X < ub) = prob 이 주어졌을 때, 상한 ub 를 찾는 함수
def normal_upper_bound(prob, mu = 0.0, sigma = 1.0):
    return inverse_normal_cdf(prob, mu, sigma)


# P(X > lb) = prob 이 주어졌을 때, 하한 lb 를 찾는 함수
# P(X < lb) = 1 - prob 이 주어졌을 때, 상한 lb를 찾는 함수
def normal_lower_bound(prob, mu = 0.0, sigma = 1.0):
    return inverse_normal_cdf(1 - prob, mu, sigma)


# P(lb < X < ub) = prob 이 주어졌을 때,
# 평균을 중심으로 대칭이 되는 구간의 상한(ub)과 하한(lb)를 찾는 함수
def normal_two_sided_bounds(prob, mu = 0.0, sigma = 1.0):
    # 양쪽 끝(tail)에 해당하는 확률
    tail_prob = (1 - prob) / 2

    # 찾으려는 상한(upper bound)는 확률 tail_prob 이상을 갖는 하한을 찾으면 됨
    # P(X > a) = tail_prob 을 만족하자는 하한 a를 찾으면 됨
    upper_bound = normal_lower_bound(tail_prob, mu, sigma)
    # 또는 P(X < b) = prob + tail_prob 을 만족하는 상한 b를 찾으면 됨
    # upper_bound = normal_upper_bound(prob + tail_prob, mu, sigma)

    # 찾으려는 하한(lower bound)는 확률 tail_prob 이하를 갖는 상한을 찾으면 됨
    # P(X < b) = tail_prob 을 만족하는 상한 b를 찾으면 됨
    lower_bound = normal_upper_bound(tail_prob, mu, sigma)

    return lower_bound, upper_bound


def two_sided_p_value(x, mu = 0, sigma = 1):
    ''' 양측 검정에서 사용하는 p-value '''
    if x >= mu:
        return normal_probability_above(x, mu, sigma) * 2
    else:
        return normal_probability_below(x, mu, sigma) * 2


def estimate_parameters(N, n):
    ''' 표본(샘플)의 평균으로 모집단의 평균, 표준편차 추정
        N: 실험 횟수, n: 발견된 횟수 '''
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma


def a_b_test_statistic(N_a, n_a, N_b, n_b):
    ''' 리턴값의 의미는 표준 정규부포에서 p-value 를 계산 할 수 있는 z 값'''
    p_a, sigma_a = estimate_parameters(N_a, n_a)
    p_b, sigma_b = estimate_parameters(N_b, n_b)
    return (p_b - p_a) / math.sqrt(sigma_a ** 2 + sigma_b ** 2)


if __name__ == '__main__':
    # 동전을 던졌을 때 앞면이 나올 확률은 1/2(= 0.5) testing(검정)
    # 동전을 1,000번 던지는 실험 - 이항 분포
    # 앞면이 나오는 기대값 - 정규분포(np, sqrt(np(1 - p))

    # 영가설(귀무가설)
    # H0: p = 1/2
    # 영가설이 참이라는 가정 아래서, 동전이 앞면이 나오는 확률의평균과 표준 편차는
    mu_0, sigma_0 = normal_approximation_to_binomial(1_000, 0.5)
    print(f'p = 0.5 가정 : mu_0 = {mu_0}, sigma_0 = {sigma_0}')

    # 유의 수준 5%
    # H0이 참이지만 기각을 하는 오류를 5% 감수
    # H0를 기각하지 않을 확률 95% 의 상한과 하한을 찾음
    low, high = normal_two_sided_bounds(0.95, mu_0, sigma_0)
    print(f'low = {low}, high = {high}')
    print()


    # H0: 동전을 던졌을 때 앞면이 나올 확률 p = 1/2
    # H1: 동전을 던졌을 때 앞면이 나올 확률은 1/2이 아니다(p != 1/2)
    # 유의수준(alpha): 영가설이 참인데 가설을 기각할 가능성
    # beta: 영가설이 거짓인데 가설을 기각하지 않을 가능성
    # 검정력(power of test) = 1 - beta

    # 만약 동전 앞면이 나올 확률이 1/2이 아니라고 가정
    # 동전 앞면이 나올 확률을 0.55 라고 가정 했을 때 평균과 표준편차
    mu_1, sigma_1 = normal_approximation_to_binomial(1_000, 0.55)
    print(f'p = 0.55 가정 : mu_1 = {mu_1}, sigma_1 = {sigma_1}')

    # p = 0.5 가정에서 95% 구간이, p = 0.55 가정에서 나올 확률
    beta = normal_probability_between(low, high, mu_1,sigma_1)
    # p = 0.55 가정이 맞다고 할 오류
    print('beta =', beta)
    power = 1 - beta
    # p = 0.55 가정이 틀렸다고 검증할 수 있는 능력
    print('power =', power) # 0.8865
    print()

    # 동전 앞면이 나올 확률을 0.45 라고 가정 했을 때 평균과 표준편차
    mu_2, sigma_2 = normal_approximation_to_binomial(1_000, 0.45)
    print(f'p = 0.45 가정 : mu_2 = {mu_2}, sigma_2 = {sigma_2}')
    beta = normal_probability_between(low, high, mu_1, sigma_1)
    print('beta =', beta)
    power = 1 - beta
    print('power =', power)
    print()


    # H0: p <= 0.5
    # H1: p > 0.5
    # p = 0.5 일때 유의 수준(5%)의 upper bound 구간
    high = normal_upper_bound(0.95, mu_0, sigma_0)
    print('유의수준 5% 상한 =', high)
    beta = normal_probability_below(high, mu_1, sigma_1)
    print('단측 검정: beta =', beta)
    power = 1 - beta
    print('단측 검정 검정력 =', power)
    print()

    # H0: p >= 0.5
    # H1: p < 0.5   (i.e. p = 0.45)
    # p = 0.5 가정한 정규 분포에서 유의수준 5% lower bound 를 찾음
    # beta: p = 0.45 가정한 정규 분포에서 lower bound 보다 큰 확률
    low = normal_lower_bound(0.95, mu_0, sigma_0)
    print('유의수준 5% 하한 =', low)
    beta = normal_probability_above(low, mu_2, sigma_2)
    print('단측 검정: beta =', beta)
    power = 1 - beta
    print('단측 검정 검정력 =', power)
    print()


    # p-value: H0이 참이라고 가정할 때,
    # 실험에서 관측된 값보다 더 극단적인 값이 관측될 확률

    # p-value(극단적인 값이 나올 확률)이 유의수준(5%)보다 작다면,
    # 그 값은 우연히 발생한 값이라고 생각할 수 있다.
    # -> H0를 기각함

    # p-value가 유의수준 보다 크다면,
    # 그 값은 우연히 발생한 값이라고 말 할 수 없다.
    # -> H0를 기각하지 않음 (H0를 채택)

    # 동전을 1,000번 던지는 실험에서 동전의 앞면이 530번 나왔다.
    # H0: p = 0.5
    p_value = two_sided_p_value(530, mu_0, sigma_0)
    print(p_value)  # 0.0577 > 0.05(유의수준)
    print()

    # 동전은 1000번 던져서 앞면이 525번 발생
    # -> 앞면의 확률 p = 525/1000 = 0.525
    p_bar = 525/1000
    mu = p_bar  # 모집단의 평균을 실험값의 평균으로 대체
    sigma = math.sqrt(p_bar * (1 - p_bar) / 1000)   # 표본의 표주편차로 모집단의 표준편차를 추정
    bounds = normal_two_sided_bounds(0.95, mu, sigma)
    print(bounds)   # 0.4940, 0.5559   (0.5가 둘 사이에 있어야 함)
    # 실험을 통해서 찾은 95% 신뢰 구간
    # 진짜 p값(앞면이 나올 진짜 확률)은 위 구간에 포함된다
    # 95% 확신할 수 있다.

    # 동전은 1000번 던져서 앞면이 540번 발생
    # -> 앞면의 확률 p = 540/1000 = 0.540
    p_bar = 540/1000    # 표본 평균
    mu = p_bar  # 모집단 평균
    sigma = math.sqrt(p_bar * (1 - p_bar) / 1000)   # 모집단의 표준편차
    bounds = normal_two_sided_bounds(0.95, mu, sigma)
    print(bounds)   # 0.5091, 0.5708
    # p = 0.5인 가설은 신뢰 구간에 포함되지 못함

    print()

    # A/B Test
    # N_a = 1000, n_a = 200, N_b = 1000, n_b = 180 (또는 150)
    z1 = a_b_test_statistic(1000, 200, 1000, 180)
    print('z1 =', z1)   # -1.1403
    p_value_1 = two_sided_p_value(z1)
    print('p-value 1 =', p_value_1) # 0.2541
    # p-value > 0.05
    # A와 B의 차이

    # N_a = 1000, n_a = 200, N_b = 1000, n_b = 150 (또는 150)
    z2 = a_b_test_statistic(1000, 200, 1000, 180)
    print('z2 =', z2)  # -1.1403
    p_value_2 = two_sided_p_value(z2)
    print('p-value 2 =', p_value_2)  # 0.2541
















