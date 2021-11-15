import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0]<K:
        if len(scoville)==1:break
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville,a+b*2)
        answer+=1
    for i in scoville:
        if i<K:
            return -1
    if answer==0: return -1
    return answer

# print(solution([1, 2, 3, 9, 10, 12],7))
# print(solution([6,1],7))
# print(solution([1,2,3],11))
# print(solution([0,0,0,0],11)) #반례
# print(solution([1,2],11))