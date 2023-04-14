from collections import deque
def solution(bridge_length, weight, truck_weights):
    t = 1
    index = 1
    times = deque([1])
    queue = deque([truck_weights[0]])
    while index < len(truck_weights):
        truck =  truck_weights[index]
        t += 1
        if len(queue) == 0:
            times.append(t)
            queue.append(truck)
            index += 1
        else:
            if (t - times[0]) == bridge_length:
                times.popleft()
                queue.popleft()
            if sum(queue) + truck <= weight:
                times.append(t)
                queue.append(truck)
                index += 1
    return t + bridge_length

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))