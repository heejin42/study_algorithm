# 네오가 기억한 멜로디를 담은 문자열 m
# musicinfo = [starttime, endtime, title, codeinfo]
# -> 재생시간, 타이틀, 코드

import math

def solution(m, musicinfos):
    answer = None
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    
    for musicinfo in musicinfos:
        start, end, title, code = musicinfo.split(",")
        
        hour, minute = map(int, start.split(":"))
        start = hour * 60 + minute
        
        hour, minute = map(int, end.split(":"))
        end = hour * 60 + minute
        duration = end - start
        
        code = code.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        code *= math.ceil(duration / len(code))
        code = code[:duration]
        
        if m not in code:
            continue
            
        if answer == None or answer[0] < duration or (answer[0] == duration and answer[1] > start):
                answer = (duration, start, title)
    
    if answer:
        return answer[-1]
    
    return "(None)"

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
print(solution(m, musicinfos))