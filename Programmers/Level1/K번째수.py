def sliceAndSort(array,commands,answer):
    array = array[commands[0]-1:commands[1]] # slice
    array = sorted(array) # sort
    answer.append(array[commands[2]-1]) 
    return answer

def solution(array,commands):
    answer=[]
    for i in commands:
        answer = (sliceAndSort(array,i,answer))
    return answer
solution([1,5,2,6,3,7,4],[[2,5,3],[4,4,1],[1,7,3]])