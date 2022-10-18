from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    time, last_entered_time = 0, 0
    entered_times = deque([])
    truck_weights = deque(truck_weights)
    
    while truck_weights:
        time += 1
        
        if len(entered_times): # 다리에 트럭이 있을 때, 맨 처음 들어온 트럭이 다리를 벗어날 시간이 된 경우
            w, t = entered_times[0]
            if t + bridge_length == time:
                weight += w
                entered_times.popleft()

        tw = truck_weights[0]
        if weight - tw >= 0:
            weight -= tw
            entered_times.append((tw, time))
            last_entered_time = time
            truck_weights.popleft()
                   
    answer = last_entered_time + bridge_length
    return answer

'''
## 앞서 지나간 트럭과는 관계없이 [마지막으로 지나간 트럭의 입장시간]만 알 수 있다면 전체 트럭이 지나간 최초의 시간을 알 수 있다. ##

1. 다리의 무게가 여유가 되면 트럭이 지나갈 수 있다.
    => 이때의 time 값을 마지막 트럭이 들어온 시간으로 체크한다.
    => 트럭이 다리에 처음 올라온 시간(time)과 해당 트럭의 무게를 튜플로 저장해 entered_times에 추가한다.
2. 매 반복문마다 entered_times을 체크해 맨 처음 들어온 트럭이 다리를 벗어날 시간이 된 경우를 체크하여 다리의 무게를 갱신한다.
3. 모든 트럭이 지나가고, 마지막 트럭이 들어온 시간 last_entered_time 값을 기준으로 다리의 길이를 더한다.

'''