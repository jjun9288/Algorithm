# 자신을 제외한 배열의 곱

arr = [1,2,3,4]
tmp = 1
result = []

for i in arr:
    tmp *= i
    
for i in arr:
    result.append(tmp//i)
    
print(result)