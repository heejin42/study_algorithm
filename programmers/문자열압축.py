# 문자열 압축하여 가장 짧은 것의 길이를 return 하는 문제
# 압축 방법은 1개 이상의 단위로 잘라 같은 값이 연속해서 나타나면 개수로 표현하는 방법
# s 길이는 1 이상 1,000 이하

def solution(s):
    answer = len(s)
    if len(s)==1:
        return 1
    for i in range(1, len(s)+1):
        b = ''
        cnt = 1
        tmp=s[:i]
        for j in range(i, len(s)+i, i):
            if tmp==s[j:i+j]:
                cnt+=1
            else:
                if cnt!=1:
                    b = b + str(cnt)+tmp
                else:
                    b = b + tmp
                tmp=s[j:j+i]
                cnt = 1
        answer = min(answer, len(b))
    return answer

s = "aabbaccc"
print(solution(s))