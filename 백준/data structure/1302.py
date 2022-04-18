# 베스트셀러

n = int(input())
book_dict = {}

for _ in range(n):
    book = input()
    if book in book_dict:
        book_dict[book] += 1
    else:
        book_dict[book] = 1
        
tmp = max(book_dict.values())
candidates = [] #가장 많이 팔린 책이 여러 권일 경우

for k, v in book_dict.items():
    if v == tmp:
        candidates.append(k)
        
candidates.sort()
print(candidates[0])