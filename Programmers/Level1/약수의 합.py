def devide(n):
    i=1
    total = 0
    while(n>=i):
        if n%i==0:
            total+=i
        i+=1
    return total
def solution(n):
    return devide(n)

solution(12)
solution(5)