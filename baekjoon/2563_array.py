n = int(input())
arr = [[0]*100 for _ in range(100)]
for i in range(n):
    x,y = map(int, input().split(' '))
    for row in range(y, y+10):
        for col in range(x, x+10):
            arr[row][col] = 1

result = 0
cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            result += 1

print(result)

    
