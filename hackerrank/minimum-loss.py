def minimumLoss(price):
    # Write your code here
    # 집을 사고 다시 팔 때, 손해를 보는 경우 중 가장 적은 손해를 구하라
    # 각 차이의 양수 최소값 구하기?
    minimum_loss = max(price)
    for i in range(len(price)-1):
        selling = price[i:]
        selling.sort() 
        x = selling.index(price[i])
        if x == 0:
            continue
        else:
            minimum_loss = min(minimum_loss, price[i] - selling[x-1])
    return minimum_loss

price = [20, 7, 8, 2, 5]
print(minimumLoss(price))