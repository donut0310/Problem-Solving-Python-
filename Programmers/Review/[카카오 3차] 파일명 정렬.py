import re

def solution(files):
    answer,arr = [],[]
    # 문자열 분리후 리스트화
    for file in files:
        head,number,tmp='','',[file]
        for i in range(len(file)):
            if not re.match('[0-9]',file[i]): #HEAD 구하기 => 숫자가 아닌 경우
                head += file[i]
                if re.match('[0-9]',file[i+1]):
                    tmp.append(head.lower())
            elif re.match('[0-9]',file[i]): #NUMBER 구하기 => 숫자인 경우
                number += file[i]
                if i==len(file)-1: 
                    tmp.append(int(number))
                    break
                elif not re.match('[0-9]',file[i+1]):
                    tmp.append(int(number))
                    break
        arr.append(tmp)
    #정렬
    arr.sort(key=lambda x:(x[1],x[2]))
    [answer.append(i[0]) for i in arr]
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
##["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]


# print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
## ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

# 파일명의 첫번째 인덱스부터 조사를 시작한다.
# 현재 인덱스의 문자와 다음 인덱스의 문자를 조사해 HEAD 기준에 충족하는지 판별한다.
# 다음 인덱스가 HEAD 기준에 충족하지 않는다면 현재까지 저장된 head변수의 HEAD값을 tmp[]에 삽입한다.
# NUMBER도 마찬가지의 방법으로 진행한다.

# arr 배열이 완성이 되면 HEAD(사전순), NUMBER(숫자순)의 우선순위로 정렬한다.
