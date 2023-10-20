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

# 특정 칼럼 값 별 개수 확인
df['Brand_Name'].value_counts()

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

# 결측치 제거
airlines  = airlines.dropna()

# 결측치 채우기
df.fillna(0)
# 결측값을 앞 방향 혹은 뒷 방향으로 채우기, limit(회수제한옵션)
df.fillna(method='ffill', limit=number)
df.fillna(method='bfill')
# 결측값을 변수별 평균으로 대체하기
df.fillna(df.mean())


# 중복 데이터 삭제
airlines = airlines.drop_duplicates()

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
```python
# 일부 행 선택
airlines[['id', 'Airline', 'Flight']]

# 일부 열 선택
airlines.iloc[10:20]

# 일부 열과 행 선택
airlines.loc[:10, ['id', 'Airline', 'Flight']]
```

## 3. 하나 이상의 열을 사용한 데이터 필터링
```python
# 하나의 열 필터링
airlines[airlines['Airline']=='US']
airlines[airlines['Airline'].isin(['US','UA','DL'])]
airlineList = ['US','UA','DL']
airlines[airlines['Airline'].isin(airlineList)]
airlines[~airlines['Airline'].isin(airlineList)]

# 두개 이상의 열 AND 조건 필터링
airlines[(airlines['Airline']=='US') & (airlines['AirportFrom']=='BOS') & (airlines['AirportTo']=='CLT')]

# 두개 이상의 열 OR 조건 필터링
airlines[(airlines['Airline']=='US') | (airlines['AirportFrom']=='BOS')]
```

## 4. 데이터 정렬 및 열 삭제
```python
# 특정 열 기준 오름차순 정렬
airlines.sort_values(by='DayOfWeek', ascending=True)

# 열 이름 변경
airlines.rename(columns={'Airline':'Airline_code', 'AirportFrom':'Airport_from', 'AirportTo':'Airport_to'})

# 열 추가
airlines['Country'] = 'USA'

# 조건부 열 추가
airlines['CO_SFO'] = (airlines['Airline']=='CO')&(airlines['AirportFrom']=='SFO')

# 	id  Airline Flight	AirportFrom	AirportTo	DayOfWeek	Time	Length	Delay	Country	CO_SFO
# 0	1	CO	    269	    SFO	        IAH	        3	        15	    205	    1	    USA	    True
# 1	2	US	    1558	PHX	        CLT	        3	        15	    222	    1	    USA	    False
# 2	3	AA	    2400	LAX	        DFW     	3	        20  	165 	1   	USA 	False
# 3	4	AA	    2466	SFO     	DFW 	    3	        20	    195	    1	    USA	    False
# 4	5	AS	    108	    ANC 	    SEA     	3       	30  	202 	0	    USA 	False

# 열 삭제
airlines.drop(['CO_SFO'], axis=1)

# 행 추가
new_data = {'id':600000, 'Airline':'KA', 'Flight':'1234', 'AirportFrom':'ICH', 'AirportTo':'PHX', 'DayOfWeek':2, 'Time':480, 'Length':500, 'Delay':1, 'Country':'USA'}
airlines.append(new_data, ignore_index=True)

# 특정 값을 가진 행 삭제
idx_co = airlines[airlines['Airline']=='CO'].index
airlines.drop(idx_co)

```

## 5. 데이터 요약
```python
# groupby를 사용한 데이터 요약
airlines.groupby(['Airline', 'AirportFrom', 'AirportTo'], as_index=False)['id'].agg('count')

df.groupby('Country')['High'].mean()
df.groupby(['Country', 'Industry_Tag'])['High'].describe()

# 여러 값에 대한 요약
airlines.groupby(['Airline', 'AirportFrom', 'AirportTo'])['Time'].agg(['sum', 'count']).reset_index()

# 집계와 함께 pivot_table을 사용하여 요약
airlines.pivot_table(index=['Airline','AirportFrom','AirportTo'], values=['Time'], aggfunc=['sum', 'count']).reset_index(col_level=1)
```

## 6. 함수 적용
```python
def level(x):
    if x > brand_df['High'].describe()['75%']:
        return 1
    elif x <=  brand_df['High'].describe()['75%'] and x > brand_df['High'].describe()['50%']:
        return 2
    elif x <=  brand_df['High'].describe()['50%'] and x >  brand_df['High'].describe()['25%']:
        return 3
    else:
        return 4
    
brand_df['level'] = brand_df['High'].apply(lambda x: level(x))
```

## 7. 합치기
```python
new_df = df.merge(brand_df, on='Brand_Name', how='left')
```

## 8. 비율 확인하기
```python
ratio_df = pd.DataFrame(df['Country'].value_counts()/df['Country'].count())
ratio_df.reset_index(inplace=True)
ratio_df
```