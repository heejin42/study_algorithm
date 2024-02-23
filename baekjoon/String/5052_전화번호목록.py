import sys
input = sys.stdin.readline

def solution(n, numbers):
    numbers.sort()
    for i in range(n-1):
        if numbers[i+1].startswith(numbers[i]):
            return 'NO'
    return 'YES'

T = int(input())
for _ in range(T):
    n = int(input())
    numbers = []
    for _ in range(n):
        numbers.append(input().strip())
    print(solution(n, numbers))
        
    