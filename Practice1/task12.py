s = input('Введите слово: ')
check = True

for i in range(0, len(s)//2):
    if (s[i] != s[len(s) - 1 - i]):
        check = False
if (check):
    print(s, ' - палиндром')
else:
    print(s, ' - не палиндром')
