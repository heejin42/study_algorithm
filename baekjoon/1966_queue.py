import sys
from collections import deque 

input = sys.stdin.readline
N = int(input())
for i in range(N):
    n, m = map(int, input().split(' '))
    printer = list(map(int, input().split(' ')))
    q = deque(printer)
    count = 0
    index = deque([i for i in range(n)])
    while q:
        doc = q[0]
        if doc == max(q):
            count += 1
            if index[0] == m:
                print(count)
                break
            else:
                q.popleft()
                index.popleft()
        else:
            q.append(q.popleft())
            index.append(index.popleft())
