def solution(square, n, m):
    for length in range(min(n,m), 0, -1):
        for i in range(0, n-length+1):
            for j in range(0, m-length+1):        
                if square[i][j] == square[i][j+length-1] == square[i+length-1][j] == square[i+length-1][j+length-1]:
                    return length*length

n, m = map(int, input().split(' '))
# 세로 n 가로 m
square = []
for _ in range(n):
    square.append(list(map(int, list(input()))))

print(solution(square, n, m))