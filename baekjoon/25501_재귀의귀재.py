import sys
input = sys.stdin.readline

def solution(string):
    i = 0
    count = 1
    result = 1
    for i in range(len(string)//2):
        if string[i] == string[-i-1]:
            count += 1
            i += 1
        else:
            result = 0
            break
    
    print(result, count)  

n = int(input())
for _ in range(n):
    string = input().strip()
    solution(string)
    
    