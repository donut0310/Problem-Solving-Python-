from itertools import permutations

def solution(k, dungeons):
    answer = -1
    _list = [i for i in range(len(dungeons))]
    c = list(permutations(_list, len(_list)))

    for order in c:
        tmp, cnt = k, 0
        for i in order:
            need, consume = dungeons[i][0], dungeons[i][1]

            if tmp < need: break
            tmp -= consume
            cnt += 1
        answer = max(answer, cnt)
    return answer

print(solution(80, [[80,20],[50,40],[30,10]])) # 3