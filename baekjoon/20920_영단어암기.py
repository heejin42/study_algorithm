import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split(' '))
word_book = {}
for _ in range(n):
    word = input().strip()
    if len(word) < m:
        continue
    else:
        if word in word_book:
            word_book[word][0] += 1 
        else:
            word_book[word] = [1, len(word)]

word_book = sorted(word_book.items(), key = lambda item : [-item[1][0], -item[1][1], item[0]])
for word in word_book:
    print(word[0])           