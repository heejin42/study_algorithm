# 1억x1억 구구단을 외우려고 한다.
# 숫자 e가 주어지고 그 이하의 임의의 수 s가 여러개 주어질 때,
# 각 s보다는 크고 e보다는 작은 수 중에서 억억단에 가장 많이 등장한 수를 답하라
# 많이 등장한 수가 여러개라면 그중 가장 작은 수를 답할 것

# 구구단은 대칭이다. -> i -> i 까지만 확인


e = 8
starts = [1,3,7]
count_num = [0 for _ in range(e+1)]
for i in range(min(starts), e+1):
    for j in range(1, i):
        if i * j > e:
            break
        count_num[i*j] += 2 
    if i*i <= e:
        count_num[i*i] += 1

result = []           
for s in starts:
    x = count_num[s:].index(max(count_num[s:]))
    result.append(s+x)
print(result)