# 10000보다 작거나 같은 셀프 넘버를 출력하라.
# 여기서 셀프 넘버란? 다른 것에서 만들어질 수 없는 숫자.

num_list = [i for i in range(10001)]
answer = [i for i in range(10001)]
while num_list:
    num = num_list.pop()
    to_add = 0
    for s in str(num):
        to_add += int(s)
    created_num = num + to_add
    if created_num in answer:
        answer.remove(created_num)

for n in answer:
    print(n)