# 서로 다른 N개의 자연수의 합이 s라고 할 때, 자연수 n의 최대값은?
# 최대로 많은 수가 있으려면 최소 값으로 구성되어야 한다. 
# 1부터 0이 될 때까지 계속 빼야하나?
s = int(input())
cnt = 0
num = 1
while True:
    if s - num < 0:
        break
    s -= num
    cnt += 1
    num += 1
    
print(cnt)