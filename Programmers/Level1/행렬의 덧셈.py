def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arr = []
        for j in range(len(arr1[i])):
            arr.append(arr1[i][j]+arr2[i][j])
        answer.append(arr)
    return answer

solution([[1,2],[2,3]],[[3,4],[5,6]])
solution([[1],[2]],[[3],[4]])