print('Введите 3 целых числа')
a = int(input())
b = int(input())
c = int(input())

if (a > b):
    if (a > c):
        print(a, '- наибольшее число')
    else:
        print(c, '- наибольшее число')
else:
    if (b > c):
        print(b, '- наибольшее число')
    else:
        print(c, '- наибольшее число')
