import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split(' '))
q = deque([i for i in range(1, n+1)])
numbers = list(map(int, input().split(' ')))
index = 0
count = 0
for target in numbers:
    if q[0] == target:
        q.popleft()
    else:
        if list(q).index(target) < len(q)/2:
            while q[0] != target:
                q.append(q.popleft())
                count += 1
            q.popleft()    
        else:
            while q[0] != target:
                q.appendleft(q.pop())
                count += 1
            q.popleft()    

print(count)

