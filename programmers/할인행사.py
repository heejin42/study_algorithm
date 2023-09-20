from collections import Counter
def solution(want, number, discount):
    # 매일 한가지 제품을 할인하고 할인 제품은 하나만 살 수 있다.
    # 원하는 제품과 수량이 10일 연속으로 일치할 경우 회원가입 하겠다.
    # 회원가입할 날짜의 총 일 수를 구하라.
    # discount 길이 100,000 
    answer = 0
    check = {}
    for w, n in zip(want, number):
        check[w] = n
        
    for i in range(len(discount)-9):
        c = Counter(discount[i:i+10])
        if c == check:
            answer += 1
    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))