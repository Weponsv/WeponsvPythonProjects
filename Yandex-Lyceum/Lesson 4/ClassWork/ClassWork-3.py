limit = int(input())

total = 0
count = 0

while True:
    total += int(input())
    count += 1
    if total >= limit:
        break

print(count)