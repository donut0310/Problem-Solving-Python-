def isEven(num):
    if num%2==0: return True
    else: return False

def match(num):
    if isEven(num): return num//2
    else: return (num+1)//2

def solution(n,a,b):
    ans=0
    while n>2:
        if(abs(a-b)) == 1:
            if (b<a and (not isEven(b))) or (a<b and (not isEven(a))):
                break
        a=match(a)
        b=match(b)  
        ans+=1
        n//=2     
    return ans+1

solution(8,4,7)
