# Python - Pandas 함수 정리
kaggle의 airlines.csv 데이터를 가지고 데이터 분석에 자주 사용되는 pandas의 함수 및 메서드를 정리해보겠다.
![URL](https://www.kaggle.com/datasets/jimschacko/airlines-dataset-to-predict-a-delay/)


## 1. 데이터 로드 및 이해
```python
import pandas as pd

# 데이터 로드
airlines = pd.read_csv('./data/Airlines.csv')

# 데이터 전체 모양 (행 개수, 열 개수) 확인
airlines.shape
# (539383, 9)

# 데이터 일부 확인
airlines.head(5)
#    id Airline  Flight AirportFrom AirportTo  DayOfWeek  Time  Length  Delay
# 0   1      CO     269         SFO       IAH          3    15     205      1
# 1   2      US    1558         PHX       CLT          3    15     222      1
# 2   3      AA    2400         LAX       DFW          3    20     165      1
# 3   4      AA    2466         SFO       DFW          3    20     195      1
# 4   5      AS     108         ANC       SEA          3    30     202      0

# 데이터 타입 확인
airlines.dtypes
# id              int64
# Airline        object
# Flight          int64
# AirportFrom    object
# AirportTo      object
# DayOfWeek       int64
# Time            int64
# Length          int64
# Delay           int64
# dtype: object

# 데이터 컬럼 리스트 확인
airlines.columns.tolist()
# ['id', 'Airline', 'Flight', 'AirportFrom', 'AirportTo', 'DayOfWeek', 'Time', 'Length', 'Delay']

# 데이터 전체 요약 통계 확인
airlines.describe()
#           id	            Flight	        DayOfWeek	    Time	        Length	        Delay
# count	    539383.00000	539383.000000	539383.000000	539383.000000	539383.000000	539383.000000
# mean	    269692.00000	2427.928630	    3.929668	    802.728963	    132.202007  	0.445442
# std	    155706.60446	2067.429837	    1.914664	    278.045911	    70.117016	    0.497015
# min	    1.00000         1.000000	    1.000000	    10.000000   	0.000000    	0.000000
# 25%	    134846.50000	712.000000	    2.000000	    565.000000	    81.000000	    0.000000
# 50%	    269692.00000	1809.000000	    4.000000	    795.000000  	115.000000	    0.000000
# 75%	    404537.50000	3745.000000	    5.000000	    1035.000000	    162.000000	    1.000000
# max	    539383.00000	7814.000000	    7.000000	    1439.000000	    655.000000	    1.000000

# 결측치 개수 확인
airlines.isna().sum()
# id             0
# Airline        0
# Flight         0
# AirportFrom    0
# AirportTo      0
# DayOfWeek      0
# Time           0
# Length         0
# Delay          0
# dtype: int64

# 특정 열 유니크 값 확인
airlines['Airline'].unique()
# array(['CO', 'US', 'AA', 'AS', 'DL', 'B6', 'HA', 'OO', '9E', 'OH', 'EV', 'XE', 'YV', 'UA', 'MQ', 'FL', 'F9', 'WN'], dtype=object)

# 특정 열의 값 개수 확인
airlines['Airline'].value_counts(ascending=True)
# HA     5578
# F9     6456
# AS    11471
# OH    12630
# YV    13725
# B6    18112
# 9E    20686
# FL    20827
# CO    21118
# UA    27619
# EV    27983
# XE    31126
# US    34500
# MQ    36605
# AA    45656
# OO    50254
# DL    60940
# WN    94097
# Name: Airline, dtype: int64
```

## 2. 열 또는 행 선택

## 3. 하나 이상의 열을 사용한 데이터 필터링

## 4. 데이터 정렬 및 열 삭제

## 5. 데이터 요약