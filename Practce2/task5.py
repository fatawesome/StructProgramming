import math

print('Give me x')
x = float(input())
ln = x
if (x < 0):
    ln *= -1

a = math.log(ln)
b = (math.e) ** (2 * x) + a * x
y = x * (a ** 3) + (b ** 2)

print('a = ', a)
print('b = ', b)
print('y = ', y)
