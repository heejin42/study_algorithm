import sys

N, M = map(int, sys.stdin.readline().split(' '))
arr = list(map(int, sys.stdin.readline().split(' ')))
p = [0]

for i in range(len(arr)):
    p.append(p[i] + arr[i])

for i in range(M):
    n, m = map(int, sys.stdin.readline().split(' '))
    print(p[m]-p[n-1])