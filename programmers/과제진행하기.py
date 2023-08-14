def solution(plans):
    new_plans = []
    for plan in plans:
        h,m = map(int, plan[1].split(":"))
        new_plans.append([plan[0], h*60+m, int(plan[2])])
    new_plans.sort(key = lambda x:x[1])
    stack = []
    result = []
    for i in range(len(new_plans)):
        if i == len(new_plans)-1:
            stack.append(new_plans[i])
            break
        sub, st, t = new_plans[i]
        nsub, nst, nt = new_plans[i+1]
        
        if st+t <= nst:
            result.append(sub)
            temp_time = nst-(st+t)
            while temp_time != 0 and stack:
                tsub, tst, tt = stack.pop()
                if tt <= temp_time:
                    result.append(tsub)
                    temp_time -= tt
                else:
                    stack.append([tsub, tst, tt-temp_time])
                    temp_time = 0
        else:
            new_plans[i][2] = t - (nst-st)
            stack.append(new_plans[i])
    while stack:
        sub, st, tt = stack.pop()
        result.append(sub)
    return result
        


plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]] 
print(solution(plans))