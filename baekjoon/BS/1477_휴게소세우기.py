n, m, l = map(int, input().split(' '))
build = [0] + list(map(int, input().split(' '))) + [l]
build.sort()
left = 1  
right = l-1

while right > left:
    mid = (right+left) // 2
    count = 0
    for i in range(len(build)-1):
        if build[i+1] - build[i] > mid:
            count += (build[i+1] - build[i]-1) // mid
    if count <= m:
        right = mid - 1
    else:
        left = mid + 1
print(left)