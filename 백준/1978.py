# 소수 찾기

n = int(input())
num = list(map(int, input().split()))

prime = []
cnt = 0

for number in num:
    for i in range(1, number+1):
        if number % i == 0:
            cnt += 1
        
    if cnt == 2:
        prime.append(number)
        
    cnt = 0
    
print(len(prime))
        
        
    