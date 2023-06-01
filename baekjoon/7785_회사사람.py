import sys
input = sys.stdin.readline
n = int(input())

people = set()
for _ in range(n):
    name, flag = map(str, input().strip().split(' '))
    if flag == "enter":
        people.add(name)
    elif flag == "leave":
        people.remove(name)

result = sorted(list(people), reverse=True)
for name in result:
    print(name)
