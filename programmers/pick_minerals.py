import sys
input = sys.stdin.readline

def solution(picks, minerals):
    targets = []
    answer = 0
    cnt = sum(picks)
    for i in range(0, len(minerals), 5):
        tired = 0
        for mineral in minerals[i:i+5]:
            if mineral == 'diamond':
                tired += 25
            elif mineral == 'iron':
                tired += 5
            elif mineral == 'stone':
                  tired += 1
        targets.append([tired, i])
        cnt -= 1
        if cnt == 0:
            break
    targets.sort(reverse = True)
    for target in targets:
        start = target[1]
        if picks[0] > 0:
            for mineral in minerals[start:start+5]:
                    answer += 1
            picks[0] -= 1
            pass
        elif picks[1] > 0:
            for mineral in minerals[start:start+5]:
                if mineral == 'diamond':
                    answer += 5
                else:
                    answer += 1
            picks[1] -= 1
        elif picks[2] > 0:
            for mineral in minerals[start:start+5]:
                if mineral == 'diamond':
                    answer += 25
                elif mineral == 'iron':
                    answer += 5
                elif mineral == 'stone':
                    answer += 1
            picks[2] -= 1
    return answer

picks = [0, 1, 1]
minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
print(solution(picks, minerals))