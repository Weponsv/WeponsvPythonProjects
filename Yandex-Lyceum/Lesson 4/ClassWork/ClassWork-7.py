tmp_name1 = str(input())
tmp_age1 = int(input())

max_age = tmp_age1
max_name = tmp_name1

while True:
    tmp_name2 = str(input())
    tmp_age2 = int(input())

    if tmp_age2 < 0:
        break
    else:
        if max_age < tmp_age2:
            max_age = tmp_age2
            max_name = tmp_name2

print(max_name)