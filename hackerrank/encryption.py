def encryption(s):
    charactors = list(s)
    x = len(s) ** (1/2)
    rows = int(x)
    if x-rows > 0:
        columns = rows + 1
    else:
        rows = columns
    if rows*columns < len(s):
        rows += 1
        
    answer = ''
    for j in range(columns):
        for i in range(rows):
            if columns*i + j < len(s):
                answer += s[columns*i + j]
        answer += ' '
    return answer
    
s = 'chillout'
print(encryption(s))