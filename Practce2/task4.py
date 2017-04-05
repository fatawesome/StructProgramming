import math

print('Give me 3 numbers')
r = float(input()) ** 2
l = float(input()) * 0.2
c = 1 / (float(input()) * 0.2)

print(math.sqrt(r + (l - c) ** 2))
