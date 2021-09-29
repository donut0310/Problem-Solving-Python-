from collections import defaultdict

def findHead(file):
    n_list = [str(i) for i in range(0,10)]
    head = []
    for i in file:
        if i not in n_list:
            head.append(i)
        else:
            break
    return ''.join(head)

def findNumber(file):
    n_list = [str(i) for i in range(0,10)]
    number=[]
    for i in file:
        if i in n_list:
            number.append(i)
        else:
            break
    return int(''.join(number))

def solution(files):
    answer = []
    file_dict = defaultdict(list)

    for i in files:
        file_dict[i].append(findHead(i).lower()) #Head
        file_dict[i].append(findNumber(i[len(file_dict[i][0]):])) #Number

    new_dict = sorted(file_dict.items(),key=lambda x:(x[1][0],int(x[1][1]))) #Sort => 1: Head, 2: Number
    [answer.append(i[0]) for i in new_dict]
    
    return answer

solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])