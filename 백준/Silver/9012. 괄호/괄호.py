# Stack을 이용하여, 예를 들어 닫는 괄호가 들어오고 그 뒤로 여는 괄호가 들어온다면
# 닫는 괄호를 pop을 할 수 있는 것이다.

T = int(input())

for _ in range(T):
    p = input()
    list = []
    isVPS = True
    
    for i in p:
        if i == '(':
            list.append(i)
        else:
            if list:
            #if len(list) > 0:
                list.pop()
            else:
                isVPS = False
                break

    if list:
    #if len(list) > 0 :
        isVPS = False

    print('YES' if isVPS==True else 'NO')