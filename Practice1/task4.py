print('Введите 4 числа')
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print('Вот что я насчитал')
for i in range (a, b + 1):
    if (i % d == c):
        print(i)
