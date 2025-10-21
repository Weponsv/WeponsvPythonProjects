start = int(input())
end = int(input())

for i in range(start, end, 2):
    print(i, end=' ')

for i in range(end, start - 1, -1):
    print(i, end=' ')