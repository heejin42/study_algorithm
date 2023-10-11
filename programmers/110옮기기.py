from collections import deque
 
def solution(s):
    answer = []
    for cur in s:
        q = deque()  
        zcnt = 0  # 0의 개수
        cnt = 0  # "110"이 삽입된 개수

        for i in range(len(cur)):
            # "110" 추출
            if len(q) > 1 and cur[i] == '0' and q[-2] == '1' and q[-1] == '1':
                q.pop()
                q.pop()
                cnt += 1
                continue
 
            if cur[i] == '0':
                zcnt += 1
                
            q.append(cur[i])
        
        new_s = ""
        while q:
            if not zcnt and cnt:
                new_s += "110" * cnt
                cnt = 0
        
            if q[0] == '0':
                zcnt -= 1
                
            new_s += q.popleft()
        
        if cnt:
            new_s += "110" * cnt
        
        answer.append(new_s)
    
    return answer


s = ["1110","100111100","0111111010"]
print(solution(s))