# 2진 트리 모양의 초원, 각 노드에는 양 또는 늑대
# 노드 방문하며 데리고 간다. 늑대의 수가 같거나 많아지면 잡아먹는다.
# 이진탐색 경우의 수, 최대 양 구하기, dfs 문제


def solution(info, edges):
    visited = [False for _ in range(len(info))]
    result = []
    
    def dfs(sheep, wolf):
        if sheep > wolf:
            result.append(sheep)
        else:
            return
        
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = True
                if info[c] == 0:
                    dfs(sheep+1, wolf)                
                else:
                    dfs(sheep, wolf+1)
                visited[c] = False
    visited[0] = True            
    dfs(1,0)
    result.sort(reverse=True)            
    return result[0]
        
    
info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]  
print(solution(info, edges))