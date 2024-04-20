
def organizingContainers(container):
    # 한 종류가 찢어질 수 없다.
    # 각각의 종류 개수를 n개로 묶어서 총 합이 == 이면 된다.
    containers = []
    dic = {}
    for contain in container:
        containers.append(sum(contain))
        
        for i in range(len(contain)): 
            if i in dic:
                dic[i] += contain[i]
            else:
                dic[i] = contain[i]
    for k in dic:
        if dic[k] in containers:
            x = containers.index(dic[k])
            containers[x] = 0
        else:
            return 'Impossible'
    return 'Possible'
    

container = [[1, 1], [1, 1]]
print(organizingContainers(container))