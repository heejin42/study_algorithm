# 문제 링크 - https://www.acmicpc.net/problem/17144
# 구조화
1. 먼지가 있는 좌표와 먼지 값을 알아야 한다.
2. 각 좌표에서 주위에 확산한 새로운 먼지 좌표를 만든다.
3. 공기청정기 중심으로 먼지 좌표를 업데이트 한다.

# 조건
1. 최대 50*50 크기 -> 250개 칸
2. T 최대 1000개
3. 최악의 경우, 250 * 1000

import sys
R, C, T = map(int, input().split(' '))
maps = []
machine = ()
for i in range(r):
    line = list(map(int, sys.stdin.readline().split(' ')))
    if -1 in line:
        machine.append(i)
        
for t in range(T):
    new_maps = [[0 for _ in range(c)] for _ in range(r)]
    for r in range(R):
        for c in range(C):
            dx = [0, -1, 0, 1]
            dy = [1, 0, -1, 0]
            if maps[r][c] > 0:
                for i in range(4):
                    if 0 <= r + dy[i] < R and 0 <=  c + dx[i] < C:
                        new_maps[r + dy[i]][c + dx[i]] += (maps[r][c]//5)
                        maps[r][c] -= (maps[r][c]//5)
                new_maps[r][c] += maps[r][c]
    maps = new_maps
                
                
            