def solution(s):
    answer = 1
    for start in range(len(s)):
        for end in range(len(s), start-1, -1):
            check_s = s[start:end]
            if check_s == check_s[::-1]:
                answer = max(answer, end-start)
    return answer

s = "abcdcba"
print(solution(s))