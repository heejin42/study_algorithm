import sys

input = sys.stdin.readline
N = int(input())
time_schedule = []
for n in range(N):
    time_schedule.append(list(map(int, input().split(' '))))
time_schedule.sort(key = lambda x: (x[1], x[0]))
end_time = 0
count = 0
for meeting in time_schedule:
    if meeting[0] >= end_time:
        end_time = meeting[1]
        count += 1
    else:
        continue
print(count)