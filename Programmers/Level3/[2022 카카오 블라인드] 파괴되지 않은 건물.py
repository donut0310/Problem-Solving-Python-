def solution(board, skill):
    answer = 0
    matrix = [[0]*(len(board[0])+1) for _ in range(len(board)+1)] # 누적합 배열 선언 및 초기화

    for type,r1,c1,r2,c2,degree in skill:
        if type==1: degree *= -1
        matrix[r1][c1] += degree
        matrix[r1][c2+1] -= degree
        matrix[r2+1][c1] -= degree
        matrix[r2+1][c2+1] += degree

    # 누적합 좌->우
    for i in range(len(matrix)):
        for j in range(1,len(matrix)):
            matrix[i][j] = matrix[i][j-1]+matrix[i][j]

    # 누적합 상->하
    for i in range(len(matrix[0])):
        for j in range(1, len(matrix)):
            matrix[j][i] = matrix[j-1][i]+matrix[j][i]

    # board 판과 matrix(누적합 배열) 합치기
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = board[i][j] + matrix[i][j]
            if board[i][j]>=1: answer+=1

    return answer

print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])) # 10
print(solution([[1,2,3],[4,5,6],[7,8,9]],[[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]])) # 6

''' 
<풀이>

<알고리즘>
누적합 이용
위 문제는 브루트 포스로 풀 시 O(k*n*m)에 해당하기에 시간초과가 발생한다
각 구간까지의 구간합을 구하는 누적합을 이용해야한다.
2차원 배열의 구간합을 구하기 위한 범위값을 matrix 배열에 저장한다. -> O(k) 시간에 가능
이후 matrix 2차원 배열을 왼쪽에서 오른쪽, 위에서 아래로 2번 누적합을 구한다.
마지막으로 board와 matrix배열의 인덱스별로 값을 더해주면 O(n*m) 시간에 가능
최종 O(k+n*m)에 해결이 가능하다.

2차원배열에서의 누적합을 이용할 수 있는 좋은 문제였다.
'''
'''
skill => [type, r1, c1, r2, c2, degree]
type => 1(공격) or 2(회복)
범위 => (r1,c1) ~ (r2,c2)
건물의 내구도 0 이하 => 파괴된 건물
건물의 내구도 1 이상 => 파괴되지 않은 견물
'''
