import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("./data/heart.csv")
# print(df.head(5))
# print(df.columns)
# print(df.shape)
# print(df.isnull().sum())

features = df[['trtbps', 'chol', 'restecg', 'thalachh']]
result = df[['output']]
train_x, test_x, train_y, test_y = train_test_split(features, result,  train_size=0.8, test_size=0.2)

scaler = StandardScaler()
train_features = scaler.fit_transform(train_x)
test_features = scaler.fit_transform(test_x)

model = LogisticRegression()
model.fit(train_features, train_y)

print(model.score(train_features, train_y))
print(model.score(test_features, test_y)) 
print(model.coef_)     

# 0.7107438016528925
# 0.6721311475409836
# [[-0.27381889 -0.15581091  0.17945084  1.06765183]]

Jack = np.array([61, 300, 2, 175])
Rose = np.array([70, 240, 0, 155])
Me = np.array([71, 160, 1, 170])

sample = np.array([Jack, Rose, Me])
sample = scaler.transform(sample)
print(model.predict(sample))
print(model.predict_proba(sample))

# [1 1 1]
# [[0.08893347 0.91106653]
#  [0.38613372 0.61386628]
#  [0.14388186 0.85611814]]