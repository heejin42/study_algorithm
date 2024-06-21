def shortPalindrome(s):
    mod = 1000000007
    # Write your code here
    dp1 = [0 for _ in range(26)] # dp1[x] : s='x'의 경우의 수
    dp2 = [[0 for _ in range(26)] for _ in range(26)] # dp[x][y]: s='xy'의 경우의 수
    dp3 = [[0 for _ in range(26)] for _ in range(26)] # s="xyy"의 경우의 수
    dp4 = [0 for _ in range(26)] # dp4[x]: s='x,,x'의 경우의 수
    
    for char in s:
        x = ord(char) - ord('a')
        for i in range(26):
            if dp3[x][i] != 0:
                dp4[x] += dp3[x][i]
            if dp2[i][x] != 0:
                dp3[i][x] += dp2[i][x]
            if dp1[i] != 0:
                dp2[i][x] += dp1[i]
        dp1[x] += 1
    return sum(dp4) % mod
s = 'kkkkkkc'
print(shortPalindrome(s))