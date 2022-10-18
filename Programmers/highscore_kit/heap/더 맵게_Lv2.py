import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        if first >= K: return answer
        second = heapq.heappop(scoville)
        new_one = first + (second * 2)
        heapq.heappush(scoville, new_one)
        answer += 1

    if scoville[0] >= K: return answer
    return -1
    