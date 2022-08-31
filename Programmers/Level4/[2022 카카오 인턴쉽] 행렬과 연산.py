from collections import deque

def rotate(first_row:deque, last_row:deque, cols:deque):
    # rotate
    cols[0].appendleft(first_row.popleft())
    last_row.appendleft(cols[0].pop())
    cols[-1].append(last_row.pop())
    first_row.append(cols[-1].popleft())
    return

def shiftrow(first_row:deque, last_row:deque, cols:deque):
    cols.appendleft(cols.pop())
    first_row.appendleft(first_row.pop())
    last_row.appendleft(last_row.pop())
    return

def rebuild(first_row:deque, last_row:deque, cols:deque):
    arr = []
    for i in range(len(cols)):
        tmp = []
        tmp.append(first_row.popleft())
        tmp.extend(list(cols[i]))
        tmp.append(last_row.popleft())
        arr.append(tmp)
    return arr

def solution(rc, operations):
    first_row, last_row = deque(), deque() # deque([]), deque([])
    cols = deque() # deque([deque([],deque([]...))])
    for col in rc:
        first_row.append(col[0])
        last_row.append(col[-1])
        cols.append(deque(col[1:-1]))

    for oper in operations:
        if oper == "Rotate": rotate(first_row, last_row, cols)
        elif oper == "ShiftRow": shiftrow(first_row, last_row, cols)

    answer = rebuild(first_row, last_row, cols)
    return answer

print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"])) # [[8, 9, 6], [4, 1, 2], [7, 5, 3]]


'''
<풀이>
카카오 테크 해설 참고

1. 주어진 배열을 다음과 같이 분해한다.
1-1. 첫번째 열의 모든 원소를 가지는 배열 first_row, 마지막 열의 모든 원소를 가지는 배열 last_row, 모든 행의 [1:-1] 범위의 원소를 가지는 cols를 각각
    deque로 선언한다. => 덱을 이용한 pop, append 작업은 O(1)의 시간복잡도를 가지며, 전체 배열을 조정하지 않고도 배열의 움직임을 나타낼 수 있다.
2. shiftrow는 1에서 선언한 3개의 덱을 전부 맨 앞 원소에 맨 뒤 원소를 삽입하면 된다.
    ex) 1,2,3,4,5 -> 5,1,2,3,4
3. rotate는 다음의 규칙을 따른다.
3-1. first_row의 첫 번째 원소는 cols의 첫번째 행의 첫 번째 원소로 이동한다.
3-2. cols의 첫 번째 행의 마지막 원소는 last_row의 첫 번째 원소로 이동한다.
3-3. last_row의 마지막 원소는 cols의 마지막 행의 마지막 원소로 이동한다.
3-4. cols의 마지막 행의 첫번째 원소는 first_row의 마지막 원소로 이동한다.
4. shiftrow와 rotate가 완료되면 rebuild 함수를 통해 재조립 과정을 거쳐야한다. => O(nm)의 시간복잡도

'''