n = int(input())
array_n = list(input().split(' '))
array_n.sort()
m = int(input())
array_m = list(input().split(' '))

def binary(n, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if n == N[m]:
        return N[start:end+1].count(n)
    elif n < N[m]:
        return binary(n, N, start, m-1)
    else:
        return binary(n, N, m+1, end)

# 빠른 검색을 위해 dictionary 로 생성해놓기
n_dic = {}
for n in array_n:
    start = 0
    end = len(array_n) - 1
    if n not in n_dic:
        n_dic[n] = binary(n, array_n, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in array_m ))