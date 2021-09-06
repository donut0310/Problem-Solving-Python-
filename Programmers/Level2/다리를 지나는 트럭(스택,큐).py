from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    in_bridge = deque([0 for n in range(bridge_length)])
    passed=[]

    trucks = len(truck_weights)
    while len(passed)<trucks:
        # 수용이 가능하면 in_bridge 추가
        # 매초마다 in_bridge에서 popleft
        # popleft한 값이 truck_weights에 있던 대기 트럭인 경우 passed에 append
        answer+=1
        truck = in_bridge.popleft()
        if truck != 0: 
            passed.append(truck)
            weight+=truck

        if len(truck_weights)!=0 and weight-truck_weights[0]>=0:
            truck = truck_weights.popleft()
            weight -= truck
            in_bridge.append(truck)
        else: in_bridge.append(0)
    return answer

solution(2,10,[7,4,5,6])
solution(100,100,[10])
solution(100,100,[10,10,10,10,10,10,10,10,10,10])