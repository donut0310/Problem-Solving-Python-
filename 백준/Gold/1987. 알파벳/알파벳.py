import sys
input = sys.stdin.readline

def solution():
    answer = 0
    queue = set([(0, 0, matrix[0][0])])

    while queue:
        row, col, s = queue.pop()

        answer = max(answer, len(s))

        for i in range(4):
            nextY, nextX = row + dy[i], col + dx[i]

            if 0 <= nextY < m and 0 <= nextX < n and matrix[nextY][nextX] not in s:
                queue.add((nextY, nextX, s + matrix[nextY][nextX]))

    return answer

m, n = map(int, input().rstrip().split(' '))
matrix = [list(input().rstrip()) for _ in range(m)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


print(solution())