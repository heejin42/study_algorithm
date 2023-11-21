def luckBalance(k, contests):
    n = len(contests)
    answer = 0
    contests.sort(key = lambda x:-x[0])
    for i in range(n):
        l, t = contests[i]
        if t == 0:
            answer += l
        else:
            if k > 0:
                answer += l
                k -= 1
            else:
                answer -= l
    return answer            
    # 최대 k개의 important 대회를 질 수 있다면 모든 대회를 끝난 최대 luck을 구하라
    # 지면 l을 얻고, 이기면 l을 잃는다. 
    
    
    
k = 3
contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
print(luckBalance(k, contests))