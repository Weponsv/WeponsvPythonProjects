prev_temp = int(input())
all_above_10 = prev_temp > 10
has_small_diff = False

for _ in range(4):
    current_temp = int(input())
    
    all_above_10 = all_above_10 and (current_temp > 10)
    
    if abs(current_temp - prev_temp) <= 2:
        has_small_diff = True
    
    prev_temp = current_temp

if all_above_10 and has_small_diff:
    print('Пора на север!')
else:
    print('Ещё не пора.')