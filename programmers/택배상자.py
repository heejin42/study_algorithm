# n개의 집이 있다. i(1~n)번째 집은 물류창고에서 i만큼 떨어져있다.
# 최대 cap개의 상자를 실을 수 있는 트럭으로 배달해야 하는 상자를 모두 배달하고 빈 상자는 수거하라.
# 최소 이동거리를 구하라
def solution(cap, n, deliveries, pickups):
    d_val, p_val = 0,0
    answer = 0
    for i in range(n):
        d_val += deliveries[n-i-1]
        p_val += pickups[n-i-1]
        while p_val > 0 or d_val > 0:
            d_val -= cap
            p_val -= cap
            answer += 2 * (n-i)
    return answer


cap = 4
n = 5
deliveries = [1,0,3,1,2]
pickups = [0,3,0,4,0]
print(solution(cap, n, deliveries, pickups))
