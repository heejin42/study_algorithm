target = int(input())
N = int(input())
broken = [] # 고장난 버튼 저장
if N != 0:
    broken = list(input().split())

answer = abs(target-100) # (+)나 (-) 버튼 만으로 이동할 때

for i in range(1000000): # 0번 부터 999999까지 버튼 누를 수 있는 채널 체크
    num, j = str(i), 0

    while j < len(num):
        if num[j] not in broken:
            j += 1
        else:
            break

    if j == len(num):
        answer = min(answer, len(str(i)) + abs(i-target))

print(answer)