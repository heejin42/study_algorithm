import sys

N = int(input())
arr = []
for n in range(N):
    row = list(sys.stdin.readline().strip())
    arr.append(row)

def quad_tree(x, y, n):
    value = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != value:
                value = '-1'
                break
    
    if value == '-1':
        print('(', end = '')
        quad_tree(x, y, n//2)
        quad_tree(x, y+n//2, n//2)
        quad_tree(x+n//2, y, n//2)
        quad_tree(x+n//2, y+n//2, n//2)
        print(')', end = '')

    elif value == '0':
        print(0, end='')
    elif value == '1':
        print(1, end='')

quad_tree(0, 0, N)