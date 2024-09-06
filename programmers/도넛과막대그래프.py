def check_donut(start_dic, end_dic, n):
    nodes = [n]
    while True:
        if n not in start_dic or len(start_dic[n]) != 1:
            break
        n = start_dic[n][0]
        if n == nodes[0]:
            return True
    return False

def check_bar(start_dic, end_dic, n):
    # 끝이 나오면 bar
    nodes = [n]
    while True:
        if n not in start_dic:
            return True
        if len(start_dic[n]) > 1:
            break
        n = start_dic[n][0]
    return False



def solution(edges):
    # 먼저 정점을 찾는다. = 나가는 건 있고 들어오는 건 없다.
    start_dic = {}
    end_dic = {}
    answer = [0,0,0,0]
    for a, b, in edges:
        if a not in start_dic:
            start_dic[a] = [b]
        else:
            start_dic[a].append(b)
        if b not in end_dic:
            end_dic[b] = [a]
        else:
            end_dic[b].append(a)
    for i in list(start_dic.keys()):
        if len(start_dic[i]) >= 2 and i not in end_dic:
            start_node = i
            answer[0] = start_node
            break
    for x in start_dic[start_node]:
        if check_donut(start_dic, end_dic, x):
            answer[1] += 1
            continue
        if check_bar(start_dic, end_dic, x):
            answer[2] += 1
            continue
        answer[3] += 1
            
    return answer

edges = [[2, 3], [4, 3], [1, 1], [2, 1]]
print(solution(edges))