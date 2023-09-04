def minion_game(string):
    # kevin and stuart game do this with string S
    # stuart start with consonants (자음)
    # kevin start with vowels (모음-aeiou)
    # make all possible substirngs
    # each substrings have point
    # them, output is the total score and winner info
    # example Stuart 12
    length = len(string)
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    score_k = 0
    score_s = 0
    for i in range(len(string)):
        x = string[i]
        if x in vowels:a
            score_k += length - i 
        else:
            score_s += length - i
            
    if score_k > score_s:
        result = "Kevin " + str(score_k)
    elif score_k < score_s:
        result = "Stuart " + str(score_s)
    else:
        result = "Draw"
    return result
 
string = 'BANANA'
print(minion_game(string))    
     