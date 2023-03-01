n, m = map(int, input().split(' '))
arr = []

def dfs():
    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    for i in range(1, n+1):
        if len(arr) > 0 and i < arr[-1]:
            continue
        else:
            arr.append(i)
            dfs()
            arr.pop()

dfs()