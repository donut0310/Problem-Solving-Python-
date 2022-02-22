import heapq

def solution(jobs):
    answer= 0
    heap=[]
    cnt_jobs = len(jobs)
    jobs.sort(key=lambda x:(x[0],x[1]))
    heapq.heappush(heap,(jobs[0][1],jobs.pop(0)))
    cur=heap[0][1][0]

    while heap:
        # 진행할 작업 추출
        job = heapq.heappop(heap)
        # 시간 계산
        waitting =  cur-job[1][0] # 현재시간 - 요청시간
        answer += (waitting + job[1][1]) # 대기시간 + 작업시간
        cur += job[1][1]

        while jobs:
            if jobs[0][0]<=cur: # 현재 시간 이전에 대기중인 작업들 큐에 삽입
                heapq.heappush(heap,(jobs[0][1],jobs.pop(0)))
            else: # 현재 시간 이전에 대기중인 작업이 없고 큐가 비어 있는 경우, 다음 작업 하나를 바로 가져온다.
                if len(heap)==0:
                    cur=(jobs[0][0])   
                    heapq.heappush(heap,(jobs[0][1],jobs.pop(0)))
                break
    return int(answer//cnt_jobs)

# print(solution([[0, 3], [1, 9], [2, 6]]	)) # 9ms
# print(solution([[0, 3], [2,6], [1,9]])) # 9ms
# print(solution([[0,3],[5,5],[7,3]])) # 4ms
# print(solution([[0, 10], [4, 10], [5, 11], [15, 2]])) # 15ms
# print(solution([[0, 3], [1, 9], [500, 6]])) # 6ms
# print(solution([[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]])) # 13ms
# print(solution([[0, 3], [1, 9], [2, 6], [30, 3]])) #7ms
# print(solution([[0, 1], [0, 1], [0, 1]])) #2ms
# print(solution([[1000, 1000]])) #1000ms
# print(solution([[24, 10], [28, 39], [43, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]])) # 72ms

# 시작 작업이 0에서 시작이 아닌 0 이상의 수에서 시작하는 경우를 생각하지 못해
# 현재 시간이 저장된 cur 변수의 초기화 과정에서 0으로 지정했다.
# 위 경우를 고려해 cur 변수의 초기화시 현재 우선순위큐에 삽입된 첫번째 작업의 요청시간+작업시간의 값으로 변경하였고
# 정답이 될 수 있었다.