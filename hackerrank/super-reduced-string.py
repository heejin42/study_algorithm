def superReducedString(s):
    i = 0
    s = list(s)
    while i < len(s)-1:
        if s[i] == s[i+1]:
            del s[i:i+2]
            i -= 1
            if i < 0:
                i = 0
        else:
            i += 1
    if len(s) > 0:
        answer = ''.join(s)
    else:
        answer = 'Empty String'    
    return answer

s = 'aaabccddd'
print(superReducedString(s))
            
        