import sys
input = sys.stdin.readline

def solve(k):
    if k == 1:
        return "-"
    elif k == 3:
        return "- -"
    else:
        string1 = solve(k//3)
        string2 = " " * (k//3)
        return string1+string2+string1

while True:
    try:
        n = int(input())
        print(solve(3**n))
    except:
        break