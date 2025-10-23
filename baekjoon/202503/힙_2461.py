# 학급 수와 각 학급의 학생 수
# 학급 별 학생들의 능력치
# 반마다 대표를 뽑는데, 최소 최대 차이가 가장 적게 나는 경우는?
# 학급, 학생 수 < 1,000 -> 모든 경우의 수를 구하면 time limit 걸림
# 능력치 10의 9승까지
# sol: 선발된 학생들의 능력치가 가장 비슷하게 한다 
# 먼저 가장 최솟값들을 모은다, 가장 최솟값을 빼고 그 그룹 다음 숫자 채택해서 넣기
# 또 최솟값 체크 -> 다음 숫자가 없는 경우 최솟값으로 확정
# 최댓값인 경우는 그냥 업데이트


import sys
import heapq

n, m = map(int, sys.stdin.readline().split(' '))
s_dic = {}
heap = []
for i in range(n):
    students = list(map(int, sys.stdin.readline().split(' ')))
    students.sort()
    heap.append((students[0], i))
    s_dic[i] = students[1:]

heapq.heapify(heap)
while heap:
    x, i = heapq.heappop(heap)
    if len(s_dic[i])==0:
        minVal = x
        break
    
    if heap[0][0]-x > s_dic[i][0]-heap[-1][0]:
        heapq.heappush(heap, (s_dic[i][0], i))
        s_dic[i] = s_dic[i][1:]
    else:
        minVal = x
        break
        
print(heap[-1][0]-minVal)

