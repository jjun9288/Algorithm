# 섬의 개수

graph_1 = [
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,1,0,0,0],
    [0,0,0,0,0]
]

graph_2 = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]
]

cnt = 0
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]   
            
def DFS(x,y):
    graph_2[x][y] = 2
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 4 and 0 <= ny < 5:
            if graph_2[nx][ny] == 1:
                DFS(nx,ny)
         
for i in range(4):
    for j in range(5):
        if graph_2[i][j] == 1:
            DFS(i,j)
            cnt += 1
            
print(cnt)