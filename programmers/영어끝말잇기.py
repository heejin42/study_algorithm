def solution(n, words):
    answer = [0 for _ in range(n)]
    dic = []
    for i in range(len(words)):
        num = i%n
        answer[num] += 1
        word = words[i]
        if word in dic:
            return [num+1, answer[num]]
        else:
            dic.append(word)
            if i == 0: 
                continue
            elif words[i-1][-1] != word[0]:
                return [num+1, answer[num]]
    return [0, 0]
            
        

n = 5
words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
print(solution(n, words))