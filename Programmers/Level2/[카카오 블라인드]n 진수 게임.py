def make(n,i,total,narray):
    arr = []
    if i<n:
        return [i]
    while i>=n:
        arr.append(i%n)
        i//=n
    arr.append(i)
    return arr[::-1]

def solution(n, t, m, p):
    answer = ''
    total = t * m
    dict = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

    narray = []
    i=0
    while 1:
        narray.extend(make(n,i,total,narray))
        if len(narray)>=total:
            break
        i+=1
    for index in range(p-1,len(narray[:total]),m):
        s = narray[index]
        if s>9:
            answer+=str(dict[s])
        else:
            answer+=str(narray[index])
    return answer
solution(2,4,2,1)
solution(16,16,2,1)
solution(16,16,2,2)



