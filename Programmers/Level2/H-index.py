def solution(citations):
    answer = 0
    citations=sorted(citations,reverse=True)

    for i in range(max(citations),0,-1):
        cnt=0
        for j in citations:
            if cnt>=i: break
            elif j>=i:
                cnt+=1
            else: break
        if cnt>=i:
            answer=cnt
            break
    return answer

solution([0,1,1])