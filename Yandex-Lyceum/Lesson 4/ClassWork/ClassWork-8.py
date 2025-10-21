min_food = int(input())

while True:
    tmp2_food = int(input())

    if tmp2_food < 0:
        break
    else:
        if min_food > tmp2_food:
            min_food = tmp2_food

print(min_food)