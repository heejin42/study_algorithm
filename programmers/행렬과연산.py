from collections import deque

def solution(rc, operations):
    height = len(rc)
    width = len(rc[0])
    left_col = deque([rc[i][0] for i in range(height)])
    right_col = deque([rc[i][width - 1] for i in range(height)])
    rows = deque([deque(rc[i][1:width - 1]) for i in range(height)])

    for op in operations:
        if op == 'ShiftRow':
            left_col.appendleft(left_col.pop())
            rows.appendleft(rows.pop())
            right_col.appendleft(right_col.pop())
        else:  # 'Rotate'
            rows[0].appendleft(left_col.popleft())
            right_col.appendleft(rows[0].pop())
            rows[height - 1].append(right_col.pop())
            left_col.append(rows[height - 1].popleft())
    answer = []
    for i in range(height):
        answer.append([left_col[i]] + list(rows[i]) + [right_col[i]])
    return answer
    
rc = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
operations = ["Rotate", "ShiftRow"]
print(solution(rc, operations))