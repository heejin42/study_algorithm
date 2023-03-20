import sys
input = sys.stdin.readline

N, C = map(int, input().split(' '))
internet = []
for n in range(N):
    internet.append(int(input()))
internet.sort()
start = 1
end = internet[-1]-internet[0]

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    flag = internet[0]
    for i in internet:
        if (i - flag) >= mid:
            cnt += 1
            flag = i
    if cnt >= C:
        start = mid + 1
    else:
        end = mid - 1
    
print(end)

