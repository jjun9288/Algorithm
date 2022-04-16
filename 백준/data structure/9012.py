# 괄호

t = int(input())

for _ in range(t):
    
    stack = []
    is_VPS = True
    
    par = input()
    
    for i in par:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                is_VPS = False
                break
            
    if stack:
        is_VPS = False
    
    print('YES' if is_VPS else 'NO')