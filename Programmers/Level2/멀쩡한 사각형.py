def gcd(w,h):
    if h==0: return w
    else: return gcd(h,w%h)

def solution(w,h):
    return w*h-(w+h-gcd(w,h))

print(solution(8,12))

# 해설 참고 문제