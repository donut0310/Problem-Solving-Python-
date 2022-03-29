def is_seperated(place,p1,p2):
    # 수평선상 존재
    if p1[0]==p2[0]:
        if place[p1[0]][p1[1]+1] != 'X': return 0 # 칸막이가 없거나 붙어있는 경우
        return 1
    # 수직선상 존재
    if p1[1]==p2[1]:
        if place[p1[0]+1][p1[1]] != 'X': return 0 # 칸막이가 없거나 붙어있는 경우
        return 1
    # 대각선상 존재
    # p1이 p2의 좌상단에 위치하는 경우
    if p1[1]<p2[1]:
        if place[p1[0]][p1[1]+1] == 'X' and place[p1[0]+1][p1[1]] == 'X': return 1
        return 0
    # p1이 p2의 우상단에 위치하는 경우
    else:
        if place[p1[0]][p1[1]-1] == 'X' and place[p1[0]+1][p1[1]] == 'X': return 1
        return 0

def solution(places):
    answer = []
    # 대기실 별 응시자 위치 확인 후 거리두기 여부 확인
    for place in places:
        p_list = [] # 응시자 위치 저장 p_list = [(1,1),(2,2)...]
        for i in range(5):
            for j in range(5):
                if place[i][j]=='P': p_list.append((i,j))
    
        # 응시자간 거리두기 여부 확인
        # 응시자간 거리가 맨해튼거리 2 이하인 경우에 대해 조사 후 칸막이 여부 확인
        flag1=0 # 외부 반복문 탈출 조건
        for i in range(len(p_list)-1):
            flag2=0 # 내부 반복문 탈출 조건
            for j in range(i+1,len(p_list)):
                if abs(p_list[i][0]-p_list[j][0]) + abs(p_list[i][1]-p_list[j][1]) <= 2: #맨해튼 거리 2 이하인 경우
                    if not is_seperated(place,p_list[i],p_list[j]): # 칸막이가 없는 경우
                        flag2=1
                        break
            if flag2:
                flag1=1
                break
        if flag1: answer.append(0)
        else: answer.append(1)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]	))

# 각 대기실마다 응시자의 위치 정보를 p_list 배열에 담는다.
# 첫번째 응시자부터 본인 다음 순서의 응시자를 반복 비교한다.
# 두 응시자간의 맨해튼 거리가 2이하인 경우만 신경쓴다.
# 맨해튼 거리가 2이하 일때 칸막이의 여부를 확인한다.
# 두 응시자의 위치는 다음과 같다.
# p1의 행은 p2의 행보다 크거가 같다.
# p1의 열은 p2의 열보다 작거나 같거나 크다
# 두 응시자의 위치가 수직선상, 수평선상, 대각선상에 위치할 때로 나눠 칸막이의 여부를 확인한다.


