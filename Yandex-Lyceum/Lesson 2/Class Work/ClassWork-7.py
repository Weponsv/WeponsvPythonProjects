word = input()


biggest_letter = max(word)
smallest_letter = min(word)

length = len(word)
if length % 2 == 1:
    length = length - 1

length = int(length)
print(f'{smallest_letter * (length // 2)}{biggest_letter * (length // 2)}')