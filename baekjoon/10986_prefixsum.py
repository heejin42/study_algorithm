import sys
input = sys.stdin.readline

N,M= map(int, input().split())
num = list(map(int, input().split()))
sum = 0
numRemainder = [0] * M

for i in range(N):
  sum += num[i]
  numRemainder[sum % M] += 1

result = numRemainder[0]

for i in numRemainder:
  result += i*(i-1)//2
  
print(result)
        

# for i in range(1, n):
#     next_p = []
#     for j in p[i-1]:
#         v = j+arr[i]
#         next_p.append(v)
#         if v % m == 0:
#             result += 1
#     next_p.append(arr[i])
#     if arr[i]%m == 0:
#         result += 1
#     p.append(next_p)

# if arr[0]%m == 0:
#     print(result + 1)
# else:
#     print(result)