n, m = map(int, input().split(' '))
array_n = []
for i in range(n):
    array_n.append(input())
array_n.sort()

array_m = []
for i in range(m):
    array_m.append(input())

def binary_search(target, array_m, start, end):
    while start<=end:
        mid = (start + end) // 2
        if array_m[mid] == target:
            return True
        elif array_m[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

count = 0
for str in array_m:
    if binary_search(str, array_m, 0, len(array_m)-1):
        count += 1
print(count)
    

