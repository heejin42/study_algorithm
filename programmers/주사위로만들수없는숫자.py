from itertools import product, permutations
def solution(dice):
    answer = ''
    count = len(dice)
    dices = [i for i in range(count)]
    # 0~9 사이의 숫자가 씌여진 정육면체 주사위 1개~4개
    # 만들 수 없는 가장 작은 숫자 구하기
    candidates = [i for i in range(int('9'*count)+1)]
    for i in range(1, count+1):
        if i == 1: 
            for d in dice:
                for num in d:
                    if num in candidates:
                        candidates.remove(num)
        elif i == 2: 
            cases = list(permutations(dices, 2))
            for x1, x2 in cases:
                for x in list(product(dice[x1], dice[x2])):
                    num = int(''.join(str(e) for e in list(x)))
                    if num in candidates:
                        candidates.remove(num)
        elif i == 3:
            cases = list(permutations(dices, 3))
            for x1, x2, x3 in cases:
                for x in list(product(dice[x1], dice[x2], dice[x3])):
                    num = int(''.join(str(e) for e in list(x)))
                    if num in candidates:
                        candidates.remove(num)
        elif i == 4:
            cases = list(permutations(dices, 4))
            for x1, x2, x3, x4 in cases:
                for x in list(product(dice[x1], dice[x2], dice[x3], dice[x4])):
                    num = int(''.join(str(e) for e in list(x)))
                    if num in candidates:
                        candidates.remove(num)
    candidates.sort()
    return candidates[0]    
    

dice = [[0,1,5,3,9,2], [2,1,0,4,8,7], [6,3,4,7,6,5]]
print(solution(dice))