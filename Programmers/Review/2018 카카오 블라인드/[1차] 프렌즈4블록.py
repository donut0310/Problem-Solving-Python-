'''
1. 행열의 각 원소 기준으로 오른쪽, 아래, 대각아래 방향에 같은 문자가 있다면 set 집합에 좌표 저장
2. set 집합의 좌표 값들을 0으로 변경
3. 마지막 행을 기준으로 위로 올라가면서 빈 공간 찾고, 빈 공간의 개수 카운트 후 다시 블록이 나오면 빈 공간 개수만큼 행 값을 늘려서 좌표 변경
4. 위 과정을 set 집합 내 원소들이 존재할 때 까지 반복
'''

def solution(m, n, board):
    answer = 0
    _board = []
    [_board.append(list(i)) for i in board]

    while True:
        target = set()
        # 지워질 블록 찾기
        for i in range(m-1):
            for j in range(n-1):
                if 'A' <= _board[i][j] <= 'Z' and (_board[i][j] == _board[i+1][j] == _board[i][j+1] == _board[i+1][j+1]):
                    target.add((i,j))
                    target.add((i+1,j))
                    target.add((i,j+1))
                    target.add((i+1,j+1))
        
        if len(target) == 0: break
        
        # 블록 지우기
        for row, col in target:
            _board[row][col] = '0'

        answer += len(target)

        # 보드판 채우기
        for j in range(n):
            cnt = 0
            for i in range(m-1, -1, -1):
                if _board[i][j] == '0': cnt += 1
                else:
                    _board[i+cnt][j], _board[i][j] = _board[i][j], _board[i+cnt][j]
    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])) # 14
print(solution(6, 6,["AABBEE","AAAEEE","VAAEEV","AABBEE","AACCEE","VVCCEE" ]))# 32