from collections import defaultdict
## solution(1) => 효율성 시간초과, double linked list
# def solution(stones,k):
#     answer = 0
#     dict = defaultdict(list)
#     for i in range(len(stones)+2):
#         if i==0: dict[i]=[0,1,0]
#         elif i==len(stones)+1: dict[i]=[i-1,0,0]
#         else: dict[i]=[i-1,i+1,stones[i-1]] # [prev,next,value]    
    
#     # 징검다리 건너기
#     while True:
#         q=[0] # 시작점
#         while q:
#             cur=q[-1] # 현재 발판
#             prev,next = dict[cur][0],dict[cur][1] # 이전 발판, 다음 발판
#             if next-cur > k: return answer # 징검다리를 건널 수 없는 겨웅
#             if not cur: # 시작점인 경우 => 발판이 아님!
#                 q.pop()
#                 q.append(next)
#             else:
#                 if dict[cur][1]==len(stones)+1: # 도착
#                     answer+=1
#                     break
#                 dict[cur][2]-=1 #발판 숫자 감소
#                 if not dict[cur][2]: # 발판이 사라진 경우 이전 발판과 다음 발판을 연결
#                     dict[prev][1]=dict[cur][1]
#                     dict[next][0]=dict[cur][0]
#                 q.append(dict[cur][1])

## solution2 => 이분 탐색
def solution(stones,k):
    answer=0
    left,right=1,max(stones)
    while left<=right:
        mid = (left+right)//2
        cnt=0
        for stone in stones:
            if stone<=mid: cnt+=1
            else: cnt=0
            if cnt==k:
                right=mid-1
                answer=mid
                break
        if cnt<k: left=mid+1
    return answer
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))

'''
<풀이>
문제 조건 특성상 징검다리의 숫자는 통과할 수 있는 사람의 수를 나타낸다.
따라서 최소 1명 ~ 최대 max(stones)만큼 통과할 수 있다.
1. 이분탐색의 left, right 선언: left = 최소인원 1, right = 최대인원 max(stones)
2. for loop를 사용해 각 디딤돌마다 mid(통과할 사람) 보다 큰지 검사한다.
2-1. mid보다 작거나 같다면 결국 0이 될 디딤돌이기에 연속된 0 크기의 디딤돌의 개수를 카운팅한다.
2-2. 연속된 0 크기의 디딤돌이 k개와 같아진다면 더이상 건널 수 없기에 right값을 mid-1로 변경한다.
3-1. 연속된 0 크기의 값 cnt가 k보다 작다면 더 많은 사람들이 건널 수 있음을 의미하기에 left를 mid+1로 변경한다.
'''