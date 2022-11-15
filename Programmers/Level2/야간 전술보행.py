def solution(distance, scope, times):
    answer = 10000001
    for i in range(len(scope)):
        scope[i] = sorted(scope[i])

    for i in range(len(scope)):
        s, e = scope[i] # 근무 지역의 범위
        w, b = times[i] # 근무 시간, 휴식 시간
        total = w + b

        for time in range(s, e+1):
            if 0 < time % total <= w: # 발각
                answer = min(answer, time)
                break

    answer = min(answer, distance)
    return answer

print(solution(10, [[3, 4], [5, 8]], [[2, 5], [4, 3]])) # 8
print(solution(12, [[7, 8], [4, 6], [11, 10]], [[2, 2], [2, 4], [3, 3]])) # 12

'''
<풀이>
1. 화랑이는 1ms의 속도로 직진하기 때문에 distance배열의 각 칸은 초로 치환할 수 있다.
2. 각 경비병의 근무 지역(정렬되지 않을 수 있기 때문에 정렬을 미리 진행)이 언제 근무 시간에 해당하는지를 계산한다.
    근무 시간 => 0 < 현재 시간(== 근무 지역의 위치) % (근무시간 + 휴식시간) <= 근무 시간
3. 화랑이의 위치가 위에서 구한 근무 시간에 포함된다면 현재 위치까지의 이동이 최소거리가 된다.
    scope는 정렬되지 않은 상태기 때문에 3번에 해당할 때마다 기존의 최소거리와 비교해 최소거리를 갱신한다.
'''