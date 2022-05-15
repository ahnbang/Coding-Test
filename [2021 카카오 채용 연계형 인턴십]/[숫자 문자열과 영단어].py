def solution(s):
    answer = 0
    words = ['zero','one','two','three','four','five','six','seven','eight','nine']
    
    for word in words:
        
        s = s.replace(word,str(words.index(word)))
        
    answer = int(s)
    
    return answer
