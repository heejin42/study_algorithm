# 길이 k의 순열을 차근차근 만들어간다. ->

#from itertools import permutations

# def solution(k, a):
#     candidates = list(permutations([0,1,2,3,4,5,6,7,8,9], k+1))
#     candidates.sort()
#     for candidate in candidates[::-1]:
#         flag = True
#         for i in range(k):
#             check = str(candidate[i])+ a[i] + str(candidate[i+1])
#             if eval(check) == False:
#                 flag = False
#                 break
#         if flag:
#             print(*candidate, sep='')
#             break
#     for candidate in candidates:
#         flag = True
#         for i in range(k):
#             check = str(candidate[i])+ a[i] + str(candidate[i+1])
#             if eval(check) == False:
#                 flag = False
#                 break
#         if flag:
#             print(*candidate, sep='')
#             break
    
def check(a, b, s):
    if s == '>':
        return a>b
    else:
        return a<b    
    
def dfs_front(nums, used, i):
    global A
    global k
    global flag
    if i == k:
        print(*nums, sep='')
        flag = 1
        return

    for x in range(10):
        if flag:
            return
        if len(nums) == 0:
            nums.append(x)
            used[x] = 1
            dfs_front(nums, used, 0)
            used[x] = 0
            nums.pop()
        else:
            if used[x] == 0:
                if check(nums[-1], x, A[i]):
                    nums.append(x)
                    used[x] = 1
                    dfs_front(nums, used, i+1)
                    used[x] = 0
                    nums.pop()

def dfs_back(nums, used, i):
    global A
    global k
    global flag
    if i == k:
        print(*nums, sep='')
        flag = 1
        return

    for x in range(9, -1, -1):
        if flag:
            return
        if len(nums) == 0:
            nums.append(x)
            used[x] = 1
            dfs_back(nums, used, 0)
            used[x] = 0
            nums.pop()
        else:
            if used[x] == 0:
                if check(nums[-1], x, A[i]):
                    nums.append(x)
                    used[x] = 1
                    dfs_back(nums, used, i+1)
                    used[x] = 0
                    nums.pop()
            
    

k = int(input())
A = list(input().split(' '))
flag = 0
dfs_back([], [0,0,0,0,0,0,0,0,0,0,0], -1)
flag = 0
dfs_front([], [0,0,0,0,0,0,0,0,0,0,0], -1)