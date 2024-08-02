n = str(input())
f = int(input())

base = n[:-2]
for i in range(100):
    if i < 10:
        x = base + '0' + str(i)
    else:
        x = base + str(i)
    if int(x)%f == 0:
        print(x[-2:])
        break   

