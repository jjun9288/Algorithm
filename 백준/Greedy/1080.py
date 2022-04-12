# 행렬

n, m = map(int, input().split())
a, b = [], []
cnt = 0
for _ in range(n):
    a.append(list(map(int, list(input()))))
for _ in range(n):
    b.append(list(map(int, list(input()))))

def cal(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            if a[i][j] == 0: 
                a[i][j] = 1
            else:
                a[i][j] = 0

if (n < 3 or m < 3) and a != b:
    cnt = -1
else:      
    for i in range(n-2):
        for j in range(m-2):
            if a[i][j] != b[i][j]:
                cnt += 1
                cal(i, j)
 
if cnt != -1:
    if a != b:
        cnt = -1

print(cnt)
                
                
    

