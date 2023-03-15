import sys
a, b, c = map(int, sys.stdin.readline().split(' '))

def calculator(a,b,c):
    if b == 1:
        return a%c
    else:
        tmp = calculator(a, b//2, c)
        if b%2 == 1:
            return (tmp*tmp*a)%c
        elif b%2 == 0:
            return (tmp*tmp)%c

print(calculator(a,b,c))