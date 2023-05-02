import sys
input = sys.stdin.readline
total_pay = int(input())
n = int(input())
for i in range(n):
    price, cnt = map(int, input().split(' '))
    total_pay = total_pay - (price*cnt)

if total_pay == 0:
    print('Yes')
else:
    print("No")    
