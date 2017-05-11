surname = []
result = []
count = int(input('Give me counter: '))
max = -1
sur_out = ''
k = 0
for i in range(0,count):
    surname.append(input('Surname: '))
    result.append(int(input('Distance: ')))

while (k != 4):
    for i in range(0,count):
        if (result[i] > max):
            max = result[i]
            sur_out = surname[i]
    print(sur_out, ' ')
    k = k + 1
    max = -1
    result.pop(i)
    count = count - 1
