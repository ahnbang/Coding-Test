def DFS(y,x):
    global groupN
    if y <= -1 or x <= -1 or y >= N or x >= N:
        
        return False
    
    if graph[y][x] == 1:
        
        graph[y][x] = 0
        groupN += 1
        DFS(y+1,x)
        DFS(y,x+1)
        DFS(y-1,x)
        DFS(y,x-1)
        
        
        return True
    
    return False



if __name__ == "__main__":
    
    N = int(input())
    graph = []
    for _ in range(N):
        
        numbers = list(map(int, input()))
        graph.append(numbers)
    
    
    result = 0
    group = []
    #for i in range(N):
    #for j in range(N):
    for i in range(N):
        for j in range(N):
            groupN = 0
            if DFS(j,i) == True:
                result +=1
                group.append(groupN)
    group.sort()
    print(result)
    for i in group:
        print(i)            
    
    