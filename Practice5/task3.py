binary = int(input('Here comes binary: '))
octal = []
count = 0
triple = 0

while (binary > 0):
    triple = binary % 1000

    if (triple == 0):
        octal.append(0)
    elif (triple == 1):
        octal.append(1)
    elif (triple == 10):
        octal.append(2)
    elif (triple == 11):
        octal.append(3)
    elif (triple == 100):
        octal.append(4)
    elif (triple == 101):
        octal.append(5)
    elif (triple == 110):
        octal.append(6)
    elif (triple == 111):
        octal.append(7)

    binary = binary // 1000

octal.reverse()
#print(octal)
octal_num = 0
k = len(octal)

for i in range(len(octal)):
    octal_num = octal_num + octal[i] * pow(10, k - 1)
    k = k - 1

print(octal_num)
