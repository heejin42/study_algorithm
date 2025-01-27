# 길이 n짜리 수열이 있다. 연속된 수열의 부분합 중 s 이상이 되는 가장 짧은 것의 길이를 구하라
# 0 <= n < 100,000 -> 시간 초과를 방지하기 위해 투포인터로 접근
n, s = map(int, input().split())
arr = list(map(int, input().split()))
start = 0
end = 0
answer = 100000
temp_sum = arr[0]
while start <= end:
    if temp_sum >= s:
        answer = min(answer, end-start+1)
        temp_sum -= arr[start]
        start += 1
        
    else:
        end += 1
        if end < n:
            temp_sum += arr[end]
        else:
            break
        

if answer == 100000:
    print(0)
else:
    print(answer)