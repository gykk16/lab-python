'''
연속 확률 분포
1) 확률 밀도 함수(Probability Density Function: PDF)
    특정 확률 변수 구간을 적분한 값으로 확률을 계산 할 수 잇는 함수
    P(a <= x < b) = Integral from a to b [pdf(x)dx]

2) 누적 분포 함수(Cumulative Distribution Function: CDF)
    확률 변수의 값이 특정 값보다 작거나 같을 확률을 나타내는 함수
    cdf(x) = P(x <= b)

P(a <= x < b) = P(x < b) - P(x <= a)

'''
from matplotlib import pyplot as plt
import math


def uniform_pdf(x):
    ''' Uniform Distribution(균등분포) 확률 밀도 함수 '''
    return 1 if 0 <= x < 1 else 0


def uniform_cdf(x):
    ''' 균등 분포 누적 분포 함수 '''
    if x < 0:
        return 0
    elif 0 <= x < 1:
        return x
    else:
        return 1


SQRT_TWO_PI = math.sqrt(2 * math.pi)


def normal_pdf(x, mu = 0.0, sigma = 1.0):
    ''' 평균이 mu 이고, 표준편차가 sigma 인 정규 분포(Normal Distribution) 확률 밀도 함수 '''
    return math.exp(-(x - mu) ** 2 / (2 * sigma) ** 2) / (SQRT_TWO_PI * sigma)


def normal_cdf(x, mu = 0.0, sigma = 1.0):
    ''' 평균이 mu 이고, 포준편차가 sigma 인
    정규 분포(Normal Distribution)의 누적 분포 함수(Cumulative Distribution)
     math.erf() 함수(error function)를 이용해서 구현
     '''
    return (1 + math.erf((x - mu) / (math.sqrt(2) * sigma))) / 2


def inverse_normal_cdf(p, mu = 0.0, sigma = 1.0, tolerance = 0.0001):
    ''' 누적 함수 P 를 알고 있을때 정규 분포 확률 변수 x= ? '''
    # 표준 정규 분포가 아니라면 표준 정규 분포로 변환
    if mu != 0.0 or sigma != 1.0:
        return mu + sigma * inverse_normal_cdf(p, tolerance = tolerance)
    low_z, low_p = -10.0, 0
    high_z, high_p = 10.0, 1.0
    while high_z - low_z > tolerance:
        mid_z = (low_z + high_z) / 2.0  # 중감값
        mid_p = normal_cdf(mid_z)  # 중간 값에서의 누적 확률
        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        else:
            high_z, high_p = mid_z, mid_p

    return mid_z


if __name__ == '__main__':
    # -2 <= x <= 2 구간을 0.1씩 나눔
    xs = [x / 10 for x in range(-20, 21)]
    print(xs)
    ys = [uniform_pdf(x) for x in xs]
    print(ys)

    plt.plot(xs, ys)
    plt.title('Uniform Distribution PDF')
    plt.show()

    ys2 = [uniform_cdf(x) for x in xs]
    plt.plot(xs, ys2)
    plt.title('Uniform Distribution CDF')
    plt.show()

    xs = [x / 10 for x in range(-50, 51)]
    # mu(평균) = 0.0, sigma(표준편차) = 1.0
    ys3 = [normal_pdf(x) for x in xs]
    # mu(평균) = 0.0, sigma(표준편차) = 2.0
    ys4 = [normal_pdf(x, sigma = 2.0) for x in xs]
    # mu(평균) = 0.0, sigma(표준편차) = 0.5
    ys5 = [normal_pdf(x, sigma = 0.5) for x in xs]
    # mu(평균) = -1.0, sigma(표준편차) = 1.0
    ys6 = [normal_pdf(x, mu = -1.0) for x in xs]

    plt.plot(xs, ys3, '-', label = 'mu = 0, sigma = 1')
    plt.plot(xs, ys4, '--', label = 'mu = 0, sigma = 2')
    plt.plot(xs, ys5, ':', label = 'mu = 0, sigma = 0.5')
    plt.plot(xs, ys6, '-.', label = 'mu = -1, sigma = 1')
    plt.legend()
    plt.title('Normal Distribution PDF')
    plt.show()

    #####################

    xs = [x / 10 for x in range(-50, 51)]
    # mu(평균) = 0.0, sigma(표준편차) = 1.0
    ys1 = [normal_cdf(x) for x in xs]
    # mu(평균) = 0.0, sigma(표준편차) = 2.0
    ys2 = [normal_cdf(x, sigma = 2.0) for x in xs]
    # mu(평균) = 0.0, sigma(표준편차) = 0.5
    ys3 = [normal_cdf(x, sigma = 0.5) for x in xs]
    # mu(평균) = -1.0, sigma(표준편차) = 1.0
    ys4 = [normal_cdf(x, mu = -1.0) for x in xs]

    plt.plot(xs, ys1, '-', label = 'mu = 0, sigma = 1')
    plt.plot(xs, ys2, '--', label = 'mu = 0, sigma = 2')
    plt.plot(xs, ys3, ':', label = 'mu = 0, sigma = 0.5')
    plt.plot(xs, ys4, '-.', label = 'mu = -1, sigma = 1')
    plt.legend()
    plt.title('Normal Distribution CDF')
    plt.show()

    ######################

    # 누적 확률이 0.9, 0.99, 0.999 인 확률 변수 x를 찾음
    # 표준 정규 분포표와 비교

    x1 = inverse_normal_cdf(0.9)
    print('x1 =', x1)
    x2 = inverse_normal_cdf(0.99)
    print('x2 =', x2)
    x3 = inverse_normal_cdf(0.999)
    print('x3 =', x3)
