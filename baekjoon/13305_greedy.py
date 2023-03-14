import sys

input = sys.stdin.readline
N = int(input())
distance = list(map(int, input().split(' ')))
price = list(map(int, input().split(' ')))
prices = []
for p in range(len(price)):
    prices.append([p, price[p]])

prices.sort(key = lambda x:(x[1], x[0]))
tmp = N-1
result = 0
for price in prices:
    if tmp > price[0]:
        result += price[1] * sum(distance[price[0]:tmp])
        tmp = price[0]
        
print(result)
