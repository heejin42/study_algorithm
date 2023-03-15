import sys
input = sys.stdin.readline
N = int(input())
paper = [list(map(int, input().split(' ')))for _ in range(N)]

result_1 = 0
result_2 = 0
result_3 = 0

def check_paper(x,y,k):
    global result_1, result_2, result_3, paper
    flag = paper[x][y]
    for i in range(x, x+k):
        for j in range(y, y+k):
            if paper[i][j] != flag:
                k = k//3
                check_paper(x, y, k)
                check_paper(x+k, y, k)
                check_paper(x+(2*k), y, k)
                check_paper(x, y+k, k)
                check_paper(x+k, y+k, k)
                check_paper(x+(2*k), y+k, k)
                check_paper(x, y+(2*k), k)
                check_paper(x+k, y+(2*k), k)
                check_paper(x+(2*k), y+(2*k), k)
                return
    if flag == -1:
        
        result_1 += 1
    elif flag == 0:
        result_2 += 1
    elif flag == 1:
        result_3 += 1

check_paper(0, 0, N)
print(result_1)
print(result_2)
print(result_3)
