import heapq

def solution(A, B):
    answer=0
    _A = [-i for i in A]
    _B = [-i for i in B]
    heapq.heapify(_A)
    heapq.heapify(_B)

    while _A:
        a = heapq.heappop(_A)
        b = heapq.heappop(_B)
        if -a<-b: answer+=1
        else: heapq.heappush(_B,b)  
    return answer

print(solution([5,1,3,7],[2,2,6,8])) # 3

'''
"B팀이 A팀을 상대로 얻는 최대 승점"
<풀이>
A,B 배열을 heapq를 이용해 최대힙을 만들어 준다.
각 반복마다 A,B 배열에서 루트를 뽑아 비교 후 A<B 인 경우 answer 값을 증가시킨다.
A>B인 경우에는 다시 힙에 넣고 최대힙을 만들어 준 뒤, 위 과정을 반복한다.
'''