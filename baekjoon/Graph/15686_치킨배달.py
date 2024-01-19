from itertools import combinations
# 치킨집을 m개만 남기는 모든 경우에서 도시의 치킨 거리가 가장 적게 되는 값을 구하라
n, m = map(int, input().split(' '))
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split(' '))))

market = []
house = []
for i in range(n):
    for j in range(n):
        if maps[j][i] == 2:
            market.append([i, j])
        elif maps[j][i] == 1:
            house.append([i, j])
answer =  len(house) * n * 2
for market_list in combinations(market, m):
    city_distance = 0
    for i, j in house:
        distance = 2*n
        for mi, mj in market_list:
            distance = min(distance, abs(i-mi) + abs(j-mj))
        city_distance += distance
    answer = min(city_distance, answer)       

print(answer)
            
# m개의 치킨집을 남기는 경우마다
    # 도시의 치킨 거리를 구해야한다.