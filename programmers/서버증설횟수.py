import numpy as np

def solution(players, m, k):
    answer = 0
    server = np.array([])
    for p in players:
        # 증설된 서버에 시간 더해주기
        if len(server) > 0:
            server = np.subtract(server, 1)
        # 만료된 서버 삭제
        cnt = 0
        for s in server:
            if s == 0:
                cnt += 1
            else:
                break
        server = server[cnt:]
        
        # p명이 플레이하기 위해 현재 서버 체크 -> 필요한 개수 증설 
        if p//m > len(server):
            needs = p//m - len(server)
            for i in range(needs):
                server = np.append(server,k)
            answer += needs
    return answer

players = [0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
m = 1
k = 1
print(solution(players, m, k))
