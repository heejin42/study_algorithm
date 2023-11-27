# 이모티콘 플러스 가입자를 최대로, 이모티콘 판매액을 최대로 하는 경우의 가입자수와 판매액 구하기
# 각각의 이모티콘에 10%, 20% ,30% 40% 적용할 수 있음
# m개의 이모티콘, n명의 사용자, 각각의 기준 할인율과 가격이 존재
# 어떻게 풀어야 할까? 할인율 배정 모든 경우를 구해서 계산할까? 아마도?
# 중복 순열 -> 계산 -> 최대 기록
from itertools import product
def solution(users, emoticons):
    answer_plus_user = 0
    answer_sales = 0
    cases = list(product([10, 20, 30, 40], repeat=len(emoticons)))
    # case 마다 유저 확인
    for case in cases:
        emoticons_prices = []
        plus_user = 0
        sales = 0
        
        for i in range(len(emoticons)):
            emoticons_prices.append((100-case[i])*0.01*emoticons[i])
            
        for user in users:
            user_sales = 0
            plus_flag = 0
            for i in range(len(emoticons)):
                if case[i] >= user[0]:
                    user_sales += emoticons_prices[i]
                if user_sales >= user[1]:
                    plus_user += 1
                    plus_flag = 1
                    break
            if plus_flag == 0:
                sales += user_sales
                
        if answer_plus_user < plus_user:
            answer_plus_user = plus_user
            answer_sales = sales
        elif answer_plus_user == plus_user:
            answer_sales = max(answer_sales, sales)
        else:
            continue
    return [answer_plus_user, int(answer_sales)]
            
users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
print(solution(users, emoticons))