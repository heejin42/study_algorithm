from collections import deque
import sys

input = sys.stdin.readline
N = int(input())

for n in range(N):
    commands = list(input())
    count = int(input())
    error_flag = 0
    reverse_flag = 0
    q = deque(input().rstrip()[1:-1].split(','))
    if count == 0:
        q = []
      
        

    for command in commands:
        if command == 'R':
            reverse_flag += 1
        elif command == 'D':
            if len(q) > 0:
                if reverse_flag % 2 == 1:
                    q.pop()
                else:
                    q.popleft()
            else: 
                error_flag = 1
                print('error')
                break

    else:
        if reverse_flag % 2 == 1:
            q.reverse()
        print('[' + ','.join(q) + ']')
