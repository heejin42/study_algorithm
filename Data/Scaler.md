# Scikit-learn의 Scaler 4가지
데이터 분석이나 머신러닝 모델을 학습할 때, 데이터의 각 컬럼마다 크기와 편차가 다르다면 한 피처의 특징을 너무 많이 반영하게 되는 문제가 발생할 수 있다. 그렇기 때문에 데이터 정제의 과정에서 그 크기와 편차를 맞춰주는 스케일링 작업이 필요하다. 여기서는 자주 사용하는 sklearn.preprocessing의 스케일러 4가지를 비교해보고 언제 어떤 스케일러를 사용하는 것이 좋은지 정리해보겠다.

## 1. Standard Scaler
- 기존 변수의 범위를 정규 분포로 바꾸는 스케일러로 모든 피처의 평균을 0, 분산을 1로 만든다.
- 데이터의 최소, 최대를 모를 때 사용하면 좋으나, 이상치가 평균과 표준편차에 영향을 주기 때문에 이상치가 많은 데이터에는 사용하지 않는 것이 좋다.
### code
```python
from sklearn.preprocessing import StandardScaler

std = StandardScaler()
std_data = std.fit_transform(data)
```

## 2. Normalizer
각 변수의 값을 모두 원점으로부터 1만큼 떨어져 있는 범위 내로 변환하는 스케일러로 열을 대상으로 하는 것이 아니라, 행마다 정규화가 된다. 한 행의 모든 피처들 사이의 유클리드 거리가 1이 되도록 하는 것이다. 데이터의 형태는 유지되나 규모가 작아지므로 빠르게 학습하고 과대적합 확률이 낮다는 장점이 있다. 데이터 분포의 형태를 살리고 규모를 작게 하고 싶은 경우에 사용하면 된다.
```python
from sklearn.preprocessing import Normalizer

nor = Normalizer()
nor_data = nor.fit_transform(data)
```


## 3. MinMaxScaler
- 각 데이터의 값들을 0과 1 사이의 값으로 변환시키는 스케일러
- 변수들이 정규분포를 띄지 않거나 표준 편차가 작을 때 효과적인 방법이고, 이상치에는 민감하다.
```python
from sklearn.preprocessing import MinMaxScaler

mm = MinMaxScaler()
mm_data = mm.fit_transform(data)
```
0과 1 사이가 아닌 -1~1 사이로 하는 스케일러는 MaxAbsScaler()를 사용하면 된다.

## 4. Robust Scaler
모든 피처들이 같은 크기를 갖게 한다는 점에서 standard와 유사하지만 평균과 분산이 아닌, 중위수와 사분위수를 사용한다는 차이가 있다. 평균과 분산을 사용하지 않기 때문에 이상치의 영향이 적다.
```python
from sklearn.preprocessing import RobustScaler

rob = RobustScaler()
rob_data = rob.fit_transform(data)
```



