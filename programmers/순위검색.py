def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
                
    for inf in info:
        i = inf.split(' ')
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))
    for k in data:
        data[k].sort()
        
    answer = []
    for q in query:
        q = q.split()
        scores = data[(q[0], q[2], q[4], q[6])]
        # 이분탐색, 기준 점수보다 낮은 경계를 찾아야 한다.
        score = int(q[7])
        l, r = 0, len(scores)
        while l < r:
            middle = (l+r)//2
            if scores[middle] < score:
                l = middle+1
            else:
                r = middle
        answer.append(len(scores)-l)
    return answer    
         
info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))