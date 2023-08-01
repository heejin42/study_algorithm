def solution(A, B):
    # a를 알고 있을 때 b가 얻을 수 있는 가장 큰 승점은?
    # 길이는 같고 100,000 이하다.
    # 큰 수 정렬하여 앞에서부터 b가 이길 수 있는 수를 찾는다.
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)
    result = 0 
    if B[0] < A[-1]:
        return 0
    for a in A:
        if a < B[0]:
            result += 1
            del B[0]
    return result

A = [2,2,2,2]
B = [1,1,1,1]	
print(solution(A, B))