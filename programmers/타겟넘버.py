def solution(numbers, target):
    # 순서는 그대로 더하기빼기 연산을 해서 target을 만들 수 있는 경우의 수를 구하라
    # 모든 경우 탐색 -> dfs -> stack 사용
    # stack에 무엇을 기록할 것인가? 계산한 위치, 현재 계산된 값
    answer = 0
    stack = [[numbers[0],1], [-numbers[0],1]]
    while stack:
        n, next = stack.pop()
        if next==len(numbers):
            if n == target:
                answer += 1
        else:
            stack.append([n+numbers[next], next+1])
            stack.append([n-numbers[next], next+1])
    return answer            

numbers= [4,1,2,1]
target = 4
print(solution(numbers, target))