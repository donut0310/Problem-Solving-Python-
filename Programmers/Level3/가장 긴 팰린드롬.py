def search(left, right, s, cnt):
    while left >= 0 and right < len(s):
        if s[left] == s[right]:
            cnt += 2
            left -= 1
            right += 1
        else: break
    return cnt

def solution(s):
    answer, cnt = 0, 0
    # 문자열 짝수
    for i in range(len(s) - 1):
        if s[i] == s[i+1]: # 중심이 되는 인덱스의 값이 뒤에 연속해서 나오는 경우 중심 값을 바꾼다 => abbaba 에서 i가 1인 경우 'b' -> 'bb'
            left, right = i-1, i+2
            cnt = search(left, right, s, 2)
            answer = max(answer,cnt)
        else:
            left, right = i-1, i+1
            cnt = search(left, right, s, 1)
            answer = max(answer,cnt)

    # 문자열 홀수
    for i in range(len(s)):
        left, right = i-1, i+1
        cnt = search(left, right, s, 1)
        answer = max(answer,cnt)
    return answer

print(solution("abcdcba")) # 7
print(solution("abacde")) # 3
print(solution("abaaba")) # 6
print(solution("abbaba")) # 4
print(solution("abbb")) # 3

'''
<풀이>
1.문자열의 각 문자를 기준으로 좌우를 탐색한다.
2. 좌우를 탐색할 때 좌우가 같은 값인 경우를 만족 할 때 까지 반복하며
    팰린드롬 문자열의 길이를 계산하고, 최대값을 갱신한다.
3. 1-2의 과정을 문자열 s 길이만큼 반복한다.

문자열의 길이가 짝수 or 홀수인 경우로 분기해서 풀었으나 테스트케이스 5와 같이
두 조건을 모두 만족하는 경우가 발생하여, 짝수와 홀수 부분을 같은 레벨에 두고 모두 검사함

'''