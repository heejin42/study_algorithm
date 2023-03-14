import sys
input = sys.stdin.readline
N = int(input())
times = list(map(int, input().split(' ')))
times.sort()

for n in range(1, N):
    times[n] = times[n-1] + times[n]

print(sum(times))
