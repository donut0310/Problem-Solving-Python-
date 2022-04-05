def solution(people, limit):
    answer,tmp = 0,0
    people.sort(reverse=True)
    
    i,j=0,len(people)-1
    while i<j:
        if not tmp:
            if people[i]+people[j]<=limit:
                tmp=people[i]+people[j]
                j-=1
            else:
                answer+=1
                i+=1
        else:
            if tmp+people[j]<=limit:
                tmp+=people[j]
                j-=1
            else:
                tmp=0
                answer+=1
                i+=1
    return answer+1

print(solution([70,50,80,50],100))
print(solution([70,80,50],100))

'''
풀이
1. people 배열을 크기순 역정렬을 한다.
2. 몸무게가 가장 큰 사람과 가장 작은 사람끼리 짝을 지어 limit값과 비교한다.
3. 두 사람의 무게 합이 limit보다 작거나 같은 경우 같은 보트에 타게 되고 이후 다음번째로 가장 작은사람(j)의 몸무게를 더한다.
4. 이때 무게 합이 limit을 넘어간다면 보트에 태울 수 없기에 answer값을 1 증가 시킨 후 다음번째로 가장 무거운사람(i) 와 j의 무게를 더하며 위의 과정을 반복한다.
'''