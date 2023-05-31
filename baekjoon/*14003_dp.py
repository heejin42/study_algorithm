import sys
input = sys.stdin.readline

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] > target:
            end = mid
        elif arr[mid] <= target:
            start = mid + 1
    return end
    
def solve():
    global n, arr, binary_search
    total_len = [1 for _ in range(n)]
    total_arr = [arr[0]]
    for i in range(1, n):
        if arr[i] > total_arr[-1]:
            total_arr.append(arr[i])
            total_len[i] = len(total_arr) 
        else:
            total_len[i] = binary_search(total_arr, arr[i])
    print(max(total_len))
    print(*total_arr)        
                 

n = int(input())
arr = list(map(int, input().split(' ')))
solve()

