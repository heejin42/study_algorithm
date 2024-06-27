# N명의 회원이 운동을 하고 각자 들 수 있는 역기의 무게가 w로 주어져있다.
# 회원님들 사이에 친분관계가 주어질 때, 친분 관계 속에서 가장 무거우면 최고라고 생각한다. 

def solution(n, weights, relationships):
    answer = 0
    for i in range(1, n+1):
        my_w = weights[i-1]
        best_flag = 1
        for r in relationships[i]:
            if weights[r-1] >= my_w:
                best_flag = 0
                break
        if best_flag:
            answer += 1
    return answer    


n, m = map(int, input().split(' '))
weights = list(map(int, input().split(' ')))
relationships = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split(' '))
    relationships[a].append(b)
    relationships[b].append(a)
print(solution(n, weights, relationships))