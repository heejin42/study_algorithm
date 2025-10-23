# 1 <= 강의 개수 N < 100,000
# 각 강의의 시작하는 시간과 끝나는 시간을 알고 있을 때, 
# 최대한 적은 수의 강의실로 모두 할 수 있는 방법은?
# sol: 강의 시작 시간, 종료시간, 강의 번호을 기준으로 정렬
# 적은 수의 강의실을 사용한다? -> 강의실 강의가 끝나면 바로 시작할 수 있도록 함
# 두개의 힙을 사용할까? 대기 중인 수업, 강의중인 수업 마치는 시간 힙

import sys
import heapq

n = int(sys.stdin.readline())
classes = []
for _ in range(n):
    number, start, end = map(int, sys.stdin.readline().split(' '))
    classes.append((start, end, number))
heapq.heapify(classes)
s, e, n = heapq.heappop(classes)
heap = [(e, n)]
heapq.heapify(heap)
cnt = 1

while classes:
    s, e, n = heapq.heappop(classes)
    last_end, last_class = heapq.heappop(heap)
    if s >= last_end:
        # 강의중에 추가
        heapq.heappush(heap, (e, n))
    else:
        # 기존 강의 다시 추가
        # 새로운 강의 추가
        heapq.heappush(heap, (last_end, last_class))
        heapq.heappush(heap, (e, n))
        cnt += 1

print(cnt)