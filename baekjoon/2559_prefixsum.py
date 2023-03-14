import sys
n, k = map(int, sys.stdin.readline().split(' '))
arr = list(map(int, sys.stdin.readline().split(' ')))
p = [0]
for i in range(len(arr)):
    p.append(p[i] + arr[i])
new_p = []   
for i in range(k, len(arr)+1):
    new_p.append(p[i] - p[i-k])

print(max(new_p))