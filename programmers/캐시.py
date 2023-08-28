from collections import deque

def solution(cacheSize, cities):
    # 페이지가 있고, 오래된 것부터 교체
    # cache hit 1, cache miss 5
    # 오래된 것? 일방향 큐!
    answer = 0
    if cacheSize == 0:
        return len(cities)*5
    cache = deque(["" for _ in range(cacheSize)])
    for city in cities:
        print(cache)
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
        else:
            cache.popleft()
            answer += 5 
        cache.append(city)    
    return answer


cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
print(solution(cacheSize, cities))