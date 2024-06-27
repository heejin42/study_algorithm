import sys

def solution(n, fires):
    answer = 0
    fires.sort(reverse=True)
    for i in range(2, fires[0]+1):
        count = 0
        for fire in fires:
            if fire < i:
                break
            if fire%i == 0:
                count += 1
        answer = max(answer, count)
    return answer


n = int(sys.stdin.readline().strip())
fires = list(map(int, sys.stdin.readline().strip().split(' ')))
print(solution(n, fires))