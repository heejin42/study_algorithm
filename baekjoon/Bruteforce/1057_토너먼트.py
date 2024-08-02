
def solution(a, b):
    r = 1
    while a != 0 and b != 0:
        a = (a+1)//2
        b = (b+1)//2
        if a == b:
            return r
        r += 1
    return -1
    

N, a, b = map(int, input().split(' '))
print(solution(a,b))
