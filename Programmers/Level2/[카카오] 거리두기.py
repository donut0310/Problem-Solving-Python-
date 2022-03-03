def m_d(p1,p2):
    # 맨해튼 거리
    d = abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
    if d<=2: return 1
    return 0

def check(places,i,p1,p2):
    # 거리두기 유지 여부
    ud,lr=0,0
    if p1[0]<p2[0]: ud=1
    elif p1[0]>p2[0]: ud=-1
    if p1[1]<p2[1]: lr=1
    elif p1[1]>p2[1]: lr=-1
    # 두 응시자가 직선상에 위치하는 경우 => 두 응시자 사이에 파티션이 존재하는지 확인
    if p1[0]==p2[0]: # 같은 행
        # 바로 옆자리
        if p1[1]+1==p2[1] or p1[1]-1==p2[1]:
            return 0
        if places[i][p1[0]][p1[1]+lr] == 'X':
            return 1
    if p1[1]==p2[1]: # 같은 열
        if p1[0]+1==p2[0] or p1[0]-1==p2[0]:
            return 0
        if places[i][p1[0]+ud][p1[1]] == 'X':
            return 1   

    # 두 응시자가 대각선에 위치하는 경우 => 남은 대각 자리에 빈테이블이 있는지 여부 확인
    if places[i][p1[0]+ud][p1[1]] == 'O': return 0
    if places[i][p1[0]][p1[1]+lr] == 'O': return 0
    return 1

def verify_distance(places,i,p_list,p_len):
    for j in range(p_len):
        for k in range(j+1,p_len):
            if m_d(p_list[j],p_list[k]): # 맨해튼 거리가 2이하인 경우
                if not check(places,i,p_list[j],p_list[k]): # 거리두기 유지 여부
                    return 0
    return 1

def solution(places):
    answer = []
    # 응시자 위치 확인
    p_list = []
    for i in range(len(places)):
        p=[]
        for j in range(5):
            for k in range(5):
                if places[i][j][k]=='P':
                    p.append((j,k))            
        p_list.append(p)

    for i in range(len(p_list)):
        p_len=len(p_list[i])
        if not p_len:
            answer.append(1)
            continue
        if not verify_distance(places,i,p_list[i],p_len):
            answer.append(0)
            continue
        answer.append(1)
    return answer

# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
# print(solution([['PXOOO','XPOOO','XXXXX','XXXXX','XXXXX']])) #[1]
# print(solution([['POPOO','XXXXX','XXXXX','XXXXX','XXXXX']])) #[0]
# print(solution([['PXXXX','XPPXX','XXXXX','XXXXX','XXXXX','XXXXX']])) #[0]
# print(solution([['PXXXX','XPOXX','XXPXX','XXXXX','XXXXX']])) #[0]
# print(solution([['OPXXX','PXXXX','XXXXX','XXXXX','XXXXX']])) #[0]
print(solution([["OOPOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"]] )) #[0]