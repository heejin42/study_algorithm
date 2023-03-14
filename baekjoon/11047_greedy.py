import sys

input = sys.stdin.readline
N, K = map(int, input().split(' '))
coins = []
for n in range(N):
    coins.append(int(input()))
count = 0
for c in range(len(coins), 0, -1):
    if K // coins[c-1] > 0:
        x = int(K // coins[c-1])
        K -= coins[c-1]*x
        count += x
    if K == 0:
        break

print(count)