import sys
input = sys.stdin.readline
T = int(input())
def get_file_cost(files):
    cost = [0]*len(files)
    for i in range(len(files)):
        if i == 0:
            cost[i] = files[i]
        else: 
            idx = cost.index(min(cost[:i]))
            cost[i] = files[i] + cost[idx] + cost[idx]
            cost[idx] = 1e9

    print(cost[-1])

for t in range(T):
    k = int(input())
    files = list(map(int,input().split(' ')))
    get_file_cost(files)

