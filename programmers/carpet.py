def solution(brown, yellow):
    candidates = [(yellow, 1)]
    for i in range(2, yellow//2+1):
        if yellow % i == 0:
            if i >= yellow//i:
                candidates.append((i, yellow//i))
    candidates = list(set(candidates))
    print(candidates)
    for candidate in candidates:
        wide = candidate[0] + 2
        height = candidate[1] + 2
        if wide*height == brown + yellow:
            return [wide, height]

brown = 24
yellow = 24
print(solution(brown, yellow))