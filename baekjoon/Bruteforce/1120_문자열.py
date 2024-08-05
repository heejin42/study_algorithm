a, b = input().split(' ')
# a < b, 차이만큼 앞or뒤에 붙일 수 있다.
# 차이가 x라고 할 때, 모두 앞에~모두 뒤에 붙이는 경우 중 같은 게 많은 걸 찾기
# b[x:] ~ b[:-x]
diff = len(b)-len(a)
max_equal = 0
for i in range(diff+1):
    # 앞에 i만큼 붙인 경우 a[:]와 b[i:i+len(a)]까지 비교해보기
    cnt = 0 
    for j in range(0, len(a)):
        if a[j] == b[i+j]:
            cnt += 1
    max_equal = max(max_equal, cnt)
print(len(a) - max_equal)
            