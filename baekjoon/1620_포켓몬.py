import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
book = {}
reverse_book = {}
for i in range(1, n+1):
    book[i] = input().strip()
    reverse_book[book[i]] = i
        

for _ in range(m):
    line = input().strip()
    if ord(line[0]) < 65:
        print(book[int(line)])
    else:
        print(reverse_book[line])