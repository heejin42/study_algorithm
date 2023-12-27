from itertools import combinations
def solution(l, c, candidates):
    result = []
    words = list(combinations(candidates,l))
    # 모음 1개 이상, 자음 2개 이상인지 확인
    for word in words:
        count = 0
        for i in ['a', 'e', 'i', 'o', 'u']:
            if i in word:
                count += 1
        if count >= 1 and l-count >= 2:
            word = list(word)
            word.sort()
            result.append(''.join(word))
    result.sort()
    print(*result, sep='\n')
    return 
    
l, c = map(int, input().split(' '))
candidates = list(input().split(' '))
solution(l,c,candidates)
