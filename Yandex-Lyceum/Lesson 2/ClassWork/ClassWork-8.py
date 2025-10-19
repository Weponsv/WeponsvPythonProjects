import math
I0 = 1e-12

intensity = float(input())

beta = 10 * math.log10(intensity / I0)
result = math.ceil(beta)

print(result)