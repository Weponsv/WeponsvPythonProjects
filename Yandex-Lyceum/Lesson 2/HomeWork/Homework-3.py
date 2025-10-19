n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

summa = n1 + n2
proizvedenie = summa * n3
ostatok = int(str(proizvedenie) + str(proizvedenie % 2))
result = str(ostatok) * n4

print(result)