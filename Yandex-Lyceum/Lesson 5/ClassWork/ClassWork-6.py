text = str(input())
count = 0

for letter in text:
    if count == 0:
        print(f'{letter};')
    else:
        if count == len(text) - 1:
            repeated = f'{letter}-' * (count) + f'{letter}.'
        else:
            repeated = f'{letter}-' * (count) + f'{letter};'
        print(repeated)
    
    count += 1