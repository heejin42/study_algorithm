# def solution(routes):
#     routes.sort(key = lambda x:x[1])
#     key = -30001
#     cnt = 0
    
#     for route in routes:
#         if route[0] > key:
#             cnt += 1
#             key = route[1]
            
#     return cnt
    
# routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
# print(solution(routes))

def solution(routes):
    # [진입지점, 나간지점]의 리스트가 있을 떄, 최소 몇개의 단속 카메라를 둬야 다 만날 수 있을까?
    # 나간 지점을 기준으로 sort, 가장 끝에 두었을 때 담을 수 있는 애들을 pass
    answer = 0
    x = -30001
    routes.sort(key = lambda x:x[1])
    for start, end in routes:
        if start > x:
            answer += 1
            x = end
    return answer

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))