'''
gradient descent 연습

'''
import matplotlib.pyplot as plt

from scratch08.e01_경사하강법 import difference_quotient, move, tangent


def g(x):
    ''' y = (1 / 3 x ** 3 - x) '''
    return x ** 3 / 3 - x


if __name__ == '__main__':
    # e01 에서 작성한 함수 이용
    # 함수 g(x) 의 그래프를 그림
    # 극값(local 최소/최대) 를 경사 하강법으로 찾음

    ###########

    # 그래프를 그릴 x 좌표들: (-3.0, -2.9, ... , 2.9, 3.0)
    xs = [x / 10 for x in range(-30, 31)]
    # 그래프를 그릴 y 좌표들
    ys = [g(x) for x in xs]
    init_x1 = -2
    init_x2 = 2
    tolerance = 0.0000001

    count = 0
    while True:
        count += 1
        gradient1 = difference_quotient(g, init_x1, h= 0.0000001)
        tangent_estimates1 = [tangent(x1, gradient1, init_x1, g(init_x1)) for x1 in xs]
        plt.plot(xs, tangent_estimates1, label = f'x1 = {init_x1}', lw = 0.4)

        next_x1 = move(init_x1, gradient1, step = 0.7)
        ###
        gradient2 = difference_quotient(g, init_x2, h= 0.0000001)
        tangent_estimates2 = [tangent(x2, gradient2, init_x2, g(init_x2)) for x2 in xs]
        plt.plot(xs, tangent_estimates2, label = f'x2 = {init_x2}', lw = 0.4)

        next_x2 = move(init_x2, gradient2, step = -0.7)

        print(f'{count}: x1 = {next_x1}, x2 = {next_x2}')
        if abs(init_x1 - next_x1) < tolerance and abs(init_x2 - next_x2) < tolerance:
            break
        else:
            init_x1 = next_x1
            init_x2 = next_x2

    plt.plot(xs, ys, c = 'black', lw = 4)
    plt.axhline(y = 0, color = 'black')
    plt.axvline(x = 0, color = 'black')
    plt.axvline(x = 1, color = '0.9')
    plt.axvline(x = -1, color = '0.9')
    plt.legend()
    plt.ylim(bottom = -1.5, top = 1.5)
    plt.show()





