from datetime import datetime

def solution(n, t, m, timetable):
    answer = ''
    # 1
    for i,v in enumerate(timetable):
        H,M = map(int,v.split(':'))
        timetable[i] = 60*H + M
    #2
    timetable.sort(reverse=True)
    
    #3
    bus_schedule = [540] # 09:00 to minute
    for i in range(n-1):
        bus_schedule.append(bus_schedule[-1] + t)

    #4
    chart = {}
    for time in bus_schedule:
        chart[time] = []
        cnt = 0 # 탈 수 있는 사람 수 카운트
        while cnt < m and len(timetable):
            tmp = timetable[-1]
            if tmp <= time:
                chart[time].append(timetable.pop())
                cnt+=1
            else: break

    #5
    con_schedule = []
    for key, value in chart.items():
        if len(value) < m:
            con_schedule.append(key)
        else:
            last_person = value[-1]
            con_schedule.append(last_person - 1)
    HH = con_schedule[-1] // 60
    MM = con_schedule[-1] % 60

    answer = str(datetime.strptime(f'{HH}:{MM}',"%H:%M"))[11:16]
    return answer


# print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"])) #09:00
# print(solution(2,10,2,["09:10", "09:09", "08:00"])) #09:09
# print(solution(2,10,2,["09:10", "09:08","09:09", "08:00"])) #09:08
# print(solution(10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", \
#     "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])) # 18:00
# print(solution(1,1,1,["23:59"])) # 09:00

'''
1. split timetable and calculate => 60*h+m
2. sort timetable by desc
3. n과 t를 이용해 버스가 오는 시간 계산 => 리스트로 구현 (bus_schedule)
4. bus_schedule, timetable 중첩반복문 => 버스 오는 시간내에 대기중인 사람들(chart) 리스트 딕셔너리에 추가
5. chart 키를 기준으로 반복문 => 콘이 버스에 탈 수 있으면 해당 버스 시간을 con_schedule 리스트에 추가
6. con_schedule 리스트의 마지막 원소의 시간 -1분을 hh:mm으로 포맷

'''