import sys
input = sys.stdin.readline
string = ''
n = int(input())
for i in range(n//4):
    string += 'long '
    
string += 'int'
print(string)
