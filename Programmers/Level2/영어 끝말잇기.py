from collections import defaultdict
def solution(n, words):
    dict = defaultdict(list)
    prev=''
    for i,w in enumerate(words):
        if i!=0 and w[0]!=prev:
            if (i+1)%n==0: return [n,(i+1)//n]
            else: return [(i+1)%n,(i+1)//n+1]            
        if w not in dict[w[0]]:
            dict[w[0]].append(w)
            prev = w[-1]
        else: 
            if (i+1)%n==0: return [n,(i+1)//n]
            else: return [(i+1)%n,(i+1)//n+1]
    return [0,0]
    
solution(2,['abc','cba','abc'])
solution(2,['abc','def'])