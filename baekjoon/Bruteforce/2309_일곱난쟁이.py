# 아홉 난쟁이 중에 일곱 난쟁이를 찾아라. 합은 100
# 일곱 난쟁이 키를 오름차순으로 출력할 것
from itertools import combinations

heights = []
for _ in range(9):
    heights.append(int(input()))
answer = []
for candidate in combinations(heights, 7):
    if sum(candidate) == 100:
        answer = list(candidate)
        break
    
answer.sort()
for i in answer:
    print(i)