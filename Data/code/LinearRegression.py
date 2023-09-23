from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('./data/data.csv')
# 집 값 예측
x = df[['bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront','view','condition']]
y = df['price']
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)

# fig, axs = plt.subplots(2, 2, figsize=(8,8))
# ax1, ax2, ax3, ax4 = axs.flatten()
# ax1 = sns.lineplot(x = 'floors', y = 'price', data = df, ax = ax1)
# ax2 = sns.lineplot(x = 'bedrooms', y = 'price', data = df, ax = ax2)
# ax3 = sns.lineplot(x = 'bathrooms', y = 'price', data = df, ax = ax3)
# ax4 = sns.lineplot(x = 'condition', y = 'price', data = df, ax = ax4)
# plt.show()

model = LinearRegression()
model.fit(x_train, y_train)
my_house = [[3, 2, 960, 4000, 5, 0, 2, 4]]
my_predict = model.predict(my_house)
print(my_predict)
y_predict = model.predict(x_test)
plt.scatter(y_test, y_predict, alpha=0.4)
plt.xlabel("Actual Price")
plt.ylabel("Prediction")
plt.show()
print(model.coef_)
print(model.score(x_train, y_train))

