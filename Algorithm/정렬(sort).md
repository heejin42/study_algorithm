# 정렬(sort)
정렬이란 섞여 있는 데이터를 순서대로 나열하는 것이다.
정렬 알고리즘은 시간 복잡도에 따라 성능이 좌우되며 성능이 좋을수록 구현 방법이 어려워진다.


## O(n²)의 정렬
* 버블 정렬 (Bubble Sort) - 인접한 두 수를 비교하며 정렬해가는 방법으로 앞에서부터 시작해서 큰수를 뒤로 보내 뒤가 가장 큰 값을 가지도록 완성해가는 과정을 반복한다.
* 선택 정렬 (Selection Sort) - 한 바퀴 돌때 가장 작은 값을 찾아 맨 앞과 교환하는 방식의 정렬이다.
* 삽입 정렬 (Insertion Sort) - 정렬된 데이터 그룹을 늘려가며 추가되는 데이터를 알맞은 자리에 삽입하는 방식이다. 

## O(nlogn)의 정렬 - 중요!
### 병합 정렬 (Merge Sort)
분할 정복과 재귀를 이용한 알고리즘으로 계속해서 반을 쪼개고 합치는 과저에서 그룹을 만들어 정렬하게 된다. 2배의 메모리 공간이 필요하다.
![img](https://images.velog.io/images/jguuun/post/8f6ff9f4-52e7-43df-9664-880830d2f239/Merge-sort-example-300px.gif)
**예제 코드**
```python
array = [8,4,6,2,9,1,3,7,5]

def merge_sort(array):
	if len(array) < 2:
		return arra
	mid = len(array) // 2
	low_arr = merge_sort(array[:mid])
	high_arr = merge_sort(array[mid:])

	merged_arr = []
	l = h = 0
	while l < len(low_arr) and h < len(high_arr):
		if low_arr[l] < high_arr[h]:
			merged_arr.append(low_arr[l])
			l += 1
		else:
			merged_arr.append(high_arr[h])
			h += 1
	merged_arr += low_arr[l:]
	merged_arr += high_arr[h:]
	print(merged_arr)
	return merged_arr
```

### 퀵 정렬 (Quick Sort)
분할 정복 방법을 통해 주어진 배열얼 정렬한다는 점에서 병합 정렬과 유사하지만 배열을 비균등하게 분할한다는 점과 추가 메모리가 필요하지 않다는 차이가 있다.

**과정**
1. 배열 가운데서 하나의 원소를 고른다. == 피벗(pivot)
2. 피벗 앞에는 피벗보다 작은 모든 원소들이 오고, 피벗 뒤에는 피벗보다 큰 모든 원소들이 오도록 배열을 둘러 나눈다. 이제 피벗은 더이상 움직이지 않는다.
3. 분할된 두 개의 작은 배열에 대해 재귀적으로 이 과정을 반복한다. 즉 재귀호출이 한번 호출될 때마다 최소 하나의 원소의 위치가 정해진다는 것을 보장할 수 있다.

**특징**
불안정 정렬이기 때문에 최악의 경우 == 배열이 오름차순, 내림차순으로 이미 정렬이 되어 있는 경우에는 매번 파티션이 나누어지지 않는 경우가 된다. 이 때 시간복잡도는 O(n²)이 되지만 최악의 경우를 제외한 모든 경우는 O(nlogn)으로 괜찮은 성능을 보인다.

**예제 코드**
```python
array = [8,4,6,2,5,1,3,7,9]

def quick_sort(array):
	if len(array) <= 1:
		return array
	pivot = len(array) // 2
	front_arr, pivot_arr, back_arr = [], [], []
	for value in array:
		if value < array[pivot]:
			front_arr.append(value)
		elif value > array[pivot]:
			back_arr.append(value)
		else:
			pivot_arr.append(value)
	print(front_arr, pivot_arr, back_arr)
	return quick_sort(front_arr) + quick_sort(pivot_arr) + quick_sort(back_arr)
```

### 파이썬의 정렬 메소드
sort(), sorted() 등의 정렬 함수는 입력의 크기가 커질 경우 효츌적으로 정렬하기 위해 퀵 정렬과 같은 진화된 방식을 사용한다.
그러므로 O(nlogn)이 된다.