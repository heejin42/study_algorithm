# 맵이 주어졌을 떄, 상대 팀 진영에 가장 빨리 도착하는 경로의 칸이 개수를 구하라
# 최단거리는 bfs -> queue
from collections import deque
def solution(maps):
    n = len(maps)-1
    m = len(maps[0])-1
    queue = deque([[0,0,1]])
    while queue:
        now_n, now_m, distance = queue.popleft()
        if now_n == n and now_m == m:
            return distance
        else:
            dn = [0,0,1,-1]
            dm = [1,-1,0,0]
            for i in range(4):
                next_n = now_n + dn[i]
                next_m = now_m + dm[i]
                if 0<=next_n<=n and 0<=next_m<=m and maps[next_n][next_m] == 1:
                    queue.append([next_n, next_m, distance+1])
                    maps[next_n][next_m] = 0
    return -1

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))
