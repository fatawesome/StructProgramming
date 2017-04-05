import math

print('Give me 3 numbers')

c = float(input())
x = float(input())
t = float(input())

ctg = (1 / (math.tan(math.radians(c)))) ** 2
top = 2 * (x ** 2) + 5
bot = math.sqrt(c + t)

print(ctg + top / bot)
