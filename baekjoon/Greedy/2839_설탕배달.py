# N킬로그램 배달해야하고, 봉지는 3키로 5키로가 있다.
# 최소 봉지 개수를 구하되, 만들 수 없다면 -1을 출력할 것
# n -= 5 혹은 n -= 3 을 하여 0이 되면 된다. 3을 빼며 값이 5로 나누어 떨어질 때 리턴!

n = int(input())
answer = 0
while True:
    if n < 0:
        answer = -1
        break
    if n == 0:
        break
    if n%5 == 0:
        answer += n//5
        break
    else:
        answer += 1
        n -= 3
        
print(answer)