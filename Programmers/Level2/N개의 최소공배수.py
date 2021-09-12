def lcm(a,b):
    gcd = 0
    for i in range(1,min(a,b)+1):
        if a%i == 0 and b%i == 0:
            gcd = i
    lcm = (a//gcd) * (b//gcd) * gcd
    return lcm

def solution(arr):
    start = arr[0]

    if len(arr)==1:
        return arr[0]
    for i in range(1,len(arr)):
        start = lcm(start,arr[i])
    return start

solution([2,6,8,14])
solution([1,2,3])