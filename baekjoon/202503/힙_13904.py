# https://www.acmicpc.net/problem/17144
# 하루에 한 과제를 끝낼 수 있고, 과제마다 마감일이 있음, 과제마다 점수가 있는데 가장 많은 점수를 받을 수 있도록 해보자
# Sol: 점수가 큰 걸 기준으로 해야할까? 마감일이 밭은 것 부터 해야할까?
# 경우에 따라 다를 수 있다, 0 < N < 1000 
# dfs


import sys
import heapq 
n = int(sys.stdin.readline())
heap = []
date = [0 for _ in range(1001)]
score = 0

for _ in range(n):
    d, w = map(int, sys.stdin.readline().split(' '))
    heap.append((-w, d))

heapq.heapify(heap)

while heap:
    w, d = heapq.heappop(heap)
    for i in range(d, 0, -1):
        if date[i] == 0:
            score -= w
            date[i] = 1
            break

print(score)
            

