def solution(cacheSize, cities):
    answer = 0
    cacheList = []

    if cacheSize==0:
        answer+=len(cities)*5
        return answer
    for i in cities:
        flag=0
        if len(cacheList)==0:
            cacheList.append(i.lower())
            answer+=5
        else:
            for index,cache in enumerate(cacheList):
                if i.lower()==cache: # hit
                    cacheList.append(cacheList.pop(index))
                    answer+=1
                    flag=1
                    break
            if flag==0: # miss
                answer+=5
                cacheList.append(i.lower())
                if (len(cacheList)>cacheSize):
                    cacheList.pop(0)
    return answer


solution(3,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])
solution(2,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
solution(5,["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
solution(2,["Jeju", "Pangyo", "NewYork", "newyork"])
solution(0,["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])