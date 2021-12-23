# 07 ) 럭키 스트레이트

n = input()

first_sum = 0
last_sum = 0


for i in range((len(n)//2)):
    first_sum += int(n[i])

for i in range((len(n)//2), len(n)):
    last_sum += int(n[i])
    
if (first_sum == last_sum):
    print('LUCkY')
else:
    print('READY')