# 수가 주어졌을 때, 이진 트리로 해당 수 표현이 가능한지
# 이진트리가 수를 표현하는 방법은 더미 노드를 추가해서 포화 이진트리를 만든다. 
# 가장 왼쪽 노드부터 오른쪽 노드까지 살펴본다. 중위순회
# 더미인 경우 0, 아닌 경우 1 추가
# 불가능한 케이스는? 중간이 0이고 앞뒤 전체에 1이 있는 경우

def solution(numbers):
    
    def binary_search(start, end):
        if start >= end:
            return 1
        middle = (start+end+1)//2
        if binary_n[middle] == '0':
            if '1' in binary_n[start:end+1]:
                return 0
        else:
            if binary_search(start, middle-1) == 0 or binary_search(middle+1, end) == 0:
                return 0
        return 1
    
    answer = []    
    for n in numbers:
        binary_n = str(bin(n))[2:]
        i = 1
        while True:
            if len(binary_n) == 2**i-1:
                break
            elif len(binary_n) > 2**i-1:
                i += 1
            elif len(binary_n) < 2**i - 1:
                cnt = 2**i - 1 - len(binary_n) 
                binary_n = '0'*cnt + binary_n
                break
        answer.append(binary_search(0, len(binary_n)-1))
    return answer

numbers = [63, 111, 95]
print(solution(numbers))