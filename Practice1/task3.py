print('Введите стороны треугольника')
a = int(input())
b = int(input())
c = int(input())

if (a + b >= c and a + c >= b and b + c >= a):
    print('Такой треугольник существует')
else: print('Такой треугольник НЕ существует')
