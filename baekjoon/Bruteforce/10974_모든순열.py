from itertools import permutations
n = int(input())
arr = [i for i in range(1, n+1)]
p = list(permutations(arr, n))
p.sort()
for arr in p:
    print(*arr)
