# m과 n 사이의 완전 제곱수를 구하라
# 없는 경우, -1

def check_num(n):
    divide = 1
    while True:
        if n/divide == divide:
            return True
        elif divide*divide>n:
            break
        else:
            divide += 1
    return False

m = int(input())
n = int(input())

answer = []
for num in range(m, n+1):
    if check_num(num):
        answer.append(num)

if len(answer) == 0:
    print(-1)
else:
    print(sum(answer))
    print(answer[0])