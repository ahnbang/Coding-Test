# Link : https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    answer = 0
    student = [True]*(n+2)
    lost.sort()
    reserve.sort()
    for i in range(len(lost)):
        for i in lost:
            if i in reserve:
                reserve.remove(i)
                lost.remove(i)
    
    for i in lost: 
        if (i-1) in reserve:
            reserve.remove(i-1)
        elif (i+1) in reserve:
            reserve.remove(i+1)
        else:
            student[i] = False
    student[0], student[n+1] = False, False
    answer = student.count(True)
    return answer
