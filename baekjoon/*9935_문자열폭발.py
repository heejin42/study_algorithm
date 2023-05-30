import sys
input = sys.stdin.readline
target = input().strip()
bomb = input().strip()

stack = []
for i in range(len(target)):
    stack.append(target[i])
    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
        if stack[-len(bomb):] == list(bomb):
            for _ in range(len(bomb)):
                stack.pop()
                
if len(stack) > 0:
    print("".join(stack))
else:
    print("FRULA")