height = int(input())
current_height = height

while current_height > 0:
    move = int(input())
    current_height += move
    
    if current_height <= 0:
        print('Наконец-то!')
        break
    else:
        print('Продолжаем движение.')