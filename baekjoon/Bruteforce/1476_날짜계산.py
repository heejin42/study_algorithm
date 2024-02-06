e,s,m = map(int, input().split(' '))
year = max(e,s,m)
if e == 15:
    e = 0
if s == 28:
    s = 0
if m == 19:
    m = 0
    
while True:
    if year%15 == e and year%28 == s and year%19 == m:
        break
    year += 1
print(year)