a = []
n = 7
m = 7
sum = 0

for i in range(n):
    row = input().split()
    for i in range(m):
         row[i] = int(row[i])
    a.append(row)

for i in range(n):
    for j in range(m):
        if (a[i][j] % 2 != 0) and (a[i][j] < 0):
            sum = sum + abs(a[i][j])

print(sum)
