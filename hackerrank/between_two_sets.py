def getTotalX(a, b):
    answer = 0
    for i in range(max(a), min(b)+1):
        answer += (all([i%aa == 0 for aa in a]) and all([bb%i==0 for bb in b]))
    return answer 
    
a = [20, 60, 100]
b = [200, 300, 400]
getTotalX(a,b)