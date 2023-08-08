def solution(n, t, m, timetable):
    answer = 0
    
    timetable = [int(time[:2])*60+int(time[3:]) for time in timetable]  # 시간 -> 분 change
    timetable.sort()
    busTime = [9*60+t*i for i in range(n)]  

    i = 0  
    for bt in busTime:  
        cnt = 0 
        while cnt<m and i<len(timetable) and timetable[i]<=bt:
            i += 1
            cnt += 1
        if cnt<m:  
            answer = bt
        else: 
            answer = timetable[i-1]-1
            
    return str(answer//60).zfill(2)+":"+str(answer%60).zfill(2)
    
            
                
        
n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]

print(solution(n,t,m,timetable))