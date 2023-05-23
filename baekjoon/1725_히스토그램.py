import sys
input = sys.stdin.readline

n = int(input())
heights = []
for _ in range(n):
    heights.append(int(input()))
heights.append(0)    
stack = [(0, heights[0])]
left = 0
res = 0
for i in range(1, n+1):
    left = i
    while stack and stack[-1][1] > heights[i]:
        left, h = stack.pop()
        res = max(res, (i-left) * h)
    stack.append((left, heights[i]))
    
print(res)
        