s = input('Введите предложение: ')
s = s + ' '
words = 0
for i in range (1, len(s)):
    if (s[i] == ' ') & (s[i-1] != ' '):
        words+=1
print('Кол-во слов в предложении: ', words)
