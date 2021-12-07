def solution(n, left, right):
    answer=[]
    for i in range(left,right+1):
        r=i//n
        c=i%n
        if r==0:
            answer.append(c+1)
        elif c==0:
            answer.append(r+1)
        elif r==c:
            answer.append(r+1)
        elif r!=c and r>c:
            answer.append(r+1)
        elif r!=c and r<c:
            answer.append(c+1)
    return answer

print(solution(3,2,5))
print(solution(4,7,14))
print(solution(2,1,3))