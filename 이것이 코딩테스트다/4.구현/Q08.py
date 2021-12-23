# 08 ) 문자열 재정렬

n = input()

alphabets = []
nums = []
sum = 0

for i in range(len(n)):
    if (n[i] == '0' or n[i] == '1' or n[i] == '2' or n[i] == '3' or n[i] == '4' or n[i] == '5' or n[i] == '6' or n[i] == '7' or n[i] == '8' or n[i] == '9'):
        nums.append(int(n[i]))
    else:
        alphabets.append(n[i])

alphabets.sort()        
for a in alphabets:
    print(a, end='')

for num in nums:
    sum += num
    
print(sum)