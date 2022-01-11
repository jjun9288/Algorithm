# 덩치

n = int(input())
a = []
rank = []

for i in range(n):
    a.append(list(map(int, input().split())))
    
for i in range(n):
    rank.append(1)

for i in range(len(a)):
    for j in range(i):
        if a[j][0] < a[i][0]:
            if a[j][1] < a[i][1]:
                rank[j] += 1
                
        elif a[j][0] > a[i][0]:
            if a[j][0] > a[i][0]:
                rank[i] += 1
                
for i in rank:
    print(i, end=' ')
                           

