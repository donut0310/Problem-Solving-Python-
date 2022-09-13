def to_second(time):
    tmp = list(map(int, time.split(':')))
    result = tmp[0] * 3600 + tmp[1] * 60 + tmp[2]
    return result

def solution(play_time, adv_time, logs):
    answer = ''
    pt = to_second(play_time)
    at = to_second(adv_time)
    dp = [0] * (pt + 1)

    for log in logs:
        st, et = log.split('-')
        st = to_second(st)
        et = to_second(et)
        dp[st] += 1
        dp[et] -= 1

    for i in range(len(dp)):
        if i==0: continue
        dp[i] += dp[i-1]

    range_sum = sum(dp[:at])
    default_max = range_sum
    index = 0

    for i in range(1, pt - at + 1):
        range_sum = range_sum - dp[i-1] + dp[i+at-1]

        if range_sum > default_max:
            default_max = range_sum
            index = i

    answer = f'{index // 3600:0>2}:{index % 3600 // 60:0>2}:{index % 3600 % 60:0>2}'
    return answer

# print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
# "01:30:59" -> 5459

print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
# "01:00:00" -> 3600