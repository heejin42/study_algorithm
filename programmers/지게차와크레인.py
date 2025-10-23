# 이차원 배열로 컨테이너 상황 관리, 바깥은 0으로 안에 빈 공간은 1로 표시

def checkOutside(containers, x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    outside = False
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if containers[nx][ny]=="0":
            containers[x][y] = "0"
            outside = True
            break
    
    if outside:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if containers[nx][ny] == "1":  # 빈 공간을 외부랑 연결 "1" -> "0"
                containers[nx][ny] = "0"
                checkOutside(containers, nx, ny)   
    
def crane(containers, c):
    for i in range(1, len(containers)-1):
        for j in range(1, len(containers[0])-1):
            if containers[i][j] == c:
                containers[i][j] = "1"
                checkOutside(containers, i, j)


def fork(containers, c):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    index = []
    for i in range(1, len(containers)-1):
        for j in range(1, len(containers[0])-1):
            if containers[i][j] == c:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if containers[nx][ny] == "0":
                        index.append((i, j))
                        break
    for i, j in index:
        containers[i][j] = "0"
        checkOutside(containers, i, j)

def solution(storage, requests):
    answer = 0
    containers = [["0" for _ in range(len(storage[0])+2)]]
    for s in storage:
        containers.append(["0"]+list(s)+["0"])
    containers.append(["0" for _ in range(len(storage[0])+2)])
    
    for request in requests:
        if len(request)==1:
            fork(containers, request)
        else:
            crane(containers, request[0])
    
    for i in range(1, len(containers)-1):
        for j in range(1, len(containers[0])-1):
            if containers[i][j] not in ["0", "1"]:
                answer += 1
    return answer

storage = ["AZWQY", "CAABX", "BBDDA", "ACACA"]
requests = ["A", "BB", "A"]
print(solution(storage, requests))