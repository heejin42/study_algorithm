import sys
input = sys.stdin.readline
n, k = map(int, input().split(' '))
count = []
arr = list(map(int, input().split(' ')))

def merge_sort(arr):
    global count
    if len(arr) <= 1:
        return arr
    mid = (len(arr)+1)//2
    arr_1 = merge_sort(arr[:mid])
    arr_2 = merge_sort(arr[mid:])
    
    sorted_arr = []
    i, j = 0, 0
    while i < len(arr_1) and j < len(arr_2):
        if arr_1[i] > arr_2[j]:
            sorted_arr.append(arr_2[j])
            count.append(arr_2[j])
            j += 1
        else:
            sorted_arr.append(arr_1[i])
            count.append(arr_1[i])
            i += 1
    while i < len(arr_1):
        sorted_arr.append(arr_1[i])
        count.append(arr_1[i])
        i += 1
    while j < len(arr_2):
        sorted_arr.append(arr_2[j])
        count.append(arr_2[j])
        j += 1 
    return sorted_arr         


arr = merge_sort(arr)
if len(count) < k:
    print(-1)
else:
    print(count[k-1])