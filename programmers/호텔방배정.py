# 1-k번까지의 방이 있고 투숙객은 신청한 순서대로 방을 배정한다.
# 원하는 방이 비어있으면 배정하고, 아니면 번호가 큰 방 중 제일 작은 비어있는 방을 배정한다.
# 배정되는 방 번호를 순서대로 담아 리턴할 것
# 주의할 점, 1<=k<10**12, 고객 수 또한 1 이상 200,000 이하로 매우 크다.
def solution(k, room_number):
    answer = []
    room = {}
    for num in room_number:
        number = room.get(num, 0)
        if number :
            temp = [num]
            while True:
                index = number
                number = room.get(number, 0)
                if not number:
                    answer.append(index)
                    room[index] = index + 1
                    for i in temp:
                        room[i] = index + 1
                    break
                temp.append(number)

        else:
            answer.append(num)
            room[num] = num + 1
    return answer


k = 10
room_number = [1,3,4,1,3,1]
print(solution(k,room_number))