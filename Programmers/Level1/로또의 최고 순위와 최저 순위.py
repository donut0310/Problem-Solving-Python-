def highest(lottos, win_nums):
    cnt=0
    for i in lottos:
        if i==0 and len(win_nums)>0:
            cnt+=1
            win_nums.pop(0)
            continue
        for j in range(len(win_nums)):
            if i==win_nums[j]:
                cnt+=1
                win_nums.pop(j)
                break
    return cnt
def lowest(lottos, win_nums):
    cnt=0
    for i in lottos:
        if i==0:
            continue
        for j in range(len(win_nums)):
            if i==win_nums[j]:
                cnt+=1
                win_nums.pop(j)
                break
    return cnt
     
def solution(lottos, win_nums):
    answer = []
    obj = [6,6,5,4,3,2,1]
    lottos = sorted(lottos,reverse=True)

    h_cnt = highest(lottos, win_nums.copy())
    l_cnt = lowest(lottos, win_nums.copy())
    answer.append(obj[h_cnt])
    answer.append(obj[l_cnt])
    # print(answer)
    return answer

solution([44,1,0,0,31,25],[31,10,45,1,6,19])
solution([0,0,0,0,0,0],[38,19,20,40,15,25])
solution([45,4,35,20,3,9],[20,9,3,45,4,35])