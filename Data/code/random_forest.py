import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score, roc_auc_score, confusion_matrix

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species']= iris.target
df['species']= [1 if i == 1 else 0 for i in df['species']]
print(df)
train, test  = train_test_split(df, test_size  = 0.2, random_state = 2)
feature = df.drop(columns = 'species').columns
x_train = train[feature]
y_train = train['species']
x_test = test[feature]
y_test = test['species']

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


# [test] accuracy: 0.9333333333333333
# [test] f1: 0.875
# [test] auc: 0.9147727272727273

# [test] accuracy: 0.9666666666666667
# [test] f1: 0.9333333333333333
# [test] auc: 0.9744318181818181

#  oob_score: 0.9583333333333334