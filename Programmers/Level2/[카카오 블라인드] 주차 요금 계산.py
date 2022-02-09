# fees => 기본시간, 기본요금, 단위시간, 단위요금
# records => 시간 차량번호 출차여부

# condition => 누적 주차 시간이 '기본시간' 이하라면 '기본요금'
#           => 누적 주차 시간이 '기본시간'을 초과하면, '기본요금'+'단위시간'당 '단위요금'
#           => 올림 연산
# !!exception => 입차 이후 출차 기록이 없다면 23:59 출차로 간주
# return => 차량 번호 작은 순으로 주차요금 배열 반환
from collections import defaultdict
import math 

def make_dict(records):
    park_info = defaultdict(list)
    for i in records:
        data = i.split(' ')
        park_info[data[1]].append((data[0],data[2]))
    return park_info

def count(fees,records):
    time = 0
    r_len = len(records)-1
    i=r_len
    while i>=0:
        out_time,in_time=[],[]
        if i==r_len and r_len%2==0:
            out_time=[23,59]
            in_time = list(map(int,records[i][0].split(':')))
            i+=1
        else:
            out_time = list(map(int,records[i][0].split(':')))
            in_time = list(map(int,records[i-1][0].split(':')))

        h_time = out_time[0]-in_time[0]
        m_time = out_time[1]-in_time[1]
        if m_time<0:
            h_time-=1
            m_time+=60   
        time += (60*h_time+m_time)
        i-=2
    fee = fees[1]
    if time>fees[0]:
        fee += math.ceil((time-fees[0])/fees[2])*fees[3]
    return fee
    
def solution(fees, records):
    answer = []
    park_fees=[]
    park_info = make_dict(records)
    for i in park_info:
        park_fees.append((i,count(fees,park_info[i])))# tuple
    park_fees.sort(key=lambda x:x[0])
    [answer.append(v)for i,v in park_fees]
    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10],["00:00 1234 IN"]))