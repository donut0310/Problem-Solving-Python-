def solution(m, n, puddles): # n=행, m=열, puddles = [열, 행]
    arr = [[0]*(m+1) for i in range(n+1)]
    arr[1][1] = 1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==j==1: continue
            if [j,i] in puddles:
                arr[i][j] = 0
            else: arr[i][j] = (arr[i-1][j]+arr[i][j-1]) % 1000000007
    return arr[n][m]

print(solution(4,3,[[2,2]])) # 4

'''
<풀이>
DP 이용
문제에서 좌표의 출발점(집)과 도착점(학교)까지의 거리는 '오른쪽', '아래' 방향으로만 움직여야 한다.
흔한 지도 상에 출발지에서 도착지까지 갈 수 있는 모든 경우의 수를 구하는 문제와 같다.
즉, 최단거리가 보장된다.
이중 반복문을 사용하여, 현재 인덱스의 값은 좌표기준 1칸 왼쪽 인덱스의 값과, 1칸 위쪽 인덱스의 합과 같다.
식으로 표현하면, arr[i][j] = (arr[i-1][j] + arr[i][j-1])이 된다.
이때, 물 웅덩이를 만난 경우 지나갈 수 없기에 해당 인덱스의 값은 0으로 표기한다.
'''