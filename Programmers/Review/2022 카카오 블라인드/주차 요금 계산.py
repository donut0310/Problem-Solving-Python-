'''
기본 시간(분)	기본 요금(원)	단위 시간(분)	단위 요금(원)
180	5000	10	600
'''
from collections import defaultdict
import math

def check_time(enter, out):
    time_enter = list(map(int, enter.split(':')))
    time_out = list(map(int, out.split(':')))
    h = time_out[0] - time_enter[0]
    m = time_out[1] - time_enter[1]
    if m < 0: 
        m += 60
        h -= 1

    return h * 60 + m

def count_fee(time, fees):
    if time <= fees[0]:
        return fees[1]
    elif time > fees[0]:
        fee = fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]
        return fee

def solution(fees, records):
    answer = []
    parking_info = defaultdict(list)
    time_info = defaultdict(int)
    fee_info = []

    for record in records:
        tmp = record.split(' ')
        time, car_num = tmp[0], tmp[1]

        # 입차 기록이 없는 경우
        if not parking_info[car_num]:
            parking_info[car_num].append(time)
        # 입차 기록이 있는 경우
        else:
            time_info[car_num] += check_time(parking_info[car_num].pop(), time)
            print(car_num, time_info[car_num])
            print('---------------------------------')
    for car_num in parking_info.keys():
        if parking_info[car_num]:
            time_info[car_num] += check_time(parking_info[car_num].pop(), '23:59')

    for car_num, time in time_info.items():
        fee_info.append((car_num, count_fee(time, fees)))    
    
    fee_info.sort(key = lambda x: x[0])

    [answer.append(i[1]) for i in fee_info]        
    return answer

# print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
# [14600, 34400, 5000]

print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
# [0, 591]