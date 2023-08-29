def is_right(s):
    stack = []
    for i in s:
        if len(stack) == 0: 
            stack.append(i)
        else:
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 0:
        return True
    else:
        return False            
            
        

def solution(s):    
    # s를 왼쪽으로 한칸씩 이동, len(s)의 경우 중 올바른 괄호의 개수는?
    # s < 1000
    answer = 0
    for i in range(len(s)):
        new_s = s[i:]+s[:i] 
        if is_right(new_s): 
            answer += 1
    return answer

s = "}}}"
print(solution(s))