# n개의 블루레이에 기타 강의를 나눠서 녹화할 예정
# 블루레이 크기를 가장 작게 = 즉 골고루 나누는 방법은?
n, m = map(int, input().split(' '))
videos = list(map(int, input().split(' ')))
start = max(videos)
end = sum(videos)
while start <= end:
    mid = (start+end)//2
    cnt = 1
    length = 0
    for video in videos:
        if length + video <= mid:
            length += video
        else:
            cnt += 1
            length = video
            
    if cnt > m:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1 
        
print(ans) 