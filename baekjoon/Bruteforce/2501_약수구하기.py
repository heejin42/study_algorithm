# 두개의 자연수 N, k 가 주어졌을 때, n의 약수들 중 k번째 수를 출력하라.
n, k = map(int, input().split(' '))

cnt = 0
can_divide = 0
while cnt < k:
    can_divide += 1
    if can_divide > n:
        can_divide = 0
        break
    if n%can_divide==0:
        cnt += 1
print(can_divide)