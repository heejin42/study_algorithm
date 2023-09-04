from collections import Counter
def solution(topping):
    answer = 0
    # 공평하게 자르는 방법의 수 구하기
    # 공평학다는 것은? 토핑의 가짓수!]
    # 시간제한을 통과하려면?
    topping_a = {}
    topping_b = Counter(topping)
    for i in range(len(topping)):
        target = topping[i]
        if target in topping_a:
            topping_a[target] += 1
        else:
            topping_a[target] = 1
        topping_b[target] -= 1
        if topping_b[target] == 0:
            del topping_b[target]
        
        if len(topping_a) == len(topping_b):
            answer += 1
    return answer 

topping = [1,2,1,3,1,4,1,2]
print(solution(topping))