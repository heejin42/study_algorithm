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
            x = queue.get()
            print(x[1])
    else:
        if comm < 0:
            queue.put((-comm, comm))
        else:
            queue.put((comm, comm))
    
