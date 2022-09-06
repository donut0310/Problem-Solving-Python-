def solution(board, skill):
    # 구간합에 이용될 배열
    # 1차원 배열일때 구간합을 구하기 위한 임시 배열은 기존 배열 크기의 + 1 만큼
    # 2차원 배열일때는 행, 열 모두 기존 배열보다 1 크게 만들어야 한다.
    matrix = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    
    # 구간합 범위 지정
    for s_type, r1, c1, r2, c2, degree in skill:
        if s_type == 1: degree *= -1
        # 구간의 각 꼭짓점은 대각하지 않은 꼭짓점들과 부호가 반대여야한다.
        matrix[r1][c1] += degree
        matrix[r1][c2+1] -= degree
        matrix[r2+1][c1] -= degree
        matrix[r2+1][c2+1] += degree
    
    # 가로 구간합 계산
    for i in range(len(matrix)):
        for j in range(1, len(matrix[i])):
            matrix[i][j] = matrix[i][j - 1] + matrix[i][j]
    
    # 세로 구간합 계산
    for i in range(len(matrix[0])):
        for j in range(1, len(matrix)):
            matrix[j][i] = matrix[j - 1][i] + matrix[j][i]

    # 기존 보드판에 계산된 구간합 합치기
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += matrix[i][j]
            if board[i][j] > 0: answer += 1
    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))  # 10