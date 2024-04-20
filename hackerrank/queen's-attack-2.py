def queensAttack(n, k, r_q, c_q, obstacles):
    # 8개 방향으로 살펴보면서 obstacle이나 board 밖으로 나가면 quit
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]    
    cnt = 0
    for i in range(8):
        now = [r_q+dy[i], c_q+dx[i]]
        while now not in obstacles and 0 < now[0] <= n and 0 < now[1] <= n:
            cnt += 1
            now = [now[0]+dy[i], now[1]+dx[i]]
    return cnt 