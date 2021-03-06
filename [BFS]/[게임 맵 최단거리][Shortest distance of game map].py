# link : https://programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque
def solution(maps):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]  
    start = (0,0)
    queue = deque()
    queue.append(start)
    N,M = len(maps), len(maps[0])
    while queue:
        x,y = queue.popleft()
        for i in range(len(dx)):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny >= N or ny < 0 or nx >= M or nx < 0: 
                continue
            if maps[ny][nx]  == 0: 
                continue
            if maps[ny][nx]  == 1:
                Next = (nx,ny)
                maps[ny][nx] = maps[y][x] + 1
                queue.append(Next)
    if maps[N-1][M-1] == 1: 
        return -1
    else:
        return maps[N-1][M-1]
    
  if __name__ == "__main__"
    maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
    solution(maps)
  
  
  

  
  
  
