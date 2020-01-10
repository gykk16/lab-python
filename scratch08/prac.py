from collections import Counter

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

boston = load_boston()
X = boston.data
y = boston.target
features = boston.feature_names

print(features)

fig, ax = plt.subplots(4, 4)
ax_flat = ax.flatten()
for i in range(len(features)):
    axis = ax_flat[i]
    axis.scatter(X[:, i], y)
    axis.set_title(features[i])
plt.show()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .3)

X_train_rm = X_train[:, np.newaxis, 5]  # 2차원 배열
X_test_rm = X_test[:, np.newaxis, 5]
print(f'X_train_rm: {X_train_rm.shape}, X_test_rm: {X_test_rm.shape}')
print()

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred = lin_reg.predict(X_test)

plt.scatter(X_test_rm, y_test)
plt.plot(X_test_rm, y_pred)
plt.show()


plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred, 'r-')
plt.show()

plt.scatter(X_train, y_train)
plt.plot(X_test, y_pred, 'r-')
plt.show()