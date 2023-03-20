from Queue import PriorityQueue
import sys

input = sys.stdin.readline
N = int(input())
queue = PriorityQueue()

for n in range(N):
    command = int(input())
    if command == 0:
        if queue.empty():
            print(0)
        else:
            x = queue.get()
            print(x[1])
    else:
        queue.put((-command, command))
    
