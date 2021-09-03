def solution(prices):
    answer = []

    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[i]>prices[j]:
                break
        answer.append(j-i) 
    return answer

solution([1,2,3,2,3])
solution([3,2,1,4,5])
solution([1,2,3,2,3,1])