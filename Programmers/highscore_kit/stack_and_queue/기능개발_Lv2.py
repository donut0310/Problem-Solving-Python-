from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    tasks = deque() # 작업별 남은 기간

    # 작업별 남은기간 계산    
    [tasks.append(math.ceil((100 - progresses[i]) / speeds[i])) for i in range(len(progresses))]

    tmp, cnt = 0, 1
    while tasks:
        task = tasks.popleft()
        if not tmp: # 첫번째 작업인 경우
            tmp = task
        elif task <= tmp: # 이전 작업보다 작업 완료가 빠른 작업
            cnt += 1
        elif task > tmp: # 이전 작업보다 작업 완료가 느린 작업
            tmp = task
            answer.append(cnt)
            cnt = 1

    answer.append(cnt) # 마지막 작업의 상태 추가
    return answer

# print(solution([93, 30, 55], [1, 30, 5])) # [2, 1]
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])) # [1, 3, 2]
print(solution([99, 99, 99, 90, 90, 90], [1,1,1,1,1,1])) # [3, 3]