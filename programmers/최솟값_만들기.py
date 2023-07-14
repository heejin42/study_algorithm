def solution(A, B):
    total = 0
    A.sort()
    B.sort(reverse=True)
    print(A,B)
    for i in range(len(A)):
        total += A[i]*B[i]
        
    return total
        
A = [1,2]
B = [3,4]
print(solution(A, B))
