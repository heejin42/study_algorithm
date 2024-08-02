string = str(input())
target = str(input())
answer = 0
while target in string:
    x = string.rfind(target)
    string = string[:x]
    answer += 1
print(answer)