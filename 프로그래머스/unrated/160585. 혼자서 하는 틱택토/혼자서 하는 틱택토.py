def search(arr, info, flag):
    o_cnt, x_cnt, o_flag, x_flag = info
    if flag:
        o_cnt += arr.count('O')
        x_cnt += arr.count('X')
    if len(set(arr)) == 1:
        if arr[0] == 'O': o_flag = 1
        elif arr[0] == 'X': x_flag = 1
        
    info = (o_cnt, x_cnt, o_flag, x_flag)
    return info

def solution(board):
    answer = -1
    arr = []
    info = (0, 0, 0, 0) # o_cnt, x_cnt, o_flag, x_flag
        
    # 각 행, 열별로 O, X가 일렬로 있는지 조사
    for i in range(3):
        row = [board[0][i], board[1][i], board[2][i]]
        col = [board[i][0], board[i][1], board[i][2]]
        info = search(row, info, 1)
        info = search(col, info, 0)
    
    diags = [[board[0][0], board[1][1], board[2][2]], [board[2][0], board[1][1], board[0][2]]]
    
    for diag in diags:
        info = search(diag, info, 0)

    # O,X 표시의 차례가 바뀐 경우 -> o_cnt < x_cnt
    
    # 게임이 종료되었음에도 계속 진행하는 경우
    if info[2] and info[0] <= info[1]: return 0
    if info[3] and info[0] != info[1]: return 0
    if info[0] < info[1] or info[0] - info[1] > 1: return 0

    return 1

'''
<풀이>
주어진 배열의 크기는 가로 세로 3 고정이다.
배열을 각 행, 열, 대각선으로 쪼갠 뒤 다음과 같은 검증을한다.
1. 배열 arr에서 'O', 'X'가 몇개씩 있는지, 하나의 문자로만 이루어져있는지를 검사한다.
1-1. 배열마다 'O'와 'X'의 개수를 증가한다.
1-2. set(arr)의 사이즈가 1이라면 하나의 문자로 이루어진 것이기 때문에 arr[0]이 'O'라면 o_flag = 1
1-3. set(arr)의 사이즈가 1이라면 하나의 문자로 이루어진 것이기 때문에 arr[0]이 'O'라면 x_flag = 1
2. 1에서 구한 값들을 가지고 분기문을 사용해 틱택토 게임이 정상적으로 진행될 수 없는 상황인지 검사한다.
'''