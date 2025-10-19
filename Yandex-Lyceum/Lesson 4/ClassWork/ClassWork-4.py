need_1 = int(input())
need_2 = int(input())

count = 0
while True:
    text = int(input())
    if text == need_1 or text == need_2:
        break
    else:
        count += 1

print(count)