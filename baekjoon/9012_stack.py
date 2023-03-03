T = int(input())


for t in range(T):
    flag = 0
    ps = list(input())
    while len(ps) > 0:
        if flag < 0:
            break
        else:
            x = ps.pop()
            if x == ')':
                flag += 1
            else:
                flag -= 1
    if len(ps) == 0 and flag == 0: 
        print("YES")
    else:
        print("NO")