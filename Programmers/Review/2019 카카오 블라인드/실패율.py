from collections import defaultdict

def solution(N, stages):
    answer = []
    stage_dict = defaultdict(int)

    for stage in stages:
        stage_dict[stage] += 1
    
    player = len(stages)
    result = []
    for i in range(1, N+1):
        if not player:
            result.append((i, 0))
            continue
        stage_player = stage_dict[i]
        result.append((i, stage_player / player))
        player -= stage_player

    result.sort(key=lambda x:(-x[1], x[0]))
    print(result)
    [answer.append(i[0]) for i in result]
    return answer

# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]	)) # [3,4,2,1,5]
print(solution(5, [1,2,2,3,3,3]))
