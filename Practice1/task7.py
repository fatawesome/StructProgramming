print('Введите x и y')
x = float(input())
y = float(input())

day = 0

while x < y:
    x = x * 1.1
    day = day + 1

print('День "y" -', day)
