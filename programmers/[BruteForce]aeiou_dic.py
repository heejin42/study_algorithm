import itertools
def solution(word):
    length = len(word)
    words = []
    for i in range(1, 6):
        words += itertools.product(['A','E','I','O','U'], repeat = i)
    words.sort()
    answer = words.index(tuple(word)) + 1
    return answer

word = "AAAAE"
print(solution(word))