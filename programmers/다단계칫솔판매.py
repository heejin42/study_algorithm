def solution(enroll, referral, seller, amount):
    answer = []
    dic = {}
    profit_dic = {}
    for en, re in zip(enroll, referral):
        profit_dic[en] = 0
        if re == "-":
            dic[en] = "center"
        else:
            dic[en] = re
    profit_dic["center"] = 0
    
    for i in range(len(seller)):
        sel = seller[i]
        profit = amount[i]*100
        profit_dic[sel] += (profit - int(0.1*profit))
        profit = int(0.1*profit)
        sel = dic[sel]
        
        while True:
            if profit < 10 or sel not in dic:
                profit_dic[sel] += profit
                break
            else:
                profit_dic[sel] += (profit - int(0.1*profit))
                profit = int(0.1*profit)
                sel = dic[sel]
    for name in enroll :
        answer.append(int(profit_dic[name]))
        
    return answer


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]
print(solution(enroll, referral, seller, amount))