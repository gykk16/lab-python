'''
1) 선형 회귀식
	cty = slope * displ + intersect
의 기울기(slope)와 절편(intersect)을 경사 하강법의 3가지 방법(stochastic, batch, mini-batch)으로결정하고 값을 비교

2) 배기량과 시내 연비 산점도 그래프(scatter plot)과 선형 회귀 직선을 하나의 plot으로 출력해서 결과 확인

'''
import random
import matplotlib.pyplot as plt

from scratch04.e01_선형대수 import vector_mean
from scratch08.e03_편미분 import gradient_step
from scratch08.e04_선형회귀 import minibatches, linear_gradient

with open('mpg.csv', encoding = 'UTF-8') as f:
    # 파일 사용(read, wirte)이 모두 끝났을 때 close() 자동 호출
    f.readline()    # 첫번째 라인을 읽고 버림 - 컬럼 이름들

    # 한줄씩 읽어서 그 줄의 앞뒤 동백들(줄바꿈, \n)을 제거하고,
    # ',' 로 분자열을 분리해서 만든 리스트를 df에 저장
    df = [line.strip().split(',') for line in f]
    # strip() : 앞뒤 공백 제거 , split() : 데이터 나누기

print(df)

displ = [float(i[2]) for i in df]
cty = [float(i[7]) for i in df]
displ_cty = [(d, c) for d, c in zip(displ, cty)]
print(displ_cty[0:5])


def mini_batch_gd(dataset,
                  epochs,
                  learning_rate = 0.001,
                  batch_size = 1,
                  shuffle = True):
    dataset = dataset.copy()    # 원본 데이터를 복사해서 사용
    # 경사 하강법으로 찾으려고 하는 직선의 기울기와 절편의 초기값
    theta = [random.randint(-10, 10),
             random.randint(-10, 10)]
    print('theta 초기값:', theta)
    for epoch in range(epochs):    # epochs 횟수만큼 반복
        if shuffle:
            random.shuffle(dataset) # 무작위로 순서를 썩음

        mini_batch = minibatches(dataset, batch_size, shuffle)

        for batch in mini_batch:    # 미니 배치 크기 만큼 반복
            # 미니 배치 안의 점들에 대해서 gradient 들을 계산
            gradients = [linear_gradient(x, y, theta) for x, y in batch]
            # gradient 들의 평균을 계산
            gradient = vector_mean(gradients)
            # gradient 를 사용해서 파라미터 theta 를 변경
            theta = gradient_step(theta, gradient, -learning_rate)

    return theta

print('\n')
print('=== stochastic gradient descent ===')

theta_stochastic = mini_batch_gd(displ_cty, 500,
                                 learning_rate = 0.001,
                                 shuffle = False)
print(theta_stochastic)


print('\n')
# 미니 배치 경사 하강법에서 배치 사이즈를 데이터 길이 만큼 주면 배피 경사 하강법
print('=== batch gradient descent ===')
theta_batch = mini_batch_gd(displ_cty, 3000,
                            batch_size = len(displ_cty),
                            learning_rate = 0.01,
                            shuffle = True)
print(theta_batch)


print('\n')
print('=== mini batch gradient descent ===')
theta_mini = mini_batch_gd(displ_cty, 1000,
                            batch_size = 30,
                            learning_rate = 0.01,
                            shuffle = True)
print(theta_mini)


def linear_regression(x, theta):
    slope, intercept = theta
    return slope * x + intercept    # y = ax + b

ys_stochastic = [linear_regression(x, theta_stochastic) for x in displ]
plt.plot(displ, ys_stochastic, c = 'red', label = 'Stochastic GD')
ys_batch = [linear_regression(x, theta_batch) for x  in displ]
plt.plot(displ, ys_batch, c = 'green', label = 'Batch GD')
ys_mini = [linear_regression(x, theta_mini) for x  in displ]
plt.plot(displ, ys_mini, c = 'orange', label = 'Mini Batch GD')

plt.scatter(displ, cty, c = '0.5')
plt.xlabel('displacement(cc)')
plt.ylabel('city efficiency(mpg)')
plt.title('Fuel Efficiency vs Displacement')
plt.legend()
plt.show()