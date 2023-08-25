def solution(scores):
    # len(scores) <= 100,000
    answer = 0
    target_a, target_b = scores[0]
    target_score = target_a + target_b
    scores.sort(key = lambda x:(-x[0], x[1]))
    max_b = 0
    for a,b in scores:
        if a > target_a and b > target_b:
            return -1
        if b >= max_b:
            max_b = b
            if a + b > target_score:
               answer += 1
    return answer + 1

scores = [[2,2],[1,4],[3,2],[3,2],[2,1]]
print(solution(scores))
    