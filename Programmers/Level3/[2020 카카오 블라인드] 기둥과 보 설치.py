def double_panel_check(x,y,panel):
    '''
    선택된 좌표의 보의 양쪽에 연결된 보들이 있는지 검사
    '''
    if panel[x-1][y] and panel[x+1][y]: return True
    return False

def verifying_install_pillar(x,y,pillar,panel):
    '''
    <조건>
    1. 바닥이면 설치 가능 -> y 좌표 0
    2. 바닥이 아닌 경우 보 위거나 기둥 위면 설치 가능, 전자의 경우 보는 시작점을 기준으로 두 개를 확인해야함
    '''
    if y==0: return True # 1
    elif panel[x-1][y] or panel[x][y] or pillar[x][y-1]: return True # 2
    return False

def verifying_delete_pillar(x,y,pillar,panel):
    '''
    <조건>
    기둥을 삭제했을 때 기둥이 받치고 있던 보가 두 개라면, 두 개의 보 모두 검사해야 함
    기둥을 삭제했을 때, 기둥이 받치고 있던 기둥이 존재한다면 해당 기둥을 검사해야 함
    * 배열의 0번째, 1번째, n-2번째 n-1번째(마지막 인덱스) 와 2~n-3번째 인덱스, 총 5가지의 구간을 나눠 각각의 경우에 연관된 모든 기둥과 보들을 검사해야 함
    '''
    if x==0: # 삭제할 기둥이 x축의 시작점인 경우
        if pillar[x][y+1] and not panel[x][y+1]: return False # 삭제할 기둥 위에 기둥이 존재하는데 보로 받쳐져 있지않은 경우
        if panel[x][y+1] and not pillar[x+1][y]: return False # 삭제할 기둥 위에 보가 존재하는데 보의 끝점이 기둥으로 받쳐져 있지않은 경우
    elif x==1: 
        if pillar[x][y+1] and not panel[x-1][y+1] and not panel[x][y+1]: return False
        if panel[x-1][y+1] and not pillar[x-1][y]: return False
        if panel[x][y+1] and not double_panel_check(x,y+1,panel) and not pillar[x+1][y]: return False
    elif x==len(pillar)-2:
        if pillar[x][y+1] and not panel[x-1][y+1] and not panel[x][y+1]: return False    
        if panel[x][y+1] and not pillar[x+1][y]: return False
        if panel[x-1][y+1] and not double_panel_check(x-1,y+1,panel) and not pillar[x-1][y]: return False
    elif x==len(pillar)-1: # 삭제할 기둥이 x축의 끝점인 경우
        if pillar[x][y+1] and not panel[x-1][y+1]: return False # 삭제할 기둥 위에 기둥이 존재하는데 보로 받쳐져 있지않은 경우
        if panel[x-1][y+1] and not pillar[x-1][y]: return False # 삭제할 기둥 위에 왼쪽에서 시작된 보가 존재하는데 보의 시작점이 기둥으로 받쳐져 있지않은 경우
    else:
        if pillar[x][y+1] and not panel[x-1][y+1] and not panel[x][y+1]: return False
        if panel[x-1][y+1]:
            if not double_panel_check(x-1,y+1,panel) and not pillar[x-1][y]: return False
        if panel[x][y+1]:
            if not double_panel_check(x,y+1,panel) and not pillar[x+1][y]: return False
    return True
    
def verifying_delete_panel(x,y,pillar,panel):
    '''
    <조건>
    보를 삭제할 때, 연결된 양쪽의 보들이 있다면, 각각의 보들이 기둥으로 받쳐져 있는지 검사해야 함
    보를 삭제할 때, 보를 바닥으로 하는 기둥들이 있다면, 각각의 기둥들이 기둥또는 다른 보로 받쳐져 있는지 검사해야 함
    * 배열의 0번째, n-2번째, 1~n-3번째로 구간을 나눠 각각의 경우에 보를 삭제 했을 때 연관된 모든 기둥과 보를 검사해야 함
    '''
    if x==0:
        if pillar[x][y] and not pillar[x][y-1]: return False
        if pillar[x+1][y] and not pillar[x+1][y-1] and not panel[x+1][y]: return False
        if panel[x+1][y] and not pillar[x+1][y-1] and not pillar[x+2][y-1]: return False
    elif x==len(pillar)-2:
        if pillar[x+1][y] and not pillar[x+1][y-1]: return False
        if pillar[x][y] and not pillar[x][y-1] and not panel[x-1][y]: return False
        if panel[x-1][y] and not pillar[x-1][y-1] and not pillar[x][y-1]: return False
    else: 
        if panel[x-1][y] and not pillar[x-1][y-1] and not pillar[x][y-1]: return False
        if panel[x+1][y] and not pillar[x+1][y-1] and not pillar[x+2][y-1]: return False
        if pillar[x][y] and not pillar[x][y-1] and not panel[x-1][y]: return False
        if pillar[x+1][y] and not pillar[x+1][y-1] and not panel[x+1][y]: return False
    return True

def verifying_install_panel(x,y,pillar,panel):
    '''
    벽면을 벗어나게 설치하는 경우는 없다.
    1. 설치 지점(시작점, 끝점) 중 하나가 기둥 위에 있는 경우 설치 가능
    2. 설치 지점(시작점, 끝점) 모두에 보가 설치되어 있는 경우 설치 가능 "- '-' -"
    '''
    if pillar[x][y-1] or pillar[x+1][y-1]: return True # 1
    elif panel[x-1][y] and panel[x+1][y]: return True # 2
    return False

def solution(n, build_frame):
    answer = [[]]
    pillar = [[0]*(n+1) for _ in range(n+1)] # 기둥 배열
    panel = [[0]*(n+1) for _ in range(n+1)] # 보 배열
    
    for x,y,item,m in build_frame:
        if item == 0: # 기둥
            if m == 1 and verifying_install_pillar(x,y,pillar,panel): # 설치
                pillar[x][y] = 1
            elif m == 0 and verifying_delete_pillar(x,y,pillar,panel) : # 삭제
                pillar[x][y] = 0
        elif item == 1: # 보
            if m == 1 and verifying_install_panel(x,y,pillar,panel): # 설치
                panel[x][y] = 1
            elif m == 0 and verifying_delete_panel(x,y,pillar,panel): # 삭제
                panel[x][y] = 0
        
    for i in range(len(pillar)):
        for j in range(len(pillar)):
            if pillar[i][j]:
                answer.append([i,j,0])
    for i in range(len(panel)):
        for j in range(len(panel)):
            if panel[i][j]:
                answer.append([i,j,1])

    answer = sorted(answer[1:], key=lambda x:(x[0],x[1],x[2]))
    return answer

# print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])) # 설치만
# [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])) # 설치 및 삭제
# [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]


