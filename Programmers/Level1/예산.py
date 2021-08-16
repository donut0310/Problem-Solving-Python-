def solution(d, budget):
    answer = 0
    d = sorted(d)
    for i in d:
        if i>budget:
            break
        else:
            budget-=i
            if budget>=0:
                answer+=1
    return answer

solution([1,3,2,5,4],9)
solution([2,2,3,3],10)

# 1 2 3 4 5

