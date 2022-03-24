def solution(cacheSize, cities):
    answer = 0
    queue = []
    if cacheSize==0: return 5*len(cities)
    for city in cities:
        if city.lower() not in queue: # cache miss
            if len(queue) == cacheSize: queue.pop(0)
            queue.append(city.lower())
            answer+=5
        else: # cache hit 
            queue.remove(city.lower())
            queue.append(city.lower())
            answer+=1 
    return answer

print(solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) #50
print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])) #21
print(solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) #60
print(solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])) #52
print(solution(2,["Jeju", "Pangyo", "NewYork", "newyork"])) #16
print(solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) #25

# LRU
# chache hit시 큐에 저장된 동일한 원소를 제거한 후 큐의 마지막에 삽입한다.
# chache miss시 큐의 첫번째 원소를 제거한 후 새로운 원소를 큐의 마지막에 삽입한다.
# deque를 사용하면 chache hit시 큐 내에 원소를 인덱스로 찾을 수 없기 때문에 list를 사용한다.