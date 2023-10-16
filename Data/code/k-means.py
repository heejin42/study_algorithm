import pandas as pd
import numpy as np
from sklearn import datasets
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans

iris = datasets.load_iris()
data = pd.DataFrame(iris.data)
feature = pd.DataFrame(iris.feature_names)

data.columns= feature[0]
target = pd.DataFrame(iris.target)

target.columns = ['target']
df = pd.concat([data, target], axis=1)

# sns.pairplot(df, hue="target")
# plt.show()


# ks = range(1, 10)
# inertias = []

# for k in ks:
#     model = KMeans(n_clusters=k)
#     model.fit(df)
#     inertias.append(model.inertia_)    
    
# plt.figure(figsize=(4,4))
# plt.plot(ks, inertias, '-o')
# plt.xlabel('number of clusters, k')
# plt.ylabel('inertia')
# plt.xticks(ks)
# plt.show()

clust_model = KMeans(n_clusters = 3)
clust_model.fit(df)
centers = clust_model.cluster_centers_
pred = clust_model.predict(df)

print(pd.DataFrame(centers))
print(pred[:10])

clust_df = df.copy()
clust_df['clust'] = pred

plt.figure(figsize=(20, 6))

X = clust_df

plt.subplot(131)
sns.scatterplot(x=X.iloc[:,0], y=X.iloc[:,1], data=df, hue=clust_model.labels_, palette='coolwarm')
plt.scatter(centers[:,0], centers[:,1], c='black', alpha=0.8, s=150)

plt.subplot(132)
sns.scatterplot(x=X.iloc[:,0], y=X.iloc[:,2], data=df, hue=clust_model.labels_, palette='coolwarm')
plt.scatter(centers[:,0], centers[:,2], c='black', alpha=0.8, s=150)

plt.subplot(133)
sns.scatterplot(x=X.iloc[:,0], y=X.iloc[:,3], data=df, hue=clust_model.labels_, palette='coolwarm')
plt.scatter(centers[:,0], centers[:,3], c='black', alpha=0.8, s=150)

plt.show()

