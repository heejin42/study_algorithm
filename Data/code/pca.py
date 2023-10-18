import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
data = load_iris()

iris_df = pd.DataFrame(
    data['data'],
    columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])

# print(iris_df.head(10))
# print(iris_df.corr())

# pca = PCA(random_state=1004)
# pca.fit_transform(iris_df)

# print(pca.explained_variance_ratio_)

# plt.rcParams['figure.figsize'] = (7, 7)
# plt.plot(range(1, iris_df.shape[1]+1), pca.explained_variance_ratio_)
# plt.xlabel("number of Principal Components", fontsize=12)
# plt.ylabel("% of Variance Explained", fontsize=12)
# plt.show()

pca = PCA(n_components=2, random_state=1004)
iris_pca = pca.fit_transform(iris_df)
print(iris_pca[:10])

## Visualization
species_map_dict = {
    0: 'setosa', 
    1: 'versicolor', 
    2: 'virginica'
}
iris_pca_df = pd.DataFrame({
    'pc_1' : iris_pca[:, 0],
    'pc_2' : iris_pca[:, 1],
    'species' : np.vectorize(species_map_dict.get)(data['target'])
})

print(iris_pca_df.head(5))

plt.figure(figsize = (7, 7))
sns.scatterplot(
    x = 'pc_1', 
    y = 'pc_2',
    hue = 'species',
    style = 'species',
    s = 100,
    data = iris_pca_df
)

plt.title('PCA result of IRIS dataset')
plt.xlabel("Principal Component 1", fontsize=14)
plt.ylabel("Principal Component 2", fontsize=14)
plt.show()