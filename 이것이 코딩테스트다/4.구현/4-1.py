# 4-1) 상하좌우

n = int(input())
x, y = 1, 1

a = list(input().split())

for i in range(len(a)):
    if a[i] == 'L':
        if y != 1:
            y -= 1
        else:
            y = y
    
    if a[i] == 'R':
        if y != n:
            y += 1
        else:
            y = y
    
    if a[i] == 'U':
        if x != 1:
            x -= 1
        else:
            x = x
            
    if a[i] == 'D':
        if x != n:
            x += 1
        else:
            x = x
      
print(x, y)