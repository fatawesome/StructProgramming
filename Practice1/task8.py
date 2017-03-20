print('Введите кол-во элементов массива')
n = int(input())

a = []

for i in range(0, n):
    print('Введите элемент', i)
    a.append(int(input()))

for i in range(0, n - 1):
    if (a[i] < 0 and a[i+1] < 0) or (a[i] >= 0 and a[i+1] >= 0):
        check = True

if (check):
    print('В этом массиве есть два элемента, идущие подряд и имеющие одинаковый знак')
else:
    print('Таких элементов нет')
