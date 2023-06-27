def solution(arr):
    # -를 만날때까지 최대, 최소를 계산할 것!
    max_num = int(arr[-1])
    min_num = int(arr[-1])
    keep = ''
    for i in range(len(arr)-2, -1, -1):
        if i%2 == 1:
            keep = arr[i]
        else:
            num = int(arr[i])
            if keep == '-':
                max_num_1 = num - min_num
                min_num = num - max_num
                max_num = max_num_1
            elif keep == '+':
                max_num = num + max_num
                min_num = num + min_num
    return max_num


arr = ["5", "-", "3", "+", "1", "+", "2", "-", "4"]
print(solution(arr))
