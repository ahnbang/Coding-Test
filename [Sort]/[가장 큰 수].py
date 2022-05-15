def solution(numbers):
    answer = ''
    sum = 0
    for i in numbers:
        sum += i 
    
    if i!= 0:
        numbers = list(map(str,numbers))
        numbers.sort(key = lambda x: x*3, reverse = True)
        for i in numbers:
            answer += i
    else:
        answer+= str(0)
    return answer
