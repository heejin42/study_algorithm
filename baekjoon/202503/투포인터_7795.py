# https://www.acmicpc.net/problem/7795
import sys

def solution(a, b, arr_a, arr_b):
    cnt = 0
    if arr_b[-1] < arr_a[0]:
        cnt += (a*b)
        return cnt
    
    for i in range(b):
        if arr_b[i] >= arr_a[0]:
            pointer_b = i
            cnt += i
            break
        
    pointer_a = 1
    while pointer_a < a:
        if pointer_b == b:
            cnt += ((a-pointer_a) * b)
            break
        else:    
            if arr_a[pointer_a] <= arr_b[pointer_b]:
                cnt += pointer_b
                pointer_a += 1
            else:
                pointer_b += 1
    return cnt
    

T = int(sys.stdin.readline())
for t in range(T):
    a, b = map(int, sys.stdin.readline().split(' '))
    arr_a = list(map(int, sys.stdin.readline().split(' ')))
    arr_b = list(map(int, sys.stdin.readline().split(' ')))
    arr_a.sort()
    arr_b.sort()
    print(solution(a, b, arr_a, arr_b))