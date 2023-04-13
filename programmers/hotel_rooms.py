def solution(book_time):
    book_time.sort(key=lambda x : x[0], reverse = True)
    rooms = [book_time.pop()]
    while book_time:
        new_room = book_time.pop()
        flag = False
        for room in rooms:
            hours = int(new_room[0][:2]) - int(room[1][:2])
            minutes = int(new_room[0][3:]) - int(room[1][3:])
            time = hours * 60 + minutes
            if time >= 10:
                next = rooms.index(room)
                rooms[next] = new_room
                flag = True
                break
        if flag == False:
            rooms.append(new_room)
        rooms.sort(key=lambda x : x[1])
    answer = len(rooms)
    return answer


book_time = [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]
print(solution(book_time))