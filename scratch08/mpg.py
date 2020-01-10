import os
import random
import matplotlib.pyplot as plt

from scratch04.e01_선형대수 import vector_mean
from scratch04.e03_리스트_행렬 import shape

from lec07_file.file07_ import my_csv_reader, print_data
from scratch08.e01_경사하강법 import difference_quotient, f, tangent
from scratch08.e03_편미분 import gradient_step
from scratch08.e04_선형회귀 import linear_gradient, minibatches

def f(x, theta):
    ''' y = ax + b '''

    return


print(os.getcwd())
mpg = my_csv_reader('..\data\mpg.csv', header = False)
print(mpg)
print()
print_data(mpg)
shape = shape(mpg)
print()
print(shape)

displ = [float(i[3]) for i in mpg]
cty = [int(i[8]) for i in mpg]
dataset = [(float(i[3]), int(i[8])) for i in mpg]

print(displ)
print(cty)
print(dataset)
################
print('\n \n')
################

# cty = slope * displ + intersect 의 기울기(slope)와 절편(intersect)을
# 경사 하강법의 3가지 방법(stochastic, batch, mini-batch)으로 결정하고 값을 비교

print('=== 확률적 경사 하강법 ===')

theta = [1, 1]
step = 0.001

for epoch in range(500):
    random.shuffle(dataset)

    for x, y in dataset:
        gradient = linear_gradient(x, y, theta)
        theta = gradient_step(theta, gradient, -step)

    if (epoch + 1) % 50 == 0:
        print(f'{epoch} : {theta}')

#######################
print('\n \n')
#######################

print('=== 배치 경사 하강법 ===')

step = 0.001
theta = [1, 1]
for epoch in range(50_000):
    gradients = [linear_gradient(x, y, theta) for x, y in dataset]
    gradient = vector_mean(gradients)
    theta = gradient_step(theta, gradient, -step)

    if (epoch + 1) % 5000 == 0:
        print(f'{epoch} : {theta}')

#######################
print('\n \n')
#######################

print('=== 미니 배치 경사 하강법 ===')

theta = [1, 1]  # 임의의 파라미터 시작값
step = 0.001    # 학습률
for epoch in range(5000):
    mini_batches = minibatches(dataset, 20, True)
    for batch in mini_batches:
        gradients = [linear_gradient(x, y, theta) for x, y in batch]
        gradient = vector_mean(gradients)
        theta = gradient_step(theta, gradient, -step)
    if (epoch + 1) % 500 == 0:
        print(f'{epoch}: {theta}')

#######################
print('\n \n')
#######################

print(theta[0])


def f(x, theta):
    ''' y = mx + b '''
    return theta[0] * x + theta[1]

estimate = [f(x, theta) for x in displ]

# cty = slope * displ + intersect
plt.scatter(displ, cty)
plt.plot(displ, estimate, color = 'red')
plt.xlabel('displ')
plt.ylabel('cty')
plt.axis()
plt.show()








