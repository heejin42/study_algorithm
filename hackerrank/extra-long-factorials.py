def extraLongFactorials(n):
    answer = 1
    for i in range(2, n+1):
        answer *= i
    
    print(answer)

if __name__ == '__main__':
    n = int(input().strip())
    extraLongFactorials(n)
