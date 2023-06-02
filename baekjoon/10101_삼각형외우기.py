import sys
input = sys.stdin.readline
angle = []
for _ in range(3):
    angle.append(int(input()))
    
if sum(angle) != 180:
    print("Error")
else:
    if len(set(angle)) == 2:
        print("Isosceles")
    elif len(set(angle)) == 3:
        print("Scalene")
    if len(set(angle)) == 1:
        print("Equilateral")