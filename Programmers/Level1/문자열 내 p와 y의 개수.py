def solution(s):
    s = s.lower();
    
    p_c = s.count('p')
    y_c = s.count('y')

    if p_c==y_c:
        return True
    else:
        return False

solution('pPoooyY')
solution('Pyy')