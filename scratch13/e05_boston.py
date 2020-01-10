'''
Boston house prices dataset

'''

# 보스턴 집값 데이터 세트 로딩
# 데이터 탐색 - 그래프
# 학습 세트/검증 세트 나눔
# 학습 세트를 사용해서 선형 회귀 - 단순 선형 회귀, 다중 선형 회귀
# 검증 세트를 사용해서 예측 -> 그래프
# Mean Square Error 계산
# R2-score 계산

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

boston = load_boston()
features = boston.feature_names
print(features.shape)
X, y = load_boston(return_X_y = True)

fig, ax = plt.subplots(4, 4)
ax_flat = ax.flatten()
for i in range(len(features)):
    axis = ax_flat[i]
    axis.scatter(X[:, i], y)
    axis.set_title(features[i])
plt.show()

np.random.seed(1217)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .3)
rm_train = X_train[:, np.newaxis, 5]
rm_test = X_test[:, np.newaxis, 5]
lin_reg = LinearRegression()
lin_reg.fit(rm_train, y_train)
print(f'intercept = {lin_reg.intercept_}, cofficients = {lin_reg.coef_}')

y_pred = lin_reg.predict(rm_test)

mse = mean_squared_error(y_test, y_pred)
print('Mean Square Error =', mse)
r2 = r2_score(y_test, y_pred)
print('r2 score =', r2)

plt.scatter(rm_train, y_train)
plt.plot(rm_test, y_pred, 'r')
plt.title('RM vs price')
plt.show()

###################

lstat_train = X_train[:, np.newaxis, 12]
lstat_test = X_test[:, np.newaxis, 12]

poly_feature = PolynomialFeatures(degree = 2, include_bias = False)
lstat_train_poly = poly_feature.fit_transform(lstat_train)
lstat_test_poly = poly_feature.fit_transform(lstat_test)

lin_reg.fit(lstat_train_poly, y_train)
print(f'intercept = {lin_reg.intercept_}, cofficients = {lin_reg.coef_}')

y_pred = lin_reg.predict(lstat_test_poly)

mse = mean_squared_error(y_test, y_pred)
print('Mean Square Error =', mse)
r2 = r2_score(y_test, y_pred)
print('r2 score =', r2)

plt.scatter(lstat_test, y_test)
plt.scatter(lstat_test, y_pred)
plt.title('LSTAT vs price')
plt.show()

###################

# intercept = -38.625495771022045, cofficients = [9.67174089]
# Mean Square Error = 49.422145607387066
# r2 score = 0.4407247091305826
# intercept = 42.21995505402154, cofficients = [-2.22844813  0.03991878]
# Mean Square Error = 38.8530373167884
# r2 score = 0.5603277947677918d