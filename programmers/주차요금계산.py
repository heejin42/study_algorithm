import math

def solution(fees, records):
    # 차량번호가 작은 순부터 주차요금 계산하여 라턴하기
    # 나누어 떨어지지 않으면 올림
    base_t, base_f, unit_t, unit_f = fees
    max_t = 23*60 + 59
    new_records = []
    for record in records:
        t, n, f = record.split(' ')
        time = int(t[:2]) * 60 + int(t[3:])
        new_records.append([int(n), time, f])
    new_records.sort()
    
    result = []
    time = 0
    for i in range(len(new_records)):
        if i == len(new_records) - 1:
            if new_records[i][2] == 'IN':
                time += (max_t - new_records[i][1])
            if time <= base_t:
                fee = base_f
            else:
                fee = (base_f+math.ceil((time-base_t)/unit_t)*unit_f)
            result.append(fee)
            break
            
        if new_records[i][0] == new_records[i+1][0]:
            if new_records[i][2]=='IN':
                time += (new_records[i+1][1] - new_records[i][1])
        else:
            if new_records[i][2] == 'IN':
                time += (max_t - new_records[i][1])
            if time <= base_t:
                fee = base_f
            else:
                fee = (base_f+math.ceil((time-base_t)/unit_t)*unit_f)
            result.append(fee)
            time = 0
    return result

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))