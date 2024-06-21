def lcs(a, n, b, m):
    if n < 0 or m < 0:
        return 
    if a[n] == b[m]:
        print(answer)
        lcs(a, n-1, b, m-1, answer)
        answer.append(a[n])
        return 
    else: 
        l1 = lcs(a, n-1, b, m, answer)
        l2 = lcs(a, n, b, m-1, answer)
        if len(l1) >= len(l2):
            return l1
        else:        
            return l2
        
def longestCommonSubsequence(a, b):
    # Write your code here
    # 가장 긴 공통 순열 구하기
    # 현 위치 Xn == Ym인 경우 -> LCS(Xn, Ym) = LCS(Xn-1, Ym-1) + Xn
    # 현 위치 Xn != Ym인 경우 -> LCS(Xn, Ym) = max(LCS(Xn-1, Ym), LCS(Xn, Ym-1)
    answer = []
    lcs(a, len(a)-1, b, len(b)-1, answer)
    return answer    
    
a = [1,2,3,4,1] 
b = [3,4,1,2,1,3]
print(longestCommonSubsequence(a, b))