import sys
 
n = int(sys.stdin.readline().strip())

found = ['1']
dic = {}
for i in range(0, n-1):
    x, y = sys.stdin.readline().strip().split()
    if x in found:
        dic[y] = x
        found.append(y)
    elif y in found:
        dic[x] = y
        found.append(x)

for i in range(2,n+1):
    print(dic[str(i)])