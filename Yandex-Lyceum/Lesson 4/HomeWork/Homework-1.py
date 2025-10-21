height = int(input())
worked = 0

while worked < height:
    tmp_height = int(input())
    if tmp_height < 0:
        worked -= tmp_height
        print('Продолжаем движение.')
    
print('Наконец-то!')