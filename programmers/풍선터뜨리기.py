def solution(a):
    
    # 양 쪽의 최솟값 중 하나라도 내가 크면 된다! 이길 수 있다!
    
    if len(a) == 1:
        return 1

    answer = 2   

    l_min = [a[0]]     
    r_min = [a[-1]]
    for i in range(1, len(a)):
        if a[i] < l_min[-1]:
            l_min.append(a[i])
        else:
            l_min.append(l_min[-1])
        if a[len(a) - 1 - i] < r_min[-1]:
            r_min.append(a[len(a) - 1 - i])
        else:
            r_min.append(r_min[-1])
    r_min.reverse()    

    for i in range(1, len(a) - 1):
        if l_min[i - 1] > a[i] or r_min[i + 1] > a[i]:
            answer += 1
    
    return answer

a = [9,-1,-5]
print(solution(a))