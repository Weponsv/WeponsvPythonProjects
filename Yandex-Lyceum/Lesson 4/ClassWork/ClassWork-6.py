tmp1 = int(input())

while True:
    tmp2 = int(input())
    if tmp2 == 6000:
        break
    else:
        tmp1 = max(tmp1, tmp2)

print(tmp1)