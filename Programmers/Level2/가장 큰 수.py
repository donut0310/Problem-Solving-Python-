def solution(numbers):
    answer=''
    arr=[]
    for i in numbers:
        tmp=(str(i)*4)[:4]
        arr.append((i,tmp))
    arr=sorted(arr,key=lambda x:x[1],reverse=True)
    print(arr)
    for i in range(len(arr)):
        if i==0 and arr[i][0]==0:
            return '0'
        else: answer+=str(arr[i][0])
    return answer

print(solution([6,10,2]))
print(solution([3,30,34,5,9]))
print(solution([ 67,676,677]))
print(solution([0,0,0,0,0]))
print(solution([9,997,99,878,87]))
print(solution([1,10,100,1000]))

# 핵심 => numbers에 담긴 숫자를 각각 4번씩 반복한 수를 [:4]로 슬라이싱한다. => 0<=number<=1000이기 때문
# 첫번째 풀이때 numbers에 담긴 숫자를 key로 하고 슬라이싱한 수를 value로 하는 defaultdict(str)를 정렬 했으나 40점에 달했다 
# 이유는 겹치는 숫자인 경우 같은 key에 list value로 저장하지 않고 str value로 저장했기 때문에 이전 키에 저장된 값이 삭제되기 때문이라고 생각하여
# 이에 두번째 풀이때는 tuple => (numbers,sliced nubmer) 형식으로 저장후 정렬하니 정답 처리가 되었다.