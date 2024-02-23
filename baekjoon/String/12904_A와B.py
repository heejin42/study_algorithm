# 문자열 S를 T로 바꾸는 게임
# 뒤에 A 추가, 뒤집고 뒤에 B 추가
# 바꿀 수 있으면 1, 없으면 0 출력

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