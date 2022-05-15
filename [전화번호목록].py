# Link : https://programmers.co.kr/learn/courses/30/lessons/42577

def Hash(number):
    
    value = 0
    for i in range(len(number)):
        value += (int(number[i])*(i+13))
    
    return value

def solution(phone_book):
    phone_book.sort()
    history = [False]*len(phone_book)
    stand = 0
    history[stand] = True
    answer = True
    
    while history[len(phone_book)-2] != True:
        
        
        
        stand_value = Hash(phone_book[stand])
        
        len_stand = len(phone_book[stand])
        for i in range(stand+1, len(phone_book)):
        
            target = phone_book[i][0:len_stand]
            target_value = Hash(target)
            
            if stand_value == target_value:
                answer = False
                break
            else:
                stand += 1
                history[stand] = True
                break
        
        if answer == False: break   
            
    return answer
        
                
