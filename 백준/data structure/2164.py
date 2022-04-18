# 카드 2

#list에서 삽입 삭세를 연달아 하면 O(N^2)이 나오므로 queue를 이용해서 삽입 삭제를 하면 O(1) 이므로 queue를 이용하자

from collections import deque
dq = deque()
n = int(input())

for i in range(n):
    dq.append(i+1)
    
while(len(dq) > 1):
    dq.popleft()
    dq.append(dq.popleft())
    
print(dq.popleft())
    