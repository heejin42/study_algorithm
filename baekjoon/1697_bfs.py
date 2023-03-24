from collections import deque
import sys
input = sys.stdin.readline

def bfs(n, k):
    arr = [0] * 100001
    queue = deque([n])
    while queue:
        x = queue.popleft()
        if x == k:
            return arr[x]
        for cx in (x-1, x+1, 2*x):
            if 0 <= cx <= 100000 and arr[cx] == 0:
                arr[cx] = arr[x] + 1 
                queue.append(cx)

n, k = map(int, input().split(' '))
print(bfs(n, k))