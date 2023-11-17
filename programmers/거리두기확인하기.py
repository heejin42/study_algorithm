# 대기실은 5x5 크기 5개
# 거리두기를 위해 맨해튼거리 2 이하로 앉지 말 것 [x1-x2] + [y1-y2]
# 그러나 파티션이 사이에 있으면 괜찮음
# Places = P(응시자), O(빈테이블), X(파티션)
# 5개 대기실 각각 거리두기 준수여부를 배열에 담아 리턴한다. 지키면 1, 아니면 0

def solution(places):
    result = []
    # (x,y)에 있다면, 확인할 자리
    # (x+2, y), (x-2, y), (x,y+2), (x,y-2)
    # (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)
    # (x+1, y), (x-1, y), (x,y-1), (x,y+1)
    for place in places:
        answer = 1
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    # 바로 옆 체크
                    for dx,dy in [[1,0], [-1,0], [0,-1], [0,1]]:
                        if 0<=i+dy<5 and 0<=j+dx<5 and place[i+dy][j+dx] == 'P':
                            answer = 0
                            break
                    # 사선 체크
                    for dx,dy in [[1,1], [1,-1], [-1,1], [-1,-1]]:
                        if 0<=i+dy<5 and 0<=j+dx<5 and place[i+dy][j+dx] == 'P':
                            if place[i+dy][j] == 'X' and place[i][j+dx] == 'X':
                                continue
                            else:
                                answer = 0
                                break
                    # 한 칸 건너 체크
                    for dx,dy in [[2,0], [-2,0], [0,2], [0,-2]]:
                        if 0<=i+dy<5 and 0<=j+dx<5 and place[i+dy][j+dx] == 'P':
                            if place[(2*i+dy)//2][(2*j+dx)//2] == 'X':
                                continue
                            else:
                                answer = 0
                                break
                if answer == 0:
                    break
            if answer == 0:
                break
        result.append(answer)
    return result

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))