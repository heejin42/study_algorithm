
def dfs(depth, idx, out):
    if depth == 6:
        print(*out)
        return
    for i in range(idx, k):
        out.append(s[i])
        dfs(depth+1, i+1, out)
        out.pop()
 

while True:
    x = list(map(int, input().split(' ')))
    if len(x) == 1: break
    k = x[0]
    s = x[1:]
    out = []
    dfs(0, 0, out)
    print()