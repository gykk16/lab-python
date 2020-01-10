'''
선형 회귀(linear regression)
    y = b + a * x
    y = b0 + b1 * x1 + b2 * x2 + ...

1개의 figure 에 10개의 subplot 를 그려서, 변수들과 당뇨병(y)의 대략적이 관계를 파악.
y ~ age, y ~ sex, y ~ bmi, ...

'''

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y = True)
print(X[:5])

datasets = load_diabetes()
features = datasets.feature_names
print(y[:5])

# X = pd.DataFrame(X, columns = features)
# print(X.head())

fig, ax = plt.subplots(3, 4)
x_idx = 0
for row in range(3):
    for col in range(4):
        axis = ax[row, col]

        if x_idx == 10:
            break
        axis.set_title(features[x_idx])
        axis.scatter(X[:, x_idx], y)
        x_idx += 1

plt.show()
