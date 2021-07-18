def solution(n, m):
    if n<=m: maxv = m
    else: maxv=n
    i=1
    g = 1
    l = maxv

    while(i<=maxv):
        if n%i==0 and m%i==0:
            l=i
        i+=1
    g = l*(n//l)*(m//l)
    answer = [l,g]
    return answer