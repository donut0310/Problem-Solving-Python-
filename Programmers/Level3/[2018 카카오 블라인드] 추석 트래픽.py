def solution(lines):
    answer = 1
    for idx, time in enumerate(lines):
        s, t = time.split()[1:]
        s = s.split(':')
        s = round(int(s[0]) * 3600 + int(s[1]) * 60 + float(s[2]), 3)
        t = float(t[:-1])
        lines[idx] = [s, s - t]
    lines.sort(key=lambda t: t[0])   
         
    for i in range(len(lines)-1):
        std = lines[i][0]
        tmp = 1
        for start_time in lines[i+1:]:
            if std + 0.999 <= start_time[1]: continue
            tmp+=1
        if tmp>=answer: answer=tmp
    return answer

'''
응답완료시간 s를 시, 분, 초, 밀리초로 나눈 후 초단위로 환산한다.
처리시간 t를 실수형으로 변환한 뒤 응답완료시간에서 빼 응답 시작시간으로 환산한다.
lines 배열의 요소는 다음 포맷을 가진다. [응답 완료시간, 응답 시작시간]
lines 배열을 응답 완료시간 기준으로 정렬한다.
각 요소의 응답 완료시간부터 1초(시작 시간과 끝시간을 포함하기에 0.999초)를 더한 값의 범위 내에 
응답 시작시간이 존재하는 요소들은 같은 시간에 처리된 처리량을 뜻하기 때문에 tmp 값을 1 증가시켜준다.
'''

# print(solution([
# "2016-09-15 01:00:04.001 2.0s",
# "2016-09-15 01:00:07.000 2s"
# ])) # 1
# print(solution([
# "2016-09-15 01:00:04.002 2.0s",
# "2016-09-15 01:00:07.000 2s"
# ])) # 2
print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
])) # 7