# 길이가 같은 배열 A와 B가 있다. 
# 각 순서대로 곱을 합한 값을 가장 작게 만들기 위해 배열 A를 재배열했을 때,
# 결과값을 구하라.

n = int(input())
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
a.sort(reverse=True)
b.sort()
result = 0
for i in range(n):
    result += a[i]*b[i]
print(result)