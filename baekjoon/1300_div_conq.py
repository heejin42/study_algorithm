import sys
input = sys.stdin.readline

def solve():
    global n, k
    result = 0
    start = 1
    end = n**2

    while start <= end:
        mid = (start + end) // 2
        temp = 0
        for i in range(1, n+1):
            temp += min(mid//i, n)

        if temp >= k:
            result = mid
            end = mid - 1
        elif temp < k:
            start = mid + 1

    print(result)

n = int(input())
k = int(input())
solve()


