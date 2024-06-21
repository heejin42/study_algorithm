def breakingRecords(scores):
    # Write your code here
    max_breaking = 0
    min_breaking = 0
    max_score = scores[0]
    min_score = scores[0]
    for score in scores:
        if score > max_score:
            max_breaking += 1
            max_score = score
        elif score < min_score:
            min_breaking += 1
            min_score = score
    return [max_breaking, min_breaking]

scores = [10,5,20,20,4,5,2,25,1]
print(breakingRecords(scores))