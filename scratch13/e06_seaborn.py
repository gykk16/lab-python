import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston

boston = load_boston()
X = boston['data']
y = boston['target']
features = boston['feature_names']

boston_df = pd.DataFrame(X, columns = features)
boston_df['Price'] = y

print(boston_df.head())
print(boston_df.shape)
print(boston_df.describe())

columns = ['LSTAT', 'INDUS', 'NOX', 'RM', 'Price']
subset_df = boston_df[columns]
print(subset_df.head())

# sns.pairplot(subset_df)
# plt.show()

# sns.pairplot(boston_df)
# plt.show()


# 상관 행렬(correlation matrix): 상관 계수들로 만든 행렬

# DataFrame.corr(): 상관 계수들을 계산
corr_matrix = subset_df.corr().round(2)

# heatmap: 상관 계수(correlation coefficient)가 클수록 진한 색으로 표시됨.
sns.heatmap(corr_matrix, annot = True)
plt.show()

