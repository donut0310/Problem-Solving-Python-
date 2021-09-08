def solution(n):
    total, answer = 0, 0 
    for i in range(1,n):
        total+=i
        for j in range(i+1,n):
            total+=j
            if total>n:
                break
            if total == n:
                answer+=1
                break
        total = 0
    return answer+1
solution(15)