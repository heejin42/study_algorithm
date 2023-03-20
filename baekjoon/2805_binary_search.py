import sys
input = sys.stdin.readline

N, M = map(int, input().split( ))
trees = list(map(int, input().split(' ')))

start = 0
end = max(trees)

while (start <= end):
    mid = (start + end) // 2
    length = 0
    for tree in trees:
        if (tree - mid) > 0:
            length += (tree-mid)

    if length >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)

