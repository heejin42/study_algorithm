# begin에서 target으로 변환하는 가장 짧은 과정의 단계 수를 구하라 -> bfs
# 한번에 한개 알파벳 바꿀 수 있다, words에 있는 단어로만 변환할 수 있다.
from collections import deque

def can_change(wordA, wordB):
    limit = 1
    for i in range(len(wordA)):
        if wordA[i] != wordB[i]:
            limit -= 1
            if limit < 0:
                return False
    return True

def solution(begin, target, words):
    visited = [0 for _ in range(len(words))]
    queue = deque([[begin,0]])
    while queue:
        now, cnt = queue.popleft()
        if now == target:
            return cnt
        else:
            for i in range(len(words)):
                if visited[i] == 0 and can_change(now, words[i]):
                    queue.append([words[i], cnt+1])
                    visited[i] = 1
    return 0

begin = "aab"
target = "aba"

words = ["abb", "aba"]
print(solution(begin, target, words))