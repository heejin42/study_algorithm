mushrooms = []
for _ in range(10):
    mushrooms.append(int(input()))
    
score = 0
i = 0
while i <= 9:
    score += mushrooms[i]
    if score == 100:
        break
    elif score > 100:
        if score-100 > 100-(score-mushrooms[i]):
            score -= mushrooms[i]
        break
    i += 1

print(score)