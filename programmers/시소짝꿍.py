from collections import Counter
def solution(weights):
    # 2,3,4m에 앉을 수 있음 1:1, 2:3, 1:2 3:4
    # weights이 주어질 때 시소 짝꿍을 구하여라
    # weights 의 길이 <= 100,000
    result = 0
    counter = Counter(weights)
    for k, v in counter.items():
        if v >= 2:
            result += v*(v-1)//2
    
    weights = set(weights)
    for w in weights:
        if w*2/3 in weights:
            result += counter[w*2/3] * counter[w]
        if w*2 in weights:
            result += counter[w*2] * counter[w]
        if w*3/4 in weights:
            result += counter[w*3/4] * counter[w]    
            
    return result

weights = [100,180,360,100,270]
print(solution(weights))
