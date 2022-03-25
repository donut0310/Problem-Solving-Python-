def solution(m, n, board):
    answer = 0
    _board = []
    # board 판 2차원 배열로 초기화
    for i in board:
        tmp = []
        [tmp.append(j) for j in i]
        _board.append(tmp)

    # 지워질 블록 구하기
    while True:
        tmp=set()
        for i in range(m-1):
            for j in range(n-1):
                if not _board[i][j]: continue #이미 지워진 블록인 경우 skip
                if _board[i][j]==_board[i][j+1]==_board[i+1][j]==_board[i+1][j+1]:
                    tmp.add((i,j))
                    tmp.add((i+1,j))
                    tmp.add((i,j+1))
                    tmp.add((i+1,j+1))
        if len(tmp)==0: return answer # 지워질 블록이 없는 경우 -> 게임 끝
        answer+=len(tmp) # 회당 지워질 블록의 개수 카운팅

        # 지워질 블록의 위치를 0으로 할당
        for i,j in tmp:
            _board[i][j]=0

        #빈공간 채우기, 열을 기준으로 마지막 행부터 역으로 조사후 swap
        for i in range(n):
            cnt=0
            for j in range(m-1,0,-1):
                if not _board[j][i]:
                    cnt+=1
                    if _board[j-1][i]:
                        _board[j-1][i],_board[j-1+cnt][i] = _board[j-1+cnt][i],_board[j-1][i]
                        cnt-=1

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))  #14
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])) #15

# board의 각 문자열을 쪼개서 _board 2차원배열을 초기화한다.
# 지워질 블록들의 위치 정보를 튜플로 저장할 tmp 집합을 선언한다.
# 각 행열의 -1번째 위치까지를 범위로 현재 인덱스에서 오른쪽, 아래, 우하대각선 방향의 인덱스를 조사한다.
# 4개의 값이 모두 같다면 tmp에 위치정보를 저장한다.
# tmp 위치 정보에 저장된 인덱스를 _board 에서 0값으로 대체한다.
# 이후 각 열을 기준으로 마지막 행부터 역으로 0의 위치를 조사하고, 0이 존재할때마다 cnt값을 증가시킨다.
# 0인 경우 바로 위 자리에 위치하는 값을 조사하고, 0이 아닌 경우엔 cnt값을 더해 맨처음 0이었던 위치와 교체한다.
# tmp에 저장된 값이 없다면 지워질 블록이 없다는 것이기에 게임을 종료한다.
