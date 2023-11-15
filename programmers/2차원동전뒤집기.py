# 같은 줄에 있는 모든 동전을 뒤집어야 동전을 뒤집을 수 있다.
# beginning - > 초기 상태
# target -> 목표 상태
# 목표 상태를 만들기 위한 동전 뒤집기 횟수 최솟값, 만약 만들지 못하면 -1 return
# 최대 10x10
from itertools import combinations
import copy

def solution(beginning, target):
    def reverse(n):
        return 1-n
    n = len(beginning[0])
    m = len(beginning)
    total = [i for i in range(n+m)]
    for cnt in range(1, m+n+1):
        # total 중에서 cnt개 조합을 구해서 모두 뒤집기
        candidates = list(combinations(total, cnt))
        for candidate in candidates:
            tmp_coins = copy.deepcopy(beginning)
            for line in candidate:
                if line < m:
                    tmp_coins[line][:] = map(reverse, tmp_coins[line][:])
                else:
                    for i in range(m):
                        tmp_coins[i][line-m] = 1-tmp_coins[i][line-m]
                if tmp_coins == target:
                    return cnt
    return -1

beginning = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
target = [[1, 0, 1], [0, 0, 0], [0, 0, 0]]
print(solution(beginning, target))