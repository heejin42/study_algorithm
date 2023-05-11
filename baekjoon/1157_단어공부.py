import sys
input = sys.stdin.readline

word = list(input().strip().upper())
count_alphabet = [0 for _ in range(26)]

for alphabet in word:
    n = ord(alphabet) - 65
    count_alphabet[n] += 1

x = max(count_alphabet)
if count_alphabet.count(x) > 1:
    print("?")
else:
    print(chr(count_alphabet.index(x) + 65))