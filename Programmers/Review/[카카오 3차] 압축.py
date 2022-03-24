from collections import defaultdict
def solution(msg):
    answer = []
    press_dict = defaultdict(str)
    #사전 초기화
    for i in range(1,27): press_dict[chr(i+64)]=i

    cnt=27
    while msg:
        for i in range(len(msg),0,-1):
            if msg[:i] in press_dict:
                answer.append(press_dict[msg[:i]])
                press_dict[msg[:i+1]]=cnt
                cnt+=1
                msg=msg[len(msg[:i]):]
                break
    return answer

print(solution('KAKAO')) # [11, 1, 27, 15]
print(solution('TOBEORNOTTOBEORTOBEORNOT')) # [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
print(solution('ABABABABABABABAB')) #[1, 2, 27, 29, 28, 31, 30]

# A-Z까지 알파벳을 키로, 1~26까지 숫자를 값으로 press_dict를 초기화한다.
# 입력문자 msg를 역으로 -1씩 슬라이싱한 단어들이 press_dict에 등록되어있는지 조사한다.
# 등록이 되어 있다면 현재 슬라이싱된 msg에 +1 자리만큼 더한 문자열을 press_dict에 새로 등록한다.
