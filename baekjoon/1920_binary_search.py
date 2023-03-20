import sys
input = sys.stdin.readline
N = int(input())
nums = set(map(int, input().split(' ')))
M = int(input())
arr = list(map(int, input().split(' ')))

for target in arr:
    if target in nums:
        print(1)
    else:
        print(0)
