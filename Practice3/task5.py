sum = 0

for i in range (200, 301):
    for q in range (1, i):
        if (i % q == 0):
            sum = sum + q
    for j in range (200, 301):
        if (j == sum):
            print(i, j)
    sum = 0
