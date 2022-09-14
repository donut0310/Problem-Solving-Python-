def find_index(arr, flag):
    tmp = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if not flag and not arr[i][j]: # 자물쇠는 홈만
                tmp.append((i, j))
            elif flag and arr[i][j]: # 열쇠는 돌기만
                tmp.append((i, j))
    return tmp

def rotate(arr, size):
    for i in range(len(arr)):
        row, col = arr[i]
        arr[i] = (col, size - row)

def solution(key, lock):    
    key_index = find_index(key, 1)
    lock_index = find_index(lock, 0)

    # 자물쇠 배열 확장 -> 열쇠 이동범위 고려
    key_size = len(key) - 1
    size = len(lock) + 2 * key_size
    extended_lock = [[2] * size for _ in range(size)]
    
    # 확장된 자물쇠 배열 초기화
    for i in range(len(lock)):
        for j in range(len(lock)):
            extended_lock[i + key_size][j + key_size] = 1
            
    for r, c in lock_index:
        extended_lock[r + key_size][c + key_size] = 0

    # 확장된 자물쇠 배열의 (0, 0) 부터 열쇠 탐색
    for i in range(len(extended_lock) - key_size + 2):
        for j in range(len(extended_lock[i]) - key_size + 2):
            for k in range(4):
                cnt, flag = 0, 0
                rotate(key_index, key_size)
                for r, c in key_index:
                    if 0 <= r + i < len(extended_lock) and 0 <= c + j < len(extended_lock):
                        if not extended_lock[r + i][c + j]: cnt += 1
                        elif extended_lock[r + i][c + j] == 1:
                            flag = 1
                            break
                if not flag and cnt >= len(lock_index): return True
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	)) # true

'''
회전 규칙
row -> before col
col -> size - before row

(1,0) -> (0,1) -> (1, 2)
(2,1) -> (1,0) -> (0, 2)
(2,2) -> (2,0) -> (0, 1)
'''
