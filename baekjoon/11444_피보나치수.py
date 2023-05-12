import sys
input = sys.stdin.readline

n = int(input())
p = 1000000007

# def fibo(n):
#     dp = [0 for _ in range(n+1)]
#     dp[1] = 1
#     x1 = 0
#     x2 = 1
#     for i in range(2, n+1):
#         x = x1 + x2
#         x1 = x2
#         x2 = x
#     return x2

def mul(A, B):
    n = len(A)
    Z = [[0]*n for _ in range(n)]
    
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += A[row][i] * B[i][col]
            Z[row][col] = e % p
            
    return Z

def square(A, k):
    if k == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= p
        return A
    
    tmp = square(A, k//2)
    if k % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)
    
fib_matrix = [[1, 1], [1, 0]]
print(square(fib_matrix, n)[0][1])
    

#print(fibo(n)%p)