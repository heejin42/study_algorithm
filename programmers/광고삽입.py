def solution(play_time, adv_time, logs):
    # 동영상 길이, 공익광고 길이, 구간정보(300,000)
    # HH:MM:SS
    # 시청자들의 누적재생시간이 가장 많은 구간에 공익광고를 삽입하려고 한다. 
    # 시작 시간을 리턴하라.
    # 먼저 모든 수치를 초로 바꿀 것
    # 각 초마다 시청자수를 구할까? 
    pt = int(play_time[0:2])*3600+int(play_time[3:5])*60+int(play_time[6:])
    at = int(adv_time[0:2])*3600+int(adv_time[3:5])*60+int(adv_time[6:])
    all_time = [0 for _ in range(pt+1)]
    for log in logs:
        start, end = log.split('-')
        st = int(start[0:2])*3600+int(start[3:5])*60+int(start[6:])
        et = int(end[0:2])*3600+int(end[3:5])*60+int(end[6:])
        all_time[st] += 1
        all_time[et] -= 1
    for i in range(1, pt):
        all_time[i] = all_time[i-1] + all_time[i]
    for i in range(1, pt):
        all_time[i] = all_time[i-1] + all_time[i]
    most_view = 0
    max_time = 0
    for i in range(at-1, pt):
        view = all_time[i] - all_time[i-at]
        if most_view < view:
            max_time = i - at + 1
            most_view = view
            
    
    hour = max_time//3600
    minutes = (max_time - hour*3600) // 60
    seconds = max_time%60
    answer = "%02d:%02d:%02d"% (hour, minutes, seconds)
    
    return answer

play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
print(solution(play_time, adv_time, logs))