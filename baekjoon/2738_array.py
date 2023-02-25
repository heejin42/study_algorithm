m, n = map(int, input().split(' '))
array_1 = []
array_2 = []

for i in range(n):
    array = list(map(int, input().split(' ')))
    array_1.append(array)

for i in range(n):
    array = list(map(int, input().split(' ')))
    array_2.append(array)

for row in range(n):
    for col in range(m):
        print(array_1[row][col] + array_2[row][col], end='')
    print()
