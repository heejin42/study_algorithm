def solution(expression):
    # 수식의 우선순위에 따라 가장 큰 값을 찾는다.
    # 경우의 수를 구하고 계산하자.
    # 계산 법은 낮은 것부터 기준으로 쪼개기
    result = []
    cases = [['+', '-', '*'], ['+', '*', '-'], ['-', '+', '*'], ['-','*','+'], ['*','+','-'], ['*','-','+']]
    for case in cases:
        string1 = ''
        list1 = expression.split(case[0])
        for ex1 in list1:
            list2 = ex1.split(case[1])
            string2 = ''
            for ex2 in list2:
                num = eval(ex2)
                string2 += str(num)
                string2 += case[1]
            string2 = string2[:-1]
            num = eval(string2)
            string1 += str(num)
            string1 += case[0]
        string1 = string1[:-1]
        num = eval(string1)
        if num < 0:
            result.append(-num)
        else:
            result.append(num)
    answer = max(result)
    return answer

expression = "100-200*300-500+20"
print(solution(expression))