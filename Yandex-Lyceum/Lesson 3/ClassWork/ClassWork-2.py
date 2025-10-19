year_time = str(input()).lower()
weather = str(input()).lower()

if (year_time == 'лето' and weather == 'дождь') or (year_time == 'зима' and weather == 'снег'):
    print('Нормально!')

elif (year_time == 'лето' and weather == 'снег') or (year_time == 'зима' and weather == 'дождь'):
    print('Глобальное изменение климата!')

else:
    print('Не хватает данных.')
