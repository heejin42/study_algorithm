# n 길이의 외벽이 있고, 최약 지점 위치가 담긴 배열이 있다.
# 친구들마다 1시간동안 이동할 수 있는 거리가 다르다.
# 취약 지점을 모두 점검하기 위해 보내야 하는 친구 수의 최소값을 구하자.

from itertools import permutations

def solution(n, weak, dist):
    dist.sort(reverse=True)
    len_weak = len(weak)
    weak = weak + [num+n for num in weak] 
    
    for i in range(1,len(dist)+1):
        for ff in permutations(dist[:i]):
            for idx in range(len_weak):
                friends = list(ff[:])
                new_weak = weak[idx:idx+len_weak]
                while friends and new_weak:
                    f = friends.pop(0)
                    w = new_weak.pop(0)
                    current = f+w

                    while new_weak and new_weak[0] <= current:
                        new_weak.pop(0)
                
                if len(new_weak) == 0:
                    return i
    return -1
            

n = 12
weak = [1, 3, 4, 9, 10]
dist = [3, 5, 7]

print(solution(n, weak, dist))
