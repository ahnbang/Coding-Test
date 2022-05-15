import string
table = ['-','_','.']
special = string.punctuation
for s in table:
    special = special.replace(s, "")
special = list(special)
table2 = []
for i in range(2,15):
    string = '.'*i
    table2.append(string)
table2.reverse()

def solution(new_id):
    new_id = new_id.lower()
    for s in special:
        new_id = new_id.replace(s,"")
    for s in table2:
        new_id = new_id.replace(s, '.')
    new_id = new_id.strip('.')
    if len(new_id) == 0:
        new_id += 'a'
    if len(new_id) >= 16:
        
        new_id = new_id[0:15]
        new_id = new_id.strip('.')
    if len(new_id) <= 2:
        string2 = new_id[len(new_id)-1]
        while len(new_id) != 3:
            new_id+=string2
    
    return new_id
