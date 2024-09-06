def check(brige):
    global n
    global h
    for i in range(n):
        now = i
        for j in range(h):
            if brige[now][j] == 1:
                now += 1
            elif now > 0 and brige[now-1][j] == 1:
                now -= 1
        if now != i:
            return False
    return True
            
        
def dfs(cnt, x, y):
    global brige
    global answer
    global n
    global h
    if check(brige):
        answer = min(answer, cnt)
    elif cnt == 3 or cnt >= answer:
        return
    for i in range(x, h):
        if i == x:
            k = y
        else:
            k = 0
        for j in range(k, n-1):
            if (not brige[i][j] and not brige[i][j+1]):
                if j > 0 and brige[i][j-1]: continue
                brige[i][j] = 1
                dfs(cnt+i, i, j+2)
                brige[i][j] = 0


n, m, h = map(int, input().split(' '))

brige = [[0 for _ in range(h)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input())
    brige[b][a] = 1
answer = 4
dfs(0,0,0)
print(answer)