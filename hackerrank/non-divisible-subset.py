# 부분 집합 중 요소 두개의 합이 k로 나눠 떨어지지 않는 가장 큰 집합
def nonDivisibleSubset(k, s):
    answer = 0
    sub_dic = {}
    for i in s:
        if (i%k) in sub_dic:
            sub_dic[i%k] += 1
        else:
            sub_dic[i%k] = 1
    check = []
    for key in sub_dic:
        remain = k - key
        if remain in check:
            continue
        if key == 0:
            check.append(key)
            answer += 1
            continue
        if key == remain:
            answer += 1
            check.append(key)
            continue
        if remain not in sub_dic:
            answer += sub_dic[key]
            continue
        if sub_dic[key] >= sub_dic[remain]:
            answer += sub_dic[key]
        else:
            answer += sub_dic[remain]
        check.append(key)
    print(answer)
            
    
if __name__ == '__main__':
    k = 4
    s = [1,2,3,4,5, 6, 7, 8, 9, 10]
    nonDivisibleSubset(k, s)
    
    