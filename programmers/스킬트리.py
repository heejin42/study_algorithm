def solution(skill, skill_trees):
    answer = 0
    skill = list(skill)
    for tree in skill_trees:
        visited = [0 for _ in range(len(skill))]
        flag = 1
        for s in tree:
            if s in skill:
                i = skill.index(s)
                if i >= 1 and visited[i-1] == 0:
                    flag = 0
                    break
                else:
                    visited[i] =1
        if flag == 1:
            answer += 1
    return answer

skill = 'CBD'
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))
