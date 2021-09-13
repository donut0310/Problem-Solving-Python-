def solution(arr1, arr2):
    answer = [[]]

    for i in range(len(arr1)):
        arr = []
        for j in range(len(arr2[0])):
            s = 0
            for k in range(len(arr1[0])):
                s+=(arr1[i][k]*arr2[k][j])
            arr.append(s)
        answer.append(arr)
    answer = answer[1:]
    return answer

# solution([[1,4],[3,2],[4,1]],[[3,3],[3,3]])
# solution([[2,3,2],[4,2,4],[3,1,4]],[[5,4,3],[2,4,1],[3,1,1]])

# exception
solution([[1,2,3],[4,5,6]],[[1,4],[2,5],[3,6]]) 
# 14,32 32,77