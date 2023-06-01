import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
a = set()
b = set()
for _ in range(n):
    a.add(input().strip())
for _ in range(m):
    b.add(input().strip())

result = sorted(list(a&b))

print(len(result))
for name in result:
    print(name)