# 로프가 주어질 때, 들어올릴 수 있는 물체의 최대 중량을 구하라. 
# 모든 로프를 다 사용할 필요는 없다.
# n개의 로프를 골라서 들 수 있는 무게는? 최소*n 
n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))
rope.sort(reverse=True)
max_weight = 0
for i in range(n):
    max_weight = max(max_weight, rope[i]*(i+1))
print(max_weight)

