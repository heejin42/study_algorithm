def get_section_average(scores, a, b):
    answer = sum(scores[a:b+1]) / (b-a+1)
    print("{:.2f}".format(answer))


n, k = map(int, input().split(' '))
scores = list(map(int, input().split(' ')))
for _ in range(k):
    a, b = map(int, input().split(' '))
    get_section_average(scores, a-1, b-1)
    