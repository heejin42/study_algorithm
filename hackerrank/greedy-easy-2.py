def minimumAbsoluteDifference(arr):
    # 요소들 간의 최소 차를 구하라
    # 2 < n < 10^5, -10^9 < arr[i] < 10^9
    arr.sort()
    answer = []
    for i in range(len(arr)-1):
        answer.append(arr[i+1]-arr[i])
    return min(answer)
    
arr = [3, -7, 0]
print(minimumAbsoluteDifference(arr))