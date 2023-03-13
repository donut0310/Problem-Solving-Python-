import sys
input = sys.stdin.readline
import sys
input = sys.stdin.readline

def solution1():
    s = list(input())    
    n = int(input())

    len_s = len(s) + 1
    arr = [[0] * 27 for _ in range(len_s)]    

    for i in range(1, len_s):
        for j in range(1, 27):
            if j == ord(s[i-1]) - 96:
                arr[i][j] += arr[i-1][j] + 1
            else: arr[i][j] += arr[i-1][j]

    for i in range(n):
        c, l, r = input().split(' ')
        print(arr[int(r)+1][ord(c) - 96] - arr[int(l)][ord(c) - 96])
        
solution1()

def solution2():
    s = list(input().rstrip())    
    n = int(input())

    len_s = len(s) + 1
    arr = [[0] * len_s for _ in range(27)]    
    for i in range(1, len_s):
        arr[ord(s[i-1]) - 96][i-1] += 1

    for i in range(1, 27):
        for j in range(1, len_s):
            arr[i][j] += arr[i][j-1]

    for i in range(n):
        c, l, r = input().split(' ')
        cnt = arr[ord(c) - 96][int(r)] - arr[ord(c) - 96][int(l)]
        print(cnt) if s[int(l)] != c else print(cnt + 1)
        
solution2()

'''
## 풀이 1로 먼저 풀었을때 100점이 나오지 않아 새로운 풀이법을 찾아 풀어보았지만 역시 50점이었다.
## 사실 두 풀이 모두 정답인데 python3 으로 제출하니 모두 50점이었다.
## pypy3으로 제출시 모두 100점으로 통과가 되는데 이유는 찾아봐야할 것 같다 :(
## 참고로 풀이 2의 실행 속도가 풀이 1보다는 빠르다 512ms vs 392ms

<풀이 1>
문자열 길이(행) * 알파벳 26자(열)로 가지는 2차원 배열 arr을 선언한다.
1. arr 배열을 탐색하면서 누적합을 구한다.
2. 현재 열을 인덱스로 가지는 문자열의 값이 현재 열과 값이 같다면 누적합에 +1을 더한다.
3. 다르다면 이전 인덱스 값을 바탕으로 누적합만 구한다. 
4. 입력된 문자(c)와 범위값(l, r)에 속하는 문자의 값을 출력한다.

<풀이 2>
알파벳 26자(행) * 문자열 길이(열)로 가지는 2차원 배열 arr 선언한다.
1. arr 각 행(문자열의 인덱스) 열(문자열의 인덱스)위치에 해당 문자값을 아스키 코드로 저장한다.
2. arr 2차원 누적합을 구한다. -> arr 열에는 해당 인덱스까지 어떠한 알파벳들이 누적되었는지 정보를 알 수 있다.
    ex 1) 1행 5열의 데이터는 주어진 문자열 s의 5번째 원소까지 1행(알파벳 a)가 몇개 누적되었는지 저장되어있다.
    ex 2) 3행 8열의 데이터는 주어진 문자열 s의 8번째 원소까지 3행(알파벳 c)가 몇개 누적되었는지 저장되어있다.
3. 입력된 문자(c)와 범위값(l, r)에 속하는 문자의 값을 출력한다.


'''
