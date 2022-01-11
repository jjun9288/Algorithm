# 블랙잭

n, m = map(int, input().split())
a = list(map(int, input().split()))
sum = []

for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            if (a[i]+a[j]+a[k] <= m) :
                sum.append((a[i]+a[j]+a[k]))
                
print(max(sum))
            
