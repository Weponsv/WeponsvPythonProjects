T_planet = float(input())

T_Earth, a_earth = 1, 1

a_planet = a_earth * (T_planet / T_Earth) ** (2 / 3)
# a2​ = 1 * (T1​ / 1​​) ** (2 / 3)
result = round(a_planet, 3)
print(result)