# 5 3 4 2 1
# 1 2 4 3 6 5
# 1 2 4 5
# 1 2 3 6
# 1 2 3 5
# 가장 긴 증가하는 수열
# 가장 긴 감소하는 수열
import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

def binary_search(arr, tgt):
    left, right = 0, len(arr)-1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > tgt:
            left = mid + 1
        else:
            right = mid
    return right

lis_arr = [0]
for num in n_list:
    if lis_arr[-1] < num:
        lis_arr.append(num)
    else:
        idx = binary_search(lis_arr, num)
        lis_arr[idx] = num
        
print(len(n_list)-len(lis_arr)+1)    