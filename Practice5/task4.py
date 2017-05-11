import sys
n = 4
row1 = [0, 1, 0, 1]
row2 = [1, 0, 1, 0]
a = []

for i in range(n):
    a.append([])
    for j in range(n):
        if ((i + j) % 2 == 0):
            a[i].append(0)
        else:
            a[i].append(1)

for i in range(n):
    for j in range(n):
        sys.stdout.write("%d" % (a[i][j]))
    print()
