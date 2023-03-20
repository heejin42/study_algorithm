import sys
input = sys.stdin.readline
K, N = map(int, input().split(' '))
line = []
for k in range(K):
    line.append(int(input()))
line.sort()

start = 1
end = line[-1]

while (start <= end):
    mid = (start + end) // 2
    cnt = 0
    for i in line:
        cnt += i // mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
