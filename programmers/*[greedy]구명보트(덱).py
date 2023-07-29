from collections import deque

def solution(people, limit):
    people = deque(sorted(people, reverse=True))
    answer = 0
    while len(people) > 1: 
        answer += 1
        if people[0] + people[-1] <= limit:   
            people.pop()
            people.popleft()
        else:
            people.popleft()
    if len(people) == 1:
        answer += 1
    return answer

people = [70, 50, 80, 50]
limit = 100
print(solution(people, limit))
