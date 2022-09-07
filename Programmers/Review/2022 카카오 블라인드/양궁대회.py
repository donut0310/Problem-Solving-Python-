SCORES = [] # 라이언이 어피치보다 잘 쏜 경우를 기록할 기록표
MAX_SCORE_GAP = 0 # 라이언이 더 잘 쏜 경우 어피치와의 점수 차

def dfs(n, info, player, score, p_arrow, index, cnt):
    global MAX_SCORE_GAP
    for arrow in p_arrow:
        a, r = player

        acc_arrow = cnt + arrow
        if acc_arrow > n: return # 화살 수 초과

        _score = score[::]
        _score[index] = arrow

        # 어피치와 라이언 점수 계산
        if info[index] < arrow:
            r += (10 - index)
        elif info[index] > 0 : a += (10 - index)

        next_index = index + 1
        if acc_arrow == n:
            for i in range(index + 1, 11): # 현재 점수판의 인덱스보다 뒤의 값에 어피치의 점수기록이 있다면, 점수 갱신을 해줘야한다.
                if info[i]: a += (10 - i)

            if a < r and r-a >= MAX_SCORE_GAP: # 어피치와의 총점 비교후 이긴 경우만 SCORES에 score 저장 후 리턴
                    MAX_SCORE_GAP = r-a
                    _score[index] = max(arrow, n - cnt)
                    tmp = ''.join(list(map(str,_score[::-1])))
                    SCORES.append((_score, r-a, tmp)) # 라이언의 기록표, 점수 차, 중복된 점수 차인 경우 기록표 비교를 위한 tmp 변수
        else:
            if next_index < 11:
                dfs(n, info, [a, r], _score, [0, info[next_index] + 1], next_index, acc_arrow)
            else: 
                if a < r and r-a >= MAX_SCORE_GAP: # 어피치와의 총점 비교후 이긴 경우만 SCORES에 score 저장 후 리턴
                    MAX_SCORE_GAP = r-a
                    _score[index] = max(arrow, n - cnt)
                    tmp = ''.join(list(map(str,_score[::-1])))
                    SCORES.append((_score, r-a, tmp))
    return

def solution(n, info):
    answer = []
    player = [0, 0]
    score = [0] * 11
    
    p_arrow = [0, info[0] + 1]
    dfs(n, info, player, score, p_arrow, 0, 0)

    if not len(SCORES): return [-1]

    SCORES.sort(key=lambda x:(x[1], x[2]))
    answer = SCORES[-1][0]
    return answer

# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0])) # [0,2,2,0,1,0,0,0,0,0,0]
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0])) # [-1]
# print(solution(9, [0,0,1,2,0,1,1,1,1,1,1])) # [1,1,2,0,1,2,2,0,0,0,0]
# print(solution(10, [0,0,0,0,0,0,0,0,3,4,3])) # [1,1,1,1,1,1,1,1,0,0,2]

# print(solution(3, [0,0,1,1,0,0,1,0,0,0,0]))

'''
<풀이>

라이언이 쏠 수 있는 화살을 [0발, 어피치의 기록 +1발] 총 두가지로 나눈다.

위 두가지의 경우의 수를 재귀호출을 통해 분기하며 모두 기록한다.

재귀 함수
1. 라이언이 쏜 화살이 n 보다 크다면, 해당 경우의 수는 불가능하므로 리턴
2. 라이언이 쏜 화살이 n 과 같다면, 어피치와 라이언의 점수 비교를 하여, 라이언이 더 높은 경우 리스트에 추가
3. 라이언이 쏜 화살이 n 보다 작다면, 재귀호출을 통해 다음 점수판의 기록을 비교한다.

'''