def solution(phone_number):
    answer = ''
    
    for i in phone_number[:-4]:
        answer+=''.join('*')

    answerLen = len(answer)    
    
    for i in phone_number[answerLen:]:
        answer+=''.join(i)
    return answer

solution('01033334444')
solution('027778888')