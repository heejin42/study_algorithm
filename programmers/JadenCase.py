def solution(s):
    words = s.split(' ')
    answer = ""
    for word in words:
        answer += word.capitalize() + ' '
    return answer[:-1]
    
s = 'for the last week'
print(solution(s))