def solution(land):
    n = len(land)
    m = len(land[0])
    sizes = [0 for _ in range(m)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 1:
                continue
            if land[i][j] == 0:
                continue
            q = [(i, j)]
            visited[i][j] = 1
            dx = [0, 1, 0, -1]
            dy = [1, 0, -1, 0]
            tmp_row = [j]
            tmp_size = 1
            while q:
                now_i, now_j = q.pop()
                for k in range(4):
                    next_i = now_i+dy[k]
                    next_j = now_j+dx[k]
                    if 0 <= next_i < n and 0 <= next_j < m and land[next_i][next_j] == 1 and visited[next_i][next_j] == 0:
                        q.append((next_i, next_j))
                        visited[next_i][next_j] = 1
                        tmp_size += 1
                        tmp_row.append(next_j)
            for x in list(set(tmp_row)):
                sizes[x] += tmp_size
    answer = max(sizes)
    return answer