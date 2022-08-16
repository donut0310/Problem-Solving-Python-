def find_index(arr, flag):
    extended_arr = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] and flag: extended_arr.append((i,j))
            if not arr[i][j] and not flag: extended_arr.append((i,j))
    return extended_arr

def rotate(key_index, size):
    for i in range(len(key_index)):
        row, col = key_index[i]
        key_index[i] = (col, size-row)

def solution(key, lock):
    answer = False

    key_index = find_index(key,1)
    lock_index = find_index(lock,0)

    n = len(lock) + (len(key)-1) * 2 # 확장할 배열의 확장 범위는 자물쇠 배열의 크기를 기준으로 열쇠가 이동가능한 영역을 구해야 한다.
    size = len(key) - 1
    arr = [[1] * n for _ in range(n)] # 자물쇠 배열 범위 확장

    for row,col in lock_index:
        arr[row + size][col + size] = 0

    for i in range(len(lock_index)):
        row, col = lock_index[i]
        lock_index[i] = (row+size, col+size)

    for i in range(4):
        rotate(key_index, size)
        print(key_index)
        for j in range(n-len(key)+1):
            for k in range(n-len(key)+1):
                cnt = 0
                for row,col in key_index:
                    row += j
                    col += k
                    if size <= row < size+len(lock) and size <= col < size+len(lock) and arr[row][col]: break # 자물쇠 영역 내에서 열쇠의 돌기와 자물쇠의 돌기가 만나면 안된다.
                    if not arr[row][col]: cnt+=1
                if cnt==len(lock_index): return True

    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]])) # true

'''
<풀이>
1. 자물쇠 배열을 기준으로 열쇠가 이동 가능한 영역을 확장한 배열 arr을 선언 및 초기화한다.
2. 열쇠 배열의 돌기 부분만 인덱스를 구한다 -> 회전시 이용함
3. 자물쇠 배열의 돌기 부분만 인덱스를 구한다. -> arr 배열내에서 자물쇠의 홈을 인덱스를 조정해 지정해야함
4. 열쇠는 arr 배열의 (0,0)으로 기준을 잡고, 전체 배열을 탐색한다.
4-1. 이때, 열쇠 돌기 부분의 변하는 인덱스 값이, 자물쇠의 홈 부분과 일치한다면, 카운트롤 올리고, 카운트가 홈의 개수와 맞다면 참을 반환한다.
4-2. 자물쇠의 영역 내에서 열쇠의 돌기와 자물쇠의 돌기는 만나면 안되기 때문에 예외처리를 진행한다.
위 과정에서 참이 반환되지 않으면, 자물쇠를 열 수 없기에 answer값을 그대로 반환한다(False)
'''