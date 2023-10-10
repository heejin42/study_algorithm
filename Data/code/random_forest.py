import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score, roc_auc_score, confusion_matrix

df = sns.load_dataset('iris')
target = 'species'
df['species']= [1 if i == 'versicolor' else 0 for i in df['species']]


train, test  = train_test_split(df, test_size  = 0.2, random_state = 2)
feature = df.drop(columns = target).columns
X_train = train[feature]
y_train = train[target]
X_test = test[feature]
y_test = test[target]


x_train,x_test,y_train,y_test = train_test_split(x_data,y_data,test_size=0.3)


# --------------------------------------------
decit = DecisionTreeClassifier()
decit.fit(x_train, y_train)
y_pred_train = decit.predict(x_test)
y_pred_proba_train = decit.predict_proba(x_train)[:,1]
y_pred = decit.predict(x_test)
y_pred_proba = decit.predict_proba(x_test)[:,1]

print('\n[test] accuracy:',decit.score(x_test, y_test))
print('[test] f1:', f1_score(y_test, y_pred))
print('[test] auc:', roc_auc_score(y_test, y_pred_proba))

# -----------------------------------
rf = RandomForestClassifier(oob_score=True)
rf.fit(x_train, y_train)

y_pred = rf.predict(x_test)
y_pred_proba = rf.predict_proba(x_test)[:,1]

print('\n[test] accuracy:',rf.score(x_test, y_test))
print('[test] f1:', f1_score(y_test, y_pred))
print('[test] auc:', roc_auc_score(y_test, y_pred_proba))

print('\n oob_score:',rf.oob_score_)