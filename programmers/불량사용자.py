from itertools import permutations
def check(id, target):
    if len(id)!= len(target):
        return False
    for i in range(len(id)):
        if target[i] == '*':
            continue
        else:
            if target[i] != id[i]:
                return False
    return True

def solution(user_id, banned_id):
    perms = list(permutations(user_id, len(banned_id)))
    result = []
    for perm in perms:
        flag = 0
        for i in range(len(banned_id)):
            if check(perm[i], banned_id[i]) == False:
                flag = 1
                break
        perm = set(perm)    
        if flag == 0 and perm not in result:
            result.append(set(perm))
    return len(result)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

print(solution(user_id, banned_id))