# 주사위가 n개 있을 때, a가 먼저 절반의 주사위를 고른다. 
# 각각의 주사위에는 다른 숫자들이 적혀있고 나올 확률은 동일하다.
# 굴려서 나온 수를 합산해서 더 큰 사람이 이긴다고 했을 때, 이길 확률이 가장 높게 선택하는 구성은?
# 2 <= n <= 10

from itertools import combinations
from itertools import product

def solution(dice):
    arr = [i for i in range(len(dice))]
    n = len(dice)//2
    case = list(combinations(arr, n))
    all_dict = {}
    for i in range(len(case)):
        sum_of_dict = {}
        all_case = list(product([0,1,2,3,4,5], repeat=n))
        for choosen in all_case:
            summ = 0
            for j in range(n):
                summ += dice[case[i][j]][choosen[j]]
            if summ in sum_of_dict:
                sum_of_dict[summ] += 1
            else:
                sum_of_dict[summ] = 1
        all_dict[i] = sum_of_dict
    max_wins = 0
    answer = []
    for i in range(len(case)):
        win_case = 0
        a = case[i]
        b = tuple([x for x in arr if x not in a])
        b_index = case.index(b)
        for a_k in all_dict[i]: 
            for b_k in all_dict[b_index]:
                if a_k > b_k:
                    win_case += all_dict[i][a_k]*all_dict[b_index][b_k]
        if max_wins < win_case:
            answer = case[i]
            max_wins = win_case
    answer = list(answer)
    for i in range(n):
        answer[i] += 1
    return answer

dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
print(solution(dice))
