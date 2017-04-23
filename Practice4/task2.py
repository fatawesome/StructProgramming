str = input()
count = 0
str = str + ' '
print(str)
for i in range(1, len(str)):
    if (str[i - 1] != ' ') and (str[i] == ' '):
        count = count + 1
print(count)
