def solution(lottos, win_nums):
    table = [6,6,5,4,3,2,1]
    joker = 0
    winning = 0
    
    for i in lottos:
        if i == 0: 
            joker += 1
        elif i in win_nums:
            winning += 1
    answer = [table[winning+joker], table[winning]]
    return answer
