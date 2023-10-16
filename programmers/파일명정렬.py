# 파일 정럴하기 
import re
def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))
    return [''.join(s) for s in sort]

files = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
print(solution(files))