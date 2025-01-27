from collections import deque
a, b = map(int, input().split(' '))
q = deque([(a, 0)])
answer = -2
while q:
    n, c = q.popleft()
    if n == b:
        answer = c
        break
    if n*2 <= b:
        q.append((n*2, c+1))
    if n*10 + 1 <= b:
        q.append((n*10+1, c+1))

print(answer+1)