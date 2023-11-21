# 정수 배열 arr, 정수 k가 주어질 데, arr로 k 길이의 배열을 만들 수 있다.
# 배열 최대와 최소 차이가 작아지는 배열을 찾아 차이를 리턴하라.
# 2 <= 배열의 길이 <= 100,000
# 최대와 최소 차이가 작아지는 배열이 무엇일까?
# 내림차순 정렬을 한 후, arr[i] - arr[i+k]가 최소가 되는 i를 구해야 한다.
def maxMin(k, arr):
    k -= 1
    n = len(arr)
    arr.sort(reverse=True)
    answer = arr[0]-arr[-1]
    for i in range(n-k):
        answer = min(answer, arr[i] - arr[i+k])
    return answer
    
n = 7
k = 3
arr = [10, 100, 300, 200, 1000, 20, 30]
print(maxMin(k, arr))
