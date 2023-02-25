count_row = 0
array = []
max_count = 0
for i in range(5):
    s = input()
    array.append(list(s))
    count_row += 1
    if max_count < len(list(s)):
        max_count = len(list(s))
result = ''
for i in range(max_count):
    for j in range(len(array)):
        try:
            char = array[j][i]
            result += char
        except:
            pass
print(result)