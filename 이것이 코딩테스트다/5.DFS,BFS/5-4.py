# 4) 미로 탈출

from collections import deque

n, m = map(int, input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input())))
    
cnt = 0    
    
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def BFS(x,y):
    q = deque([(x,y)])
    maze[x][y] = 2   # 1부터 1씩 더해가면 되지만 첫 시작이 1이여서 1로 두고 시작하면 시작 노드를 인식하지 못해서 2로 시작. 연산이 끝난 후 -1을 해준다.
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 1:
                    q.append((nx,ny))
                    maze[nx][ny] = maze[x][y] + 1  #방문했던 노드에 +1을 해서 도착지의 값이 최소거리일 것이다.
                
                
                
BFS(0,0)
print(maze[n-1][m-1]-1)

 