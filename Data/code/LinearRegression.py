from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('./data/World-Stock-Prices-Dataset.csv')
# 분야에 따른 주식 값 예측