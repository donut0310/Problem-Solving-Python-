import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub('[^\.a-z0-9_-]', '',new_id)
    new_id = re.sub('\.+', '.',new_id)
    new_id = new_id.strip('.');
    if new_id == "":
        new_id = 'a';

    new_id = new_id[0:15]; 
    new_id = new_id.rstrip('.');

    while(len(new_id)<3):
        new_id+=new_id[len(new_id)-1]
        
solution("...!@BaT#*..y.abcdefghijklm")