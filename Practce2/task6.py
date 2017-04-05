import math

print('Give me coordinates:')
print('X')
x = float(input())
print('Y')
y = float(input())

p = math.sqrt(x ** 2 + y ** 2)
f = math.atan(y / x)

print('p = ', p)
print('f = ', f)
