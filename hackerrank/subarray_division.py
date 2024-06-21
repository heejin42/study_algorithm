def birthday(s, d, m):
    answer = 0
    if len(s) < m:
        return 0
    for i in range(len(s)-m+1):
        if sum(s[i:i+m]) == d:
            answer += 1
    return answer

s = [1,2,1,3,2]
d = 3
m = 2
print(birthday(s,d,m))