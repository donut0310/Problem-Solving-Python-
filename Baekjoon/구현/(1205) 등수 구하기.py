import sys

input = sys.stdin.readline

n, new_score, p = map(int, input().split(' '))
rank_list = []
if n!=0: rank_list = list(map(int, input().split(' ')))

def solution():
   
    # 랭크 리스트에 점수가 없을 때 무조건 1등
    if not rank_list: return 1 

    # 랭크 리스트에 올라갈 수 없을 정도로 낮은 점수
    if len(rank_list) == p and new_score <= rank_list[-1]: return -1

    # 새 점수 삽입
    if len(rank_list) != p and new_score <= rank_list[-1]: rank_list.append(new_score)
    else:    
        size = len(rank_list)
        for i in range(size):
            if new_score >= rank_list[i]:
                if new_score == rank_list[i] and size == p: continue

                rank_list.insert(i, new_score)
                if len(rank_list) > p: rank_list.pop()
                break
        
    # 랭크 구하기
    answer, same = 0, 0
    for i in range(len(rank_list)):
        if i == 0: answer = 1
        else:
            if rank_list[i] == rank_list[i-1]: same += 1
            else: 
                answer += 1 + same
                same = 0
        if rank_list[i] == new_score: break
        
    return answer

print(solution())