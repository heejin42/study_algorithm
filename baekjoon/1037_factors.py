# 모든 약수가 주어질 때, 값을 구하는 문제
import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().split(' ')))
print(min(arr)*max(arr))