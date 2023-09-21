def solution(s):
    a, b = 0, 0
    while s!='1':
        a += 1
        next_s = s.replace('0', '')
        b += (len(s) - len(next_s))
        if next_s == '1':
            break
        else:
            s = bin(len(next_s))[2:]
    answer = [a, b]
    return answer

s = "110010101001"
print(solution(s))
