from collections import deque
def solution(order):
    # 배달하는 순서에 맞게 택배를 실어야 한다.
    # 해당 택배를 실을 순서가 될 때까지 다른 곳에 보관해야 하므로 보조 컨테이너 벨트를 설치한다. 
    # 스택의 구조, 가장 마지막의 보관한 상자만 뺄 수 있다.
    # 몇개의 상자를 실을 수 있는지 
    q = deque(order)
    stack = []
    i = 1
    while q:
        if i == q[0]:
            q.popleft()
            i += 1
        elif len(stack) > 0 and stack[-1] == q[0]:
            stack.pop()
            q.popleft()
        else:
            if i > len(order) and stack[-1]!=q[0]:
                break
            else:
                stack.append(i)
                i += 1
    answer = len(order)-len(q)
    return answer

order = [5,4,3,2,1]
print(solution(order))