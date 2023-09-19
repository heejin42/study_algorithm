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
#nexflix_stock.head(10)
# stock_cor = nexflix_stock[["Open", "Close"]].corr()
# sns.heatmap(stock_cor)
# sns.distplot(nexflix_stock['Open'])
# plt.hist(nexflix_stock['Open'], bins=20)
# sns.displot(nexflix_stock['Open'], kde=True)
#sns.boxplot(stock_prices["Open"])
#plt.show()
# sns.lineplot(x='Open', y="Close", data=nexflix_stock)
# plt.show()

# df = pd.read_csv("nexflix_stock.csv")
# sns.scatterplot(x = 'High', y = 'Low', data=stock_prices, hue = "Industry_Tag")
# sns.regplot(x='High', y='Low', data=stock_prices, marker='+', ci=99)
# sns.countplot(y="Country", data=stock_prices)
new = pd.DataFrame(stock_prices['Country'].value_counts()/stock_prices['Country'].count())
new.reset_index(inplace=True)
plt.pie(x=list(new['Country']),
        labels = list(new['index']),
        autopct = "%.2f%%")
plt.show()