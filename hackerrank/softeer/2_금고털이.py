# 배낭의 무게 w만큼 귀금속을 담을 수 있다.
# n개의 종류의 귀금속의 무게와 가격이 주어진다.
# 가방에 담을 수 있는 최대 값어치의 귀금속은?

def solution(w, jewelry):
    jewelry.sort(key = lambda x:x[1])
    answer = 0
    while w > 0:
        weight, price = jewelry.pop()
        if w > weight:
            answer += weight*price
            w -= weight
        else:
            answer += w*price
            w = 0
    return answer 


w, n = map(int, input().split(' '))
jewelry = []
for _ in range(n):
    jewelry.append(list(map(int, input().split(' '))))
    
print(solution(w, jewelry))
