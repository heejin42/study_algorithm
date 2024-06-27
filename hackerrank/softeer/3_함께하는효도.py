# 열매량의 nxn 배열이 주어지고, m명의 친구 초기 위치가 주어질 때
# 인접한 네칸을 수확(3초)한다. 겹칠 수 있고, 최대 수확량을 구하라
# m 최대 3명이므로 모든 경우의 수를 구해도 될 듯
from collections import deque
def solution(n, fruits, friends):
    # start = 0
    # visited = [[0 for _ in range(n+1)] for _ in range(n+1)]
    # for friend_x, friend_y  in friends:
    #     start += fruits[friend_y][friend_x]
    #     visited[friend_y][friend_x] = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # 각 친구가 방문하는 모든 경우의 수를 구하고 그 조합을 구해서 중복제거 -> 합 찾기
    all_cases = []
    for friend_x, friend_y in friends:
        # friend_x, friend_y에서 3번 이동해서 갈 수 있는 경우를 구하자
        cases = []
        routes = deque([[friend_x, friend_y]])
        # dfs로 구하기
        while routes:
            route = routes.popleft()
            if len(route) == 4:
                cases.append(route)
                continue
            for i in range(4):
                next_x = route[-1][0] + dx[i]
                next_y = route[-1][1] + dy[i]
                if 0 < next_x <= n and 0 < next_y <= n:
                    new_route = route.append(next_x, next_y)
                    routes.append(new_route)
        all_cases.append(cases)
    print(all_cases)
                
        


n, m = map(int, input().split(' '))
fruits = []
for _ in range(n):
    fruits.append(list(map(int, input().split(' '))))
friends = []
for _ in range(m):
    xi, yi = map(int, input().split(' '))
    friends.append((xi, yi))

print(solution(n, fruits, friends))