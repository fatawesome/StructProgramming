a = input('Введите символ: ')
check = False
arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(0,9):
    if (a == arr[i]):
        check = True
        break
if (check):
    print(a, ' - цифра')
else:
    print(a, ' - не цифра')
