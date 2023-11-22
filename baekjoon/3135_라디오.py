# 현재 주파수 A, 원하는 주파수 B
# +1 증가, -1 감소, 즐겨찾기

def solution(a,b,n,buttons):
    answer = 0
    for button in buttons:
        if abs(button-b) < abs(b-a):
            a = button
            answer = 1
    answer += abs(b-a)
    return answer 
        
        
a = 64
b = 120
n = 1
buttons = [567]
print(solution(a,b,n,buttons))