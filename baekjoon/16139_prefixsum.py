import sys

arr = list(sys.stdin.readline().strip())
p = [[0]*26]
p[0][ord(arr[0])-97] = 1
for i in range(1, len(arr)):
    p.append(p[-1][:])
    index = ord(arr[i]) - 97
    p[i][index] += 1


n = int(sys.stdin.readline())
for i in range(n):
    x, start, end = map(str, sys.stdin.readline().strip().split(' '))
    if start == '0':
        print(p[int(end)][ord(x)-97])
    else:
        print(p[int(end)][ord(x)-97] - p[int(start)-1][ord(x)-97])