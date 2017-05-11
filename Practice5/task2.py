a = []
b = []
tmp = 0

for i in range(8):
    a.append(int(input()))
    tmp = a[i] % 10
    b.append(tmp)

print(b)
