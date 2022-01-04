# 떡볶이 떡 자르기

n, m = map(int, input().split())
tteok = list(map(int, input().split()))


cut = max(tteok)
cut_tteok = []


while (cut > 0):
    for i in tteok:
        if (i > cut):
            cut_tteok.append(i-cut)
        else:
            cut_tteok.append(0)
    
    sum = 0
    for i in cut_tteok:
        sum += i
       
    cut_tteok = []
     
    if sum == m:
        break
    
    else:
        cut -= 1
        
print(cut)
    
    
        

