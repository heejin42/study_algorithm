def solution(cards):
    # cards를 연달아 열어가서 2개의 가장 큰 집합을 만드는 경우를 구하는 문제
    # 집합 구하기
    visited = [0 for _ in range(len(cards)+1)]
    answer = []
    for i in range(1, len(cards)+1):
        card = cards[i-1]
        boxes = 0
        while visited[card]==0: 
            boxes += 1
            visited[card] = 1
            card = cards[card-1]
        answer.append(boxes)
    if len(answer) == 1:
        return 0
    else:
        answer.sort()
        return answer[-1] * answer[-2]
    

cards = [8,6,3,7,2,5,1,4]
print(solution(cards))