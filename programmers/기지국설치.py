def solution(n, stations, w):
    # 4g 기지국을 5g 로 바꾼다. 하지만 범위가 더 좁아서 전파가 전달되지 않는 아파트가 생긴다.
    # 모든 아파트에 전파가 전달되도록 하기 위해 추가로 설치해야하는 5g 기지국의 최소 개수는?
    # n = 아파트 개수 n<200,000,000
    # stations = 현재 기지국의 위치 10,000
    # w = 전파의 최종거리 w<10,000
    # station1 + w, station2 - w-1 사이 나누기 
    answer = (stations[0]-w-1)//(w*2+1)
    if (stations[0]-w-1)%(w*2+1) > 0:
        answer += 1
    
    for i in range(1, len(stations)):
        answer += ((stations[i]-w-1) - (stations[i-1]+w)) // (w*2+1) 
        if ((stations[i]-w-1) - (stations[i-1]+w)) % (w*2+1) > 0:
            answer += 1
    if stations[-1] + w < n:
        answer += (n-(stations[-1]+w))//(w*2+1)
        if (n-(stations[-1]+w))%(w*2+1) > 0:
            answer += 1
    return answer

n = 16
stations = [9]
w = 2

print(solution(n, stations, w))
