import sys

def solution(n, lectures):
    lectures.sort(key = lambda x:(x[1], x[0]))
    count = 1
    start_t, end_t = lectures[0]
    for i in range(1, n):
        next_st, next_et = lectures[i]
        if next_st >= end_t:
            count += 1
            start_t = next_st
            end_t = next_et
    return count

n = int(input())
lectures = []
for _ in range(n):
    lectures.append(list(map(int, sys.stdin.readline().strip().split(' '))))

print(solution(n, lectures))