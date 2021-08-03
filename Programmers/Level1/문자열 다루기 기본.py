def solution(s):
    slen = len(s)
    
    if slen>=1 and slen<=8:
        if slen == 4 or slen == 6:
            for i in s:
                if i not in ['1','2','3','4','5','6','7','8','9','0']:
                    print('false')
                    return False
            return True
        return False
    return False
solution('a234')
solution('2 2 ')
solution('1.1.')