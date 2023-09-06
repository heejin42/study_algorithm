from collections import deque
def solution(x, y, n):
    # 연산 x*n x*2 x*3 중에 해서 y가 되는 가장 적은 연산 횟수
    answer = -1
    visited = [0 for _ in range(y+1)]
    visited[x] = 1
    q = deque([[x, 0]])
    print(q)
    while q:
        print(q)
        num, c = q.popleft()
        print(num, c)
        if num == y:
            return c
        
        candidates = [num+n, num*2, num*3]
        for candidate in candidates:
            print(candidate)
            if candidate <= y and visited[candidate]==0:
                q.append([candidate, c+1])
                visited[candidate]=1             
    return answer


x = 10
y = 40
n = 30
print(solution(x,y,n))