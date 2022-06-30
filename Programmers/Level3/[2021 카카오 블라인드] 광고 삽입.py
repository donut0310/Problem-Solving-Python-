def timeToSecond(time):
    return time[0] * 3600 + time[1] * 60 + time[2]

def solution(play_time, adv_time, logs):
    if play_time == adv_time: return "00:00:00"

    pt = timeToSecond(list(map(int,play_time.split(':')))) # 동영상 재생 시간
    at = timeToSecond(list(map(int,adv_time.split(':')))) # 광고 재생 시간
    dp = [0] * (pt+1)

    for log in logs:
        log = log.split('-')
        s = timeToSecond(list(map(int,log[0].split(':'))))
        e = timeToSecond(list(map(int,log[1].split(':'))))
        dp[s]+=1
        dp[e]-=1
        
    for i in range(1,len(dp)): # 전체 재생시간 동안의 누적 사용자 계산
        dp[i] += dp[i-1]

    default = sum(dp[:at]) # 동영상 재생시각이 0초일 때 광고 삽입시 구간합(사용자 누적시간)
    result = [(0,default)] # 각 구간마다 최대값이 되는 경우를 저장할 배열
    max_n = 0
    for i in range(1,pt-at+1):
        default = default-dp[i-1]+dp[i+at-1] # 구간합 갱신
        if default > max_n: # 최대값 갱신
            max_n = default
            result.append((i,max_n))
    result.sort(key=lambda x:(-x[1],x[0]))
    answer = result[0][0]
    answer = f'{answer//3600:02d}:{answer%3600//60:02d}:{answer%3600%60:02d}'
    return answer


# print(solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])) # "01:30:59"
# print(solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])) # "01:00:00"
# print(solution("50:00:00","50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])) # "00:00:00"
# print(solution("00:00:10" , "00:00:05",["00:00:08-00:00:10"])) TC 28

'''
<풀이>
* 1초마다 각 시각때의 누적시간을 구간합을 이용해 계산해 비교
1. 동영상 재생 시간과 광고 재생 시간을 초로 환산 => pt, at
2. dp 배열을 pt(동영상 재생 시간) +1의 크기로 선언해준다. 각 인덱스가 초를 의미하기 때문
3. 사용자 기록을 초로 환산해 dp 배열에 삽입한다.
3-1. 시작 시각은 +=1, 종료 시각은 -=1
3-2. ** 사용자의 시청 기록은 ~초 이상/미만으로 계산, 즉 0~10초 동안 시청이라면 0~9초까지만 시청으로 간주
4. dp배열을 순차적으로 더해준다. => 각 초마다 몇명의 시청자가 해당되는지 알 수 있음
5. pt-at+1 까지를 인덱스 범위로 반복문을 돌려, 각 인덱스별로 구간합을 계산한 후, 최대값이 되는 부분의 인덱스와 이때의 최대값을 result 배열에 저장
5-1. default(0초일 때 광고 재생 시간의 사용자 누적시간)을 매 초마다 갱신
5-2. 1초가 지나면, 현재 인덱스 -1 초의 값을 빼주고 현재 인덱스 + 광고 재생시간 -1의 값을 더해주면, 새로운 구간합을 알 수 있음
5-3. 새로 구하나 구간합이 max_n(최대값)보다 크다면 max_n을 갱신해주고, 이때의 인덱스와 max_n을 result배열에 삽입
6. result배열을 누적시간, 인덱스 순서로 내림차순 정렬하여, 첫번째 인덱스의 값이 정답이 된다.
'''