# 3 이상 1만 이하의 지방에 국가 예산을 나눠줘야함.
# 각각의 지방에서 요청하는 금액은 다 다름
# 최대로 많이 줄 수 있는 경우는?
# 기준치 값을 정하자, 중앙으로 선택
# 앞까지의 합 + 중앙값*나머지개수 < budget


def solution(n, budgets, m):
    if sum(budgets) <= m:
        return budgets[-1]
    f = 0
    t = n-1 
    answer = 0
    while f < t:
        now = (f+t) // 2
        need = sum(budgets[:now+1]) + (t-now)*budgets[now]
        if need < m:
            f = now + 1
            check = now
        elif need > m:
            t = now - 1
            check = now-1
        else:
            answer = budgets[now]
            break
        
    if answer == 0:
        base = sum(budgets[:check+1])
        for x in range(budgets[check],budgets[check+1]):
            if x*(n-check-1) + base > m:
                break
        return x-1
    else:
        return answer
    
n = int(input())
budgets = list(map(int, input().split(' ')))
m = int(input())
budgets.sort()
print(solution(n, budgets, m))