import heapq
from collections import deque

def solution(jobs):
    answer = 0
    divisor = len(jobs)
    jobs.sort(key=lambda x:(x[0], x[1]))
    pq = [] # 우선순위 큐
    heapq.heappush(pq, (jobs[0][1], jobs[0][0]))
    end_time = pq[0][1]
    jobs = deque(jobs[1:])

    while pq:
        work, req_time = heapq.heappop(pq)
        waitting_time = end_time - req_time
        answer += waitting_time + work
        end_time += work

        while jobs:
            req_time, work = jobs.popleft()
            if req_time <= end_time: # 마지막으로 작업이 완료된 시간보다 이전에 요청된 작업인 경우
                heapq.heappush(pq, (work, req_time))
            else:
                if not pq: # 하드디스크가 작업 중이 아닌 경우
                    heapq.heappush(pq, (work, req_time))
                    end_time = req_time
                else: jobs.appendleft((req_time, work))
                break

    return answer // divisor

print(solution([[0, 3], [1, 9], [2, 6], [30, 3]])) #7ms
print(solution([[0, 3], [1, 9], [2, 6]])) #9ms
print(solution([[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]])) # 13ms
