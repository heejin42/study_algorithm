import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

breast_cancer_data = load_breast_cancer()
df = pd.DataFrame(breast_cancer_data.data)
df_target = pd.DataFrame(breast_cancer_data.target)

print(df.head())
print(df_target.head())
print(df.describe())

train_data, test_data, train_labels, test_labels = train_test_split(df, df_target, test_size=0.2, random_state=100)

scaler = MinMaxScaler()
train_features = scaler.fit_transform(train_data)
test_features = scaler.fit_transform(test_data)


classifier = KNeighborsClassifier(n_neighbors = 3)
classifier.fit(train_data, train_labels)
print(classifier.score(test_data, test_labels))


k_list = range(1, 101)
accuracies = []

for k in k_list:
    classifier = KNeighborsClassifier(n_neighbors = k)
    classifier.fit(train_data, train_labels)
    accuracies.append(classifier.score(test_data, test_labels))
    
plt.plot(k_list, accuracies)
plt.xlabel = 'k'
plt.ylabel = 'Test Accuracy'
plt.title = 'Breast Cancer Classifier Accuracy'
plt.show()