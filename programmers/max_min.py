import sys
input = sys.stdin.readline

def solution(s):
    arr = list(map(int, s.split(' ')))
    answer = str(min(arr)) + ' ' + str(max(arr))
    return answer

s = input()
print(solution(s))