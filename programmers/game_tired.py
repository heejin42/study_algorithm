import itertools
def solution(k, dungeons):
    answer = 0
    candidates = itertools.permutations(dungeons, len(dungeons))
    for candidate in candidates:
        tired = k
        cnt = 0
        for dungeon in candidate:
            if dungeon[0] <= tired:
                tired -= dungeon[1]
                cnt += 1
            else:
                break
        answer = max(answer, cnt)
    return answer

k = 80	
dungeons = [[80,20],[50,40],[30,10]]
print(solution(k, dungeons))