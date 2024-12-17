N = int(input())
book_dict = dict()

for _ in range(N):
    book = input()
    if book not in book_dict:
        book_dict[book] = 1
    else:
        book_dict[book] += 1

max = max(book_dict.values())

answer = []

for k, v in book_dict.items():
    if v == max:
        answer.append(k)

answer.sort()
print(answer[0])