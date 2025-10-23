def solution(s, t):
    while t:
        if s == t:
            return 1
        if t[-1] == 'A':
            t.pop()
        elif t[-1] == 'B':
            t.pop()
            t.reverse()
    return 0

s = list(input().strip())
t = list(input().strip())
print(solution(s,t))