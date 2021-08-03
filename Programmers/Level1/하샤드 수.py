def sumOfDigits(x):
    total = 0
    while x>0:
        total+=(x%10)
        x//=10
    return total

def isHarshard(total,x):
    if x % total == 0:
        return True
    else:
        return False
def solution(x):
    total = sumOfDigits(x)
    return isHarshard(total,x)

solution(10)
solution(12)
solution(11)
solution(13)