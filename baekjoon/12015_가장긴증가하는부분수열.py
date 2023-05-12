import sys
input = sys.stdin.readline

def find_place(sequence, num):
    start = 0
    end = len(sequence) - 1
    while start <= end:
        mid = (start + end) // 2
        if sequence[mid] == num:
            return mid 
        elif sequence[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return start
    
n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))
sequence = [arr[0]]
for num in arr[1:]:
    if num > sequence[-1]:
        sequence.append(num)
    else:
        i = find_place(sequence, num)
        sequence[i] = num
        
print(len(sequence))