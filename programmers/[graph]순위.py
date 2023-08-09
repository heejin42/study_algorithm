from collections import defaultdict
def solution(n, results):
    # 정확하게 순위를 매길 수 있는 선수의 수를 구하라, 선수는 1명 이상, 100명 이하
    # result = [A, B] A가 B를 이겼다는 뜻
    # 그럼 i번째 선수가 이긴 선수들 + 진 선수들 합쳐서 n-1이면 순위를 알 수 있다.
    # 여기서 진 선수들, 이긴 선수들을 모두 추가하자.
    answer = 0
    win = defaultdict(set)
    lose = defaultdict(set)
    
    for winner,loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)
        
    for i in range(1, n+1):
        for loser in win[i]:
            # i에게 진 애들은 i가 진 애들에게도 진다.
            lose[loser].update(lose[i])
        for winner in lose[i]:
            # i 에게 이긴 애들은 i가 이긴 애들한테도 이긴다.
            win[winner].update(win[i])    
    for i in range(1, n+1):
        if len(lose[i]) + len(win[i]) == n-1:
            answer += 1
        
    return answer

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))