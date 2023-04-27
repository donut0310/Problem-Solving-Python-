def symmetry_by_x(x1, y1, x2, y2, n):
    by_x = (-y1 - y2) ** 2 + (x1 - x2) ** 2 # x축으로의 선대칭
    by_n = (n + n - y1 - y2) ** 2 + (x1 - x2) ** 2 # n을 축으로하는 선대칭
    return min(by_x, by_n)
    
def symmetry_by_y(x1, y1, x2, y2, m):
    by_y = (-x1 - x2) ** 2 + (y1 - y2) ** 2 # y축으로의 선대칭
    by_m = (m + m - x1 - x2) ** 2 + (y1 - y2) ** 2 # m을 축으로 하는 선대칭
    return min(by_y, by_m)
    
def solution(m, n, startX, startY, balls):
    answer = []
    
    for targetX, targetY in balls:
        if startX == targetX:
            answer.append(min(symmetry_by_y(startX, startY, targetX, targetY, m), (2*n - startY - targetY) ** 2 if startY > targetY else (startY + targetY) ** 2))
        elif startY == targetY:
            answer.append(min(symmetry_by_x(startX, startY, targetX, targetY, n), (2*m - startX - targetX) ** 2 if startX > targetX else (startX + targetX) ** 2))
        elif startX != targetX and startY != targetY:
            answer.append(min(symmetry_by_y(startX, startY, targetX, targetY, m), symmetry_by_x(startX, startY, targetX, targetY, n)))
    return answer

'''
점과 점 사이 거리 (점대칭, 선대칭) 
1. x 좌표가 같으면 x축을 기준으로 선대칭을 한다.(이때, x축 기준, n 기준, m 벽 찍고 돌아가는 길, y축 찍고 돌아가는 길 구별)
2. y 좌표가 같으면 y축을 기준으로 선대칭을 한다.(이때, y축 기준, m 기준, n 벽 찍고 돌아가는 길, x축 찍고 돌아가는 길 구별)
3. x 좌표와 y좌표가 모두 다르면 y축 기준 선대칭했을 때의 값과 x축 기준 선대칭 했을 때의 값을 비교(역시 대칭점이 y,x,m,n 중 가까운 곳으로 진행)
'''