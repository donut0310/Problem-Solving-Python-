def dfs(event, answer, cnt, ability, check):
    if event == len(ability[0]): # 모든 종목 검사
        answer = max(answer, cnt)
    else:
        for i in range(len(ability)):
            if check[i]: continue
            check[i] = 1
            answer = dfs(event + 1, answer, cnt + ability[i][event], ability, check)
            check[i] = 0 # 첫번째 종목이 다음 순서의 학생이 되어야 하기에 방문 체크를 초기화한다.
    return answer
        
def solution(ability):
    answer = 0
    event = 0 # 종목
    check = [0] * len(ability)
    answer = dfs(event, answer, 0, ability, check)

    return answer