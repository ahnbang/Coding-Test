def solution(numbers, target):
    answer = 0
    def DFS(Result, Depth):
        if Depth == len(numbers):
            if Result == target:
                nonlocal answer
                answer+=1
                
        else:
            DFS(Result+numbers[Depth], Depth+1)
            DFS(Result-numbers[Depth], Depth+1)
        return answer
    DFS(0,0)
    return answer
