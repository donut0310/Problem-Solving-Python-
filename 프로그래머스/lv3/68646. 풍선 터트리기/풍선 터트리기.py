def solution(a):
    answer = 0
    checking_arr = [[] for i in range(len(a))]
    
    for i in range(len(a)):
        if i == 0: checking_arr[i].append(a[i])
        else: checking_arr[i].append(min(a[i], checking_arr[i-1][0]))
    
    for i in range(len(a)-1, -1, -1):
        if i == len(a)-1: checking_arr[i].append(a[i])
        else: checking_arr[i].append(min(a[i], checking_arr[i+1][1]))
        
    for i in range(len(a)):
        left, right = checking_arr[i]
        if a[i] > left and a[i] > right: continue
        else: answer += 1
    
    return answer