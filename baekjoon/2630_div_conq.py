import sys
N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

count_white = 0
count_blue = 0

def check_square(x, y, n):
    global count_blue, count_white
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != color:
                check_square(x, y, n//2)
                check_square(x+n//2, y, n//2)
                check_square(x, y+n//2, n//2)
                check_square(x+n//2, y+n//2, n//2)
                return
    if color == 1:
        count_blue += 1
    else:
        count_white += 1


check_square(0, 0, N)
print(count_white)
print(count_blue)