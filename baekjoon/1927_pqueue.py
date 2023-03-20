from Queue import PriorityQueue
import sys

input = sys.stdin.readline
N = int(input())
queue = PriorityQueue()
for n in range(N):
    comm = int(input())
    if comm == 0:
        if queue.empty():
            print(0)
        else:
            print(queue.get())
    else:
        queue.put(comm)

