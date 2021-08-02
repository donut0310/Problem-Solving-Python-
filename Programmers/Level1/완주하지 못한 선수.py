def check(participant,completion):
    c_len = len(completion)
    for i in range(len(participant)):
        if i==c_len:
            return participant[i]
        if participant[i]!=completion[i]:
            return participant[i]

    
def solution(participant, completion):
    participant.sort()
    completion.sort()
    return check(participant,completion)

   
# solution(["leo", "kiki", "eden"],["eden", "kiki"])
# solution(["marina", "marina", "marina", "aaa", "filipa"],["marina", "marina", "marina", "filipa"])
# solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])