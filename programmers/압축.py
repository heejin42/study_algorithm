# 무손실 압축 알고리즘 중 LZW(Lempel–Ziv–Welch) 압축
# 압축과정 길이가 1인 모든 단어를 포함하도록 사전 초기화 
# 현재의 입력과 일치하는 가장 긴 문자열을 찾는다.
# 그 문자열에 해당하는 사전의 색인번호를 출력하고 입력에서 지운다.
# 글자가 남아있다면 앞의 문자열과 글자를 연결해 사전에 등록한다. 

def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dic = {}
    for i in range(1, 27):
        dic[chr(i+64)] = i
    answer = []
    start, end = 0, 1
    while True:
        if end > len(msg):
            answer.append(dic[msg[start:end-1]])
            break
        s = msg[start:end]
        if s in dic:
            end += 1
        else:
            answer.append(dic[s[:-1]])
            dic[s] = len(dic) + 1
            start = end - 1 
    return answer

msg = 'TOBEORNOTTOBEORTOBEORNOT'
print(solution(msg))