import sys
input = sys.stdin.readline

n = int(input())
nicknames = []
count = 0
for _ in range(n):
    x = input().strip()
    if x == 'ENTER':
        count += len(set(nicknames))
        nicknames = []
    else:
        nicknames.append(x)
count += len(set(nicknames))
print(count)