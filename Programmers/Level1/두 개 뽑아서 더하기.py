def removeDuplicate(array):
    i=0
    newArray = []
    while(i<len(array)):
        if(i==0):
            newArray.append(array[i])
        elif(array[i]!=array[i-1]):
            newArray.append(array[i])
        i+=1
    return newArray

def pickAndAdd(numbers):
    i = 0 
    j = i+1
    array = []

    while(i<len(numbers)-1):
        array.append(numbers[i]+numbers[j])
        if(j==len(numbers)-1):
            i+=1
            j=i+1
        else: j+=1
    array = sorted(array)
    array = removeDuplicate(array)
    return array 

def solution(numbers):
    answer = []
    answer = pickAndAdd(numbers)
    return answer

solution([2,1,3,4,1])
solution([5,0,2,7])
