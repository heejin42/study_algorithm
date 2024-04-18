def climbingLeaderboard(ranked, player):
    ranked = sorted(set(ranked), key=lambda x:-x)
    
    idx = len(ranked)-1
    result = []
    
    for p in player:
        while ranked[idx] <= p and idx >= 0:
            idx -= 1
        if idx < 0:
            result.append(1)
            continue
        result.append(idx+1+1) 
    return result


ranked = [100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 120]
print(climbingLeaderboard(ranked, player))