# 비교할 대상인 array_n은 이분탐색을 위해 오름차순 정렬을 해준다.
n = int(input())
array_n = input().split(' ')
array_n.sort()
m = int(input())
array_m = input().split(' ')

# 이분 탐색 함수
def binary_search_m(start, end, m, array_n):
    while start <= end:
        # 중간 값을 계속 비교해가며 비교할 숫자의 후보를 절반씩 줄여간다.
        mid = (start+end)//2
        if array_n[mid] == m:
            # m 값을 찾을 경우
            return True
        elif array_n[mid] > m:
            end = mid - 1
        else:
            start = mid + 1
    # 못 찾고 while 문을 빠져나올 경우
    return False


for m in array_m:
    if binary_search_m(0, len(array_n)-1, m, array_n):
        print(1, end = ' ')
    else:
        print(0, end = ' ')