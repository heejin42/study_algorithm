n = int(input())
count = n
check = 10
while True:
    if n // check > 0:
        count += (n-check+1)
        check *= 10
    else:
        break
print(count)