# 방 번호를 플라스틱 숫자로 붙이려고 할 때, 플라스틱 숫자는 한 세트로 판다는 것, 6은 9로 이용 가능
# 최소 필요한 개수를 구하라
numbers = list(input())
cnt = [0 for _ in range(10)]
numbers.sort()
for n in numbers:
    cnt[int(n)] += 1
if (cnt[6] + cnt[9]) % 2 == 0:
    new_cnt = (cnt[6] + cnt[9]) // 2
else:
    new_cnt = (cnt[6] + cnt[9]) // 2 + 1
cnt[6] = new_cnt
cnt[9] = new_cnt
print(max(cnt))


