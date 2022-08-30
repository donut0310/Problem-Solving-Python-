import math

def solution(alp, cop, problems):
    '''
    알고력을 높이기 위해 알고리즘 공부를 합니다. 알고력 1을 높이기 위해서 1의 시간이 필요합니다.
    코딩력을 높이기 위해 코딩 공부를 합니다. 코딩력 1을 높이기 위해서 1의 시간이 필요합니다.
    현재 풀 수 있는 문제 중 하나를 풀어 알고력과 코딩력을 높입니다. 각 문제마다 문제를 풀면 올라가는 알고력과 코딩력이 정해져 있습니다.
    problems = [알고력, 코딩력, 증가 알고력, 증가 코딩력]
    '''

    alp_size, cop_size = 0, 0
    for problem in problems:
        alp_size = max(problem[0], alp_size)
        cop_size = max(problem[1], cop_size)

    alp = min(alp, alp_size)
    cop = min(cop, cop_size)

    dp = [[math.inf] * (500) for _ in range(500)]
    dp[alp][cop] = 0

    for i in range(alp, alp_size+1):
        for j in range(cop, cop_size+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp, next_cop = min(alp_size, i + alp_rwd), min(cop_size, j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)
    return dp[alp_size][cop_size]

print(solution(10, 10, [[10,15,2,1,2], [20,20,3,3,4]])) # 15
print(solution(0, 0, [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]])) # 13

'''
<풀이>

초기 알고력, 코딩력 -> 목표 알고력, 코딩력에 이르는 최단시간
DP를 이용한 풀이

[알고력과 코딩력을 올리는 방법]
방법 1. 각각의 알고리즘과, 코딩을 공부하여 알고력과 코딩력을 올리는 방법
방법 2. 문제 풀이를 통한 알고력과 코딩력을 올리는 방법

1. dp의 크기는 무한(적당히 큰 값)으로 설정한다. 실제 무한대로 계산 시 무한대 + a 범위의 경우 런타임 에러가 발생
2. 초기 알고력 ~ 목표 알고력 , 초기 코딩력 ~ 목표 코딩력에 이르는 범위 내에서 방법 1과 방법 2를 계산해 DP 값을 갱신한다.
3. 이때, 인덱스가 증감할 때마다 주어진 문제를 풀었을 경우의 값도 저장해야한다.
4. 요구하는 알고력과 코딩력이 현재 인덱스(현재 알고력과 코딩력)보다 작은 경우에만 문제를 풀 수 있기 때문에 if절로 분기한 후 DP 값을 갱신한다.
4-1. 문제를 풀었을 때, 알고력과 코딩력이 각각 목표치를 넘은 경우엔, dp[목표 알고력][목표 코딩력]의 값에 해당 값을 저장해준다.
    최종적으로 반환 값은 dp[목표 알고력][목표 코딩력]이 되어야 하기 때문에, 위 과정을 거치지 않는다면 값을 찾을 수 없다.
'''