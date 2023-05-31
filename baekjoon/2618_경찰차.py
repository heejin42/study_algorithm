import math
import sys
input = sys.stdin.readline

n = int(input().strip())
k = int(input().strip())

events = []
for _ in range(k):
    events.append(list(map(int, input().split(' '))))

dp1 = [[0, [0, 0]] for _ in range(k)]
dp1[0][0] = abs(events[0][0] - 1) + abs(events[0][1] - 1)
dp1[0][1] = [n, n]
dp2 = [[0, [0, 0]] for _ in range(k)]
dp2[0][0] = abs(events[0][0] - n) + abs(events[0][1] - n)
dp2[0][1] = [1,1]

#f1(n) = f1(n-1) + 경찰차1 or f2(n-1) + 경찰차1
#f2(n) = f1(n-1) + 경찰차2 or f2(n-1) + 경찰차2

for i in range(1, k):
    distance1 = dp1[i-1][0]+abs(events[i-1][0] - events[i][0]) + abs(events[i-1][1] - events[i][1])
    distance2 = dp2[i-1][0]+abs(dp2[i-1][1][0] - events[i][0]) + abs(dp2[i-1][1][1] - events[i][1])
    if distance1 < distance2:
        dp1[i][0] = distance1
        dp1[i][1] = dp1[i-1][1]
    else:
        dp1[i][0] = distance2
        dp1[i][1] = events[i-1]
    
    #dp2[i] = max(dp1[i-1][0]+경찰차2이동거리, dp2[i-1][0]+경찰차2이동거리)    
    dist1 = dp2[i-1][0]+abs(events[i-1][0] - events[i][0]) + abs(events[i-1][1] - events[i][1])
    dist2 = dp1[i-1][0]+abs(dp1[i-1][1][0] - events[i][0]) + abs(dp1[i-1][1][1] - events[i][1])
    if dist1 < dist2:
        dp2[i][0] = dist1
        dp2[i][1] = dp2[i-1][1]
    else:
        dp2[i][0] = dist2
        dp2[i][1] = events[i-1]
        
print(min(dp1[-1][0], dp2[-1][0]))
