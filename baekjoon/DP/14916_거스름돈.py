import sys
input = sys.stdin.readline

def sol(money):
    cnt = 0

    while money > 0:
        if money % 5 == 0:
            cnt += money//5
            break
        else:
            money -= 2
            cnt += 1

    if money < 0:
        print(-1)
    else:
        print(cnt)


if __name__ == '__main__':
    money = int(input())

    sol(money)