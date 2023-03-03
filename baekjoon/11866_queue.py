from collections import deque
n, k = map(int, input().split(' '))
queue = deque([x for x in range(1, n+1)])
remove = []

while queue:
    for i in range(k-1):
        x = queue.popleft()
        queue.append(x)
    x = queue.popleft()
    remove.append(x)
    
print('<'+", ".join(map(str, remove))+'>')

