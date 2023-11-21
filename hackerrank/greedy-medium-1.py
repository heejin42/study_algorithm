def getMinimumCost(k, c):
    total = 0
    counter = 0
    length = len(c)
    c.sort(reverse=True)

    for i in range(0, length):
        total += (counter + 1) * c[i]
        if length != k and (i + 1) % k == 0:
            counter += 1

    return total
    

    
    
k = 3
c = [1, 3, 5, 7, 9]
print(getMinimumCost(k,c))