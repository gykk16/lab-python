import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

# 보스턴 집값 데이터 세트 로딩
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

dataset = load_boston()
print(type(dataset))
print(dataset.keys())
# print(dataset['DESCR'])  # dataset.DESCR

X = dataset['data']  # dataset.data
y = dataset['target']  # dataset.target
# print('X shape :', X.shape, 'y shape :', y.shape)  # X shape : (506, 13) y shape : (506,)

features = dataset['feature_names']  # dataset.feature_names

# d = {'my_name': '오쌤', 'my_age': 16}
# print(d['my_name'])

# 데이터 탐색 -> y ~ feature 산점도 그래프
fig, ax = plt.subplots(4, 4)  # 16개의 subplot을 생성
ax_flat = ax.flatten()
for i in range(len(features)):  # 특성(변수)들의 개수만큼 반복
    axis = ax_flat[i]
    axis.scatter(X[:, i], y)  # y ~ feature 산점도 그래프
    axis.set_title(features[i])  # subplot에 타이틀 추가
plt.show()

# 학습 세트/검증 세트 나눔
np.random.seed(1217)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)
print(f'X_train len: {len(X_train)}, X_test len: {len(X_test)}')

# 학습 세트를 사용해서 선형 회귀 - 단순 선형 회귀, 다중 선형 회귀
# price = b0 + b1 * rm: 주택 가격 ~ 방의 개수(rm)
X_train_rm = X_train[:, np.newaxis, 5]  # 2차원 배열
X_test_rm = X_test[:, np.newaxis, 5]
print(f'X_train_rm: {X_train_rm.shape}, X_test_rm: {X_test_rm.shape}')
print()

lin_reg = LinearRegression()  # Linear Regression 객체 생성
lin_reg.fit(X_train_rm, y_train)  # fit(적합)/학습(training) -> b0, b1 찾음
print(f'intercept: {lin_reg.intercept_}, coefficients: {lin_reg.coef_}')

# 검증 세트를 사용해서 예측 -> 그래프
y_pred_rm = lin_reg.predict(X_test_rm)
# 실제값(scatter), 예측값(plot)
plt.scatter(X_test_rm, y_test)
plt.plot(X_test_rm, y_pred_rm, 'r-')
plt.show()

# MSE(Mean Squared Error: 오차 제곱들의 평균) 계산
# error = y - y_hat, error^2 = (y - y_hat)^2
# MSE = sum(error^2) / 개수
mse = mean_squared_error(y_test, y_pred_rm)
# RMSE(Squared-Root MSE)
rmse = np.sqrt(mse)
print('Price ~ RM: RMSE =', rmse)

# R2-score(결정 계수) 계산
r2_1 = lin_reg.score(X_test_rm, y_test)
r2_2 = r2_score(y_test, y_pred_rm)
print(f'Price ~ RM: R^2 = {r2_1}, {r2_2}')

# Price ~ LSTAT 선형 회귀: price = b0 + b1 * lstat
X_train_lstat = X_train[:, np.newaxis, 12]  # 학습 세트
X_test_lstat = X_test[:, np.newaxis, 12]  # 검증 세트

lin_reg.fit(X_train_lstat, y_train)  # 모델 fit, train
print(f'Price ~ LSTAT: intercept: {lin_reg.intercept_}, coefficients: {lin_reg.coef_}')

y_pred_lstat = lin_reg.predict(X_test_lstat)  # 예측, 테스트

plt.scatter(X_test_lstat, y_test)  # 실제값 산점도 그래프
plt.plot(X_test_lstat, y_pred_lstat, 'r')  # 예측값 선 그래프
plt.title('Price ~ LSTAT')
plt.xlabel('LSTAT')
plt.ylabel('Price')
plt.show()

mse = mean_squared_error(y_test, y_pred_lstat)
rmse = np.sqrt(mse)
r2 = lin_reg.score(X_test_lstat, y_test)
# r2_score(y_test, y_pred_lstat)
print(f'Price ~ LSTAT: RMSE = {rmse}, R^2 = {r2}')
print()

# Price ~ LSTAT + LSTAT^2 선형 회귀
# price = b0 + b1 * lstat + b2 * lstat^2
poly = PolynomialFeatures(degree = 2, include_bias = False)
# 데이터에 다항식 항들을 컬럼으로 추가해 주는 클래스 객체
# 학습 세트에 다항식 항을 추가 -> fit/train할 때 사용
X_train_lstat_poly = poly.fit_transform(X_train_lstat)
# 검증 세트에 다항식 항을 추가 -> predict/test할 때 사용
X_test_lstat_poly = poly.fit_transform(X_test_lstat)

lin_reg.fit(X_train_lstat_poly, y_train)
print(f'intercept: {lin_reg.intercept_}, coefficients: {lin_reg.coef_}')

y_pred_lstat_poly = lin_reg.predict(X_test_lstat_poly)  # predict/test

plt.scatter(X_test_lstat, y_test)
# plt.plot(X_test_lstat, y_pred_lstat_poly, 'r') # 예측값
xs = np.linspace(X_test_lstat.min(), X_test_lstat.max(), 100).reshape(100, 1)
xs_poly = poly.fit_transform(xs)
ys = lin_reg.predict(xs_poly)
plt.plot(xs, ys, 'r')

plt.title('Price ~ lstat + lstat^2')
plt.show()

mse = mean_squared_error(y_test, y_pred_lstat_poly)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_lstat_poly)
print(f'Price ~ LSTAT^2: RMSE = {rmse}, R^2 = {r2}')
print()


X_train_rm_lstat = X_train[:, [5, 12]]
X_test_rm_lstat = X_test[:, [5, 12]]

lin_reg.fit(X_train_rm_lstat, y_train)
print(f'intercept: {lin_reg.intercept_}, coefficients: {lin_reg.coef_}')

y_pred_rm_lstat = lin_reg.predict(X_test_rm_lstat)
print(y_test[:5], y_pred_rm_lstat[:5])

mse = mean_squared_error(y_test, y_pred_rm_lstat)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_rm_lstat)
print(f'Price ~ RM + LSTAT^2: RMSE = {rmse}, R^2 = {r2}')

print()
# Price ~ RM + LSTAT + RM^2 + RM * LSTAT + LSTAT2
# price = b0 + b1*rm + b2*lstat + b3*rm^2 + b4*rm* lstat + b5*lstat^2
X_train_rm_lstat_poly = poly.fit_transform(X_train_rm_lstat)
X_test_rm_lstat_poly = poly.fit_transform(X_test_rm_lstat)

lin_reg.fit(X_train_rm_lstat_poly, y_train)
y_pred_rm_lstat_2 = lin_reg.predict(X_test_rm_lstat_poly)
print(f'intercept : {lin_reg.intercept_}, coefficients :{lin_reg.coef_}')
mse = mean_squared_error(y_test, y_pred_rm_lstat_2)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_rm_lstat_2)
print(f'RM + LSTAT + RM^2 + RM * LSTAT + LSTAT2: RMSE = {rmse}, R^2 = {r2}')

print()
# Price ~ RM + LSTAT + LSTAT^2
# price = b0 + b1 * rm + b2 * lstat + b3 * lstat^2
X_train_x = np.c_[X_train_rm, X_train_lstat_poly]
X_test_x = np.c_[X_test_rm, X_test_lstat_poly]

lin_reg.fit(X_train_x, y_train)
y_pred_rm_lstat_x = lin_reg.predict(X_test_x)
print(f'intercept : {lin_reg.intercept_}, coefficients :{lin_reg.coef_}')
mse = mean_squared_error(y_test, y_pred_rm_lstat_x)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred_rm_lstat_x)
print(f'RM + RM + LSTAT + LSTAT^2: RMSE = {rmse}, R^2 = {r2}')