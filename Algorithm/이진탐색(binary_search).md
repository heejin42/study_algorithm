# 이진탐색(binary_search)
이진 탐색 알고리즘은 이분 탐색이라고도 하며 탐색 범위를 두 부분으로 분할하면서 찾는 방식이다.
처음부터 끝까지 탐색하는 것보다 훨씬 빠르다는 장점이 있다.

**시간복잡도**
전체 탐색 -> O(N)
이진 탐색 -> O(logN)

### 진행 순서
- 우선 정렬을 한다.
- 첫 인덱스를 left(start), 끝 인덱스를 right(end)로 하여 mid 인덱스를 설정한다.
- mid의 값과 내가 구하고자 하는 값을 비교한다.
- 구할 값이 mid보다 높으면 left = mid + 1로, 구할 값이 mid보다 작으면 right = mid - 1 로 설정하여 반복한다.
- left > right 가 될 때까지 반복하며, 조건문을 나오게 되면 없는 것으로 확인할 수 있다.

### 예시 - 백준 1300번 문제
```python
n = int(input())
k = int(input())

start = 1
end = n*n

while start <= end:
    mid = (start + end)//2
    count = 0
    for i in range(1, n + 1):
        count += min(mid // i, n)
    
    if count >= k:
			start = mid - 1
    else:
        end = mid + 1
print(left)
```