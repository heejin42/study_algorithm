def solution(s):
    if len(s)%2 != 0:
        return 0
    if len(s) == 2:
        return 1 if s[0]==s[1] else 0
    stack = [s[0]]
    for v in s[1:]:
        if len(stack) > 0 and stack[-1] == v:
            stack.pop()
        else:
            stack.append(v)
    return 0 if len(stack) > 0 else 1    
    

s = 'cdcd'
print(solution(s))