import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

stock_prices = pd.read_csv("World-Stock-Prices-Dataset.csv")

# stock_prices["Dividends"] = stock_prices["Dividends"].astype(object)
# stock_prices["Stock Splits"] = stock_prices["Stock Splits"].astype(object)

# missing_df = stock_prices.isnull().sum().reset_index()
# missing_df.columns = ['column', 'count']
# missing_df['ratio'] = missing_df['count'] / stock_prices.shape[0]

# nexflix_stock = stock_prices[stock_prices['Brand_Name'] == "netflix"]
# nexflix_stock.to_csv("nexflix_stock.csv")
# nexflix_stock.head(10)
# stock_cor = nexflix_stock[["Open", "Close"]].corr()
# sns.heatmap(stock_cor)
# sns.distplot(nexflix_stock['Open'])
# plt.hist(nexflix_stock['Open'], bins=20)
# sns.displot(nexflix_stock['Open'], kde=True)
# sns.boxplot(stock_prices["Open"])
# plt.show()
# sns.lineplot(x='Open', y="Close", data=nexflix_stock)
# plt.show()

# df = pd.read_csv("nexflix_stock.csv")
# sns.scatterplot(x = 'High', y = 'Low', data=stock_prices, hue = "Industry_Tag")
# sns.regplot(x='High', y='Low', data=stock_prices, marker='+', ci=99)
# sns.countplot(y="Country", data=stock_prices)

# 범주형 단변수 - 파이그래프
# new = pd.DataFrame(stock_prices['Country'].value_counts()/stock_prices['Country'].count())
# new.reset_index(inplace=True)
# plt.pie(x=list(new['Country']),
#         labels = list(new['index']),
#         autopct = "%.2f%%")
# plt.show()

#stock_data = stock_prices[stock_prices.Industry_Tag.isin(["technology", "entertainment", "social media", "apparel", "fitness", "footwear", "food", "food & beverage"])]
# print(stock_data['Brand_Name'].unique())
# # sns.barplot(x = 'Industry_Tag', y = 'High', data=stock_data)
# # sns.pointplot(x='Industry_Tag', y = 'High', data=stock_data)
# # sns.boxplot(x='Industry_Tag', y='High', data=stock_data)
# food_stock = stock_prices[stock_prices.Industry_Tag.isin(["food", "food & beverage"])]
# sns.violinplot(x="Brand_Name", y="High", hue="Industry_Tag", data=food_stock)
# plt.show()


# subplots 실습

stock_data = stock_prices[stock_prices.Country.isin(["usa", "japan"])]
stock_data = stock_data[stock_data.Industry_Tag.isin(['gaming', 'automotive'])]

fig, axs = plt.subplots(2, 2, figsize=(8,8))
ax1, ax2, ax3, ax4 = axs.flatten()

ax1 = sns.boxplot(x='Industry_Tag', y='High', data=stock_data, ax=ax1)
ax2 = sns.barplot(x = 'Industry_Tag', y = 'High', data=stock_data, ax=ax2)
ax3 = sns.pointplot(x='Industry_Tag', y = 'High', data=stock_data, ax=ax3)
ax4 = sns.violinplot(x='Industry_Tag', y = 'High', hue="Country", data=stock_data, ax=ax4)

ax1.set_title("Stock price distribution by industry")
ax2.set_title("Average stock price by industry")
ax3.set_title("Average stock price by industry")
ax4.set_title("Stock price distribution by industry(usa,japan)")
# y축 이름 설정 추가
ax2.set_ylabel('average of High prices')
# y축 눈금 범위 변경
ax4.set_yticks(np.arange(0, 350, 50))
# 전체타이틀 & 그래프 사이 간격 조정
fig.suptitle("Stock prices data visualization")
fig.tight_layout()

plt.show()