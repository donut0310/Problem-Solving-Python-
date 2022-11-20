def solution(k, ranges):
    answer = []

    arr = [(0, k)]
    i = 1
    while k > 1: # 콜라츠 추측
        if k % 2 == 0: k //= 2
        else: k = k * 3 + 1
        arr.append((i, k))
        i += 1
    
    sum_arr = []
    # 정적분 계산 -> 해당 문제에선 구간의 사다리꼴 넓이
    for i in range(len(arr)):
        if i == 0: sum_arr.append(0)
        else:
            tmp = (arr[i-1][1] + arr[i][1]) / 2
            sum_arr.append(tmp)
    
    # 구간합 계산
    for i in range(1, len(sum_arr)):
        sum_arr[i] += sum_arr[i-1]

    # 정해진 범위의 넓이를 구간합을 이용해 계산
    length = len(sum_arr) - 1
    for x1, x2 in ranges:
        x2 += length
        if x1 > x2: answer.append(-1)
        else: answer.append(sum_arr[x2]-sum_arr[x1])

    return answer

print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]]))