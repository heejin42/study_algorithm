# def solution(a):
    
#     # 양 쪽의 최솟값 중 하나라도 내가 크면 된다! 이길 수 있다!
    
#     if len(a) == 1:
#         return 1

#     answer = 2   

#     l_min = [a[0]]     
#     r_min = [a[-1]]
#     for i in range(1, len(a)):
#         if a[i] < l_min[-1]:
#             l_min.append(a[i])
#         else:
#             l_min.append(l_min[-1])
#         if a[len(a) - 1 - i] < r_min[-1]:
#             r_min.append(a[len(a) - 1 - i])
#         else:
#             r_min.append(r_min[-1])
#     r_min.reverse()    

#     for i in range(1, len(a) - 1):
#         if l_min[i - 1] > a[i] or r_min[i + 1] > a[i]:
#             answer += 1
    
#     return answer

# a = [9,-1,-5]
# print(solution(a))

def solution(a):
    # n개의 풍선이 있다. 숫자가 써져 있음.
    # 인접한 두 풍선 중 하나를 터트리고 중앙으로 밀착한다.
    # 여기서 번호가 큰 걸 터트려야 하며, 작은 건 한번만 가능
    # 최후로 남을 수 있는 풍선의 개수를 구하는 것
    # 좌 최솟값, 우 최솟값 중 하나만 나보다 크면 된다.
    if len(a) == 1:
        return 1
    answer = 2
    for i in range(1, len(a)-1):
        if a[i] < min(a[:i]) or a[i] < min(a[i+1:]):
            answer += 1
    return answer
        

a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
print(solution(a))