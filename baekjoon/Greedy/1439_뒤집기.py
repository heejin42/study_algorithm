s = input()
record = [0, 1, 0]
index = -1
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        record[index] += 1
        index = index*(-1)
        
answer = min(record[1], record[-1])
print(answer)
# 달라지는 것을 카운트하기?
# 0로 모두 바꾸거나 1로 모두 바꾸는 최소 횟수
# 0 덩어리, 1 덩어리 새기
# 2 / 1
# 1 / 0
# 1 / 1
# 4 / 5
# 3 / 2