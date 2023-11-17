def solution(line):
    # case0. 동일하거나 수평인 경우  
    # (a*d - c*b) == 0 -> continue
    # case1. b가 0인 경우
    # x = -(e/a)
    # y = (e*c)/(a*d) - f/d
    # case2. 일반적인 경우
    # x = (b*f - e*d) / (a*d - c*b)
    # y = (e*c-a*f)/(a*d - b*c)
    cross = []
    for a,b,e in line:
        for c,d,f in line:
            if (a*d - c*b)== 0:
                continue
            else:
                x = (b*f - e*d) / (a*d - c*b)
                y = (e*c-a*f) / (a*d - b*c)
                if x == int(x) and y==int(y):
                    cross.append((int(x),int(y)))
    cross = list(set(cross))
    cross.sort(key = lambda x:x[0])
    max_x, min_x = cross[-1][0], cross[0][0]
    cross.sort(key = lambda x:x[1])
    max_y, min_y = cross[-1][1], cross[0][1]
    n = max_x-min_x
    m = max_y-min_y
    tmp_result = [['.' for _ in range(n+1)] for _ in range(m+1)]
    for x, y in cross:
        tmp_result[y-min_y][x-min_x] = '*'
    result = []
    for l in tmp_result[::-1]:
        result.append(''.join(l))
    return result

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(line))