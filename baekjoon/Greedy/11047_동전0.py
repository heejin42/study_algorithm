# N 종류의 동전으로 k를 만드는 최솟값을 구하라.
n, k = map(int, input().split(' '))
coins = []
for _ in range(n):
    coins.append(int(input()))
answer = 0
while True:
    if k == 0:
        break
    cnt = k // coins[-1]
    if cnt > 0:
        answer += cnt
        k -= cnt*coins[-1]
    coins.pop()
print(answer)
    