start = int(input())
end = int(input())
step = int(input())

first = True

while start <= end:
    if first:
        print(start, end='')
        first = False
    else:
        print(f', {start}', end='')
    start += step