def rotate(key, m):
    new_key = [[] for _ in range(m)]
    for i in range(m):
        for j in range(m-1, -1, -1):
            new_key[i].append(key[j][i])
    return new_key

def check(new_lock, n):
    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if new_lock[i][j] != 1:
                return False
    return True
   
def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0 for _ in range(3*n)] for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]
    for _ in range(4):
        key = rotate(key, m)
        for i in range(1, 2*n):
            for j in range(1, 2*n):
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] += key[x][y]
                if check(new_lock, n):
                    return True
                for x in range(m):
                    for y in range(m):
                        new_lock[i+x][j+y] -= key[x][y] 
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	
print(solution(key, lock))