from collections import deque
import sys
input = sys.stdin.readline

def solve(boxes):
    global n, m, h
    arr = []
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if boxes[i][j][k] == 1:
                    arr.append((i, j, k))
    queue = deque(arr)
    di = [0, 0, 1, -1, 0, 0]
    dj = [1, -1, 0, 0, 0, 0]
    dk = [0, 0, 0, 0, 1, -1]

    while queue:
        i, j, k = queue.popleft()
        for x in range(6):
            new_i = i + di[x]
            new_j = j + dj[x]
            new_k = k + dk[x]
            if 0 <= new_i < h and 0 <= new_j < n and 0 <= new_k < m:
                if boxes[new_i][new_j][new_k] == 0:
                    boxes[new_i][new_j][new_k] = boxes[i][j][k] + 1
                    queue.append((new_i, new_j, new_k))
    count_day = 1
    for box in boxes:
        for line in box:
            if 0 in line:
                return(-1)
            else:
                count_day = max(max(line), count_day)
    return count_day-1

m, n, h = map(int, input().split(' '))
boxes = []
for _ in range(h):
    line = []
    for _ in range(n):
        line.append(list(map(int, input().split(' '))))
    boxes.append(line)

print(solve(boxes))