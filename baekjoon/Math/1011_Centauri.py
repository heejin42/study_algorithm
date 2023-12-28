# x 지점부터 y지점까지의 최소 이동 횟수를 구하라
# dp 가능하지 않을까? (이동 횟수, 이동 거리 기록하기)
# 규칙을 찾아서 수학적으로 푸는 문제! 경우를 다 따지기에는 y의 범위가 너무 크다.
T = int(input()) 

for i in range(T):
  x, y = map(int, input().split()) #출발 및 도착 지점

  d = y - x #거리

  n = 0

  while True:
    if d <= n*(n+1):
      break
    n += 1
  
#총 이동 거리가 n의 제곱보다 작거나 같을 때
  if d <= n**2:
    print(n*2-1)
 
#총 이동 거리가 n의 제곱보다 클 때
  else:
    print(n*2)
