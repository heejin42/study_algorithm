# 분수의 순서: 1/1 1/2 2/1 3/1 2/2 1/3 1/4 2/3 3/2 4/1 5/1 4/2 3/3 2/4 1/5
# X번째 순서를 구하라
# 1 + 2 + 3 + 4 + 5개

def get_line(x):
    for i in range(1, x+1):
        if x <= i:
            return i, x
        x -= i
            
def solution(x):
    line, order = get_line(x)
    if line%2 == 1: # 홀수인 경우, 아래서부터
        head = line - (order-1)
        leg = order
    else: # 짝수인 경우, 위에서부터
        head = order
        leg = line - (order-1)
    return str(head) + '/' + str(leg)

x = int(input())
print(solution(x))