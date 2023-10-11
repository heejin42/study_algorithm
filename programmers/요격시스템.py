def solution(targets):
    answer = 1
    targets.sort(key = lambda x:x[1])
    l = targets[0][0] 
    r = targets[0][1]
    for target in targets:
        if target[0] <= l:
            continue
        elif l < target[0] < r:
            l = target[0] 
            continue
        else:
            answer += 1
            l = target[0]
            r = target[1]    
    return answer

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))
