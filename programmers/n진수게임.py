def convert(num, base):
    temp = ''
    N = '0123456789ABCDEF'
    if num == 0:
        return '0'
    while num > 0:
        num, mod = divmod(num, base)
        temp += N[mod]
    return temp[::-1]    

def solution(n, t, m, p):
    answer = ''
    game = ''
    for i in range(m*t):
        game += convert(i, n)
    # m 기준으로 자르고, 그중 p번째 더하기
    cur = p-1
    while 1:
        if len(answer) == t:
            break
        answer += game[cur]
        cur += m
    return answer


n = 16
t = 16
m = 2
p = 1
print(solution(n, t, m, p))