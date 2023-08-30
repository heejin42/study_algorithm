def solution(record):
    answer = []
    dic = {}
    
    for sentence in record:
        sentence_split = sentence.split()
        if len(sentence_split) == 3:
            dic[sentence_split[1]] = sentence_split[2]
            
    for sentence in record:
        sentence_split = sentence.split()
        if sentence_split[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' %dic[sentence_split[1]])
        elif sentence_split[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' %dic[sentence_split[1]])
            
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))