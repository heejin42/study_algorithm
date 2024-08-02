# 일곱개의 합이 100인가 -> 전체의 합 - 100 이 되는 num을 찾자
from itertools import combinations
def solution(nine):
    over = sum(nine) - 100
    candidates = list(combinations(nine, 2))
    for candidate in candidates:
        if sum(candidate) == over:
            nine.remove(candidate[0])
            nine.remove(candidate[1])
            break
    print(*nine, sep='\n')
    

nine = []
for _ in range(9):
    nine.append(int(input()))
solution(nine)