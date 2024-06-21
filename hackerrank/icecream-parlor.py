from itertools import combinations

def icecreamParlor(m, arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == m:
                answer = [i+1, j+1]
    return answer


k = 4
cost = [1, 4, 5, 3, 2]
print(icecreamParlor(k, cost))
