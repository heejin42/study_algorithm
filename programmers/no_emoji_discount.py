def dfs(length):
    discount_list = []
    queue = [0.9] * length
    print(queue)
    
    return discount_list     
    
        
        
    
def solution(users, emoticons):
    candidates = [0.9, 0.8, 0.7, 0.6]
    
    discount_list = dfs(len(emoticons))
    print(discount_list)
    answer = []
    return answer

user = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
solution(user, emoticons)