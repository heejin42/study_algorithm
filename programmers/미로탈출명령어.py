def solution(n, m, x, y, r, c, k):
    # n x m의 미로
    # (x, y) -> (r, c) 이동해야 한다.
    # 거리가 총 k여야 한다. 같은 곳 재방문 가능함.
    # 미로에서 탈출한 경로 중 사전 순으로 가장 빠른 경로, 불가능하면 impossible return
    # 이동경로 - l:왼 r:오 u:위 d:아래 / 사전 순 -> d l r u
    # k <= 2500
    # 재방문 가능하며 k여야 한다. k만큼 반복, bfs
    # x -> r, y -> c 까지 필요한 이동 count
    answer = ''
    dist = abs(x - r) + abs(y - c)
    k -= dist

    if k < 0 or k % 2 != 0:
        return "impossible"

    direction = {'d': 0, 'l': 0, 'r': 0, 'u': 0}

    if x > r:
        direction['u'] += x - r
    else:
        direction['d'] += r - x

    if y > c:
        direction['l'] += y - c
    else:
        direction['r'] += c - y

    answer += 'd' * direction['d']

    d = min(k // 2, n - (x + direction['d']))
    answer += 'd' * d
    direction['u'] += d
    k -= 2 * d

    answer += 'l' * direction['l']
    l = min(k // 2, y - direction['l'] - 1)
    answer += 'l' * l
    direction['r'] += l
    k -= 2 * l

    answer += 'rl' * (k // 2)
    answer += 'r' * direction['r']
    answer += 'u' * direction['u']

    return answer

n = 3
m = 4
x = 2
y = 3 
r = 3
c = 1
k = 5
print(solution(n, m, x, y, r, c, k))