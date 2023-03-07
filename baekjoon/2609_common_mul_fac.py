import sys

a, b = map(int, sys.stdin.readline().split(' '))

# time out
# for i in range(min(a,b), 0, -1):
#     if a % i == 0 and b % i == 0:
#         print(i)
#         break

# for i in range(max(a,b),a*b):
#     if i % a == 0 and i % b == 0:
#         print(i)
#         break


# 최대공약수
# a & b의 최대 공약수는 b & a를 b로 나눈 나머지의 최대 공약수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수 
# a와 b의 곱을 a와 b의 최대 공약수로 나눈 값
def lcm(a, b):
    return a * b // gcd(a, b)


print(gcd(a, b))
print(lcm(a, b))