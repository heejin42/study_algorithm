import sys
input = sys.stdin.readline

n1, m1 = map(int, input().split(' '))
a = []
b = []
for _ in range(n1):
    a.append(list(map(int, input().split(' '))))
n2, m2 = map(int, input().split(' ')) 
for _ in range(n2):
    b.append(list(map(int, input().split(' '))))
      
result = [[] for _ in range(n1)]   
for i in range(n1):
    for j in range(m2):
        sum = 0
        for k in range(len(a[i])):
            sum += a[i][k]*b[k][j]
        result[i].append(sum)
for arr in result:
    print(*arr)