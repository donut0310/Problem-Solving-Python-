from collections import defaultdict,deque
import math

def count_time(enter,exit):
    enter = list(map(int,enter.split(':')))
    exit = list(map(int,exit.split(':')))
    h = exit[0]-enter[0]
    m = exit[1]-enter[1]
    if m<0:
        h-=1
        m+=60
    return h*60 + m

def solution(fees, records):
    answer, fees_info = [],[]
    cars = defaultdict(deque)

    #차량 입출 정보 기록
    for i in records:
        info = i.split(' ')
        cars[info[1]].appendleft(info[0])
    
    # 주차 요금 계산
    for i in cars.keys():
        time=0
        while cars[i]:
            enter = cars[i].pop()
            exit = "23:59"
            if len(cars[i]): # 마지막 기록이 출차인 경우
                exit = cars[i].pop()
            time += count_time(enter,exit) # 주차 시간 계산
        fee = fees[1] + math.ceil((time-fees[0])/fees[2])*fees[3] if time>fees[0] else fees[1]
        fees_info.append((i,fee))
    fees_info.sort(key=lambda x:x[0])
    [answer.append(i[1]) for i in fees_info]
    return answer

# print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# [14600, 34400, 5000]
# print(solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
# # [0, 591]
# print(solution([1, 461, 1, 10],["00:00 1234 IN"]))
# # [14841]

# key = 차량번호, value = (시각)을 값으로 가지는 cars={} 딕셔너리를 구성한다.
# value를 deque로 구성해 매 기록마다 appendleft로 입출 정보를 저장한다.
# 입->출 순서이므로 cars[차량번호].pop()으로 순서대로 enter(입차), exit(출차) 변수에 시각정보를 담는다.
# 입->출 정보는 짝수이므로 cars[차량번호]의 길이가 1인 경우 마지막 출차기록이 없기에 23:59의 출차 시각 정보를 갖는다.
# count_time 함수를 선언해 입출 시각의 차이를 계산한다.
# 해당 차량의 모든 주차시간 정보를 구한 후 요금을 부과한다.