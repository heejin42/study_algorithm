# N명의 사람들이 각자 돈을 인출하는데 걸리는 시간이 P array로 주어진다.
# 모두가 돈을 인출하는데 걸리는 시간이 최소가 되려면? 짧게 걸리는 사람부터 하면 된다?

n = int(input())
P = list(map(int, input().split(' ')))
P.sort()
for i in range(1, n):
    P[i] += P[i-1]
print(sum(P))