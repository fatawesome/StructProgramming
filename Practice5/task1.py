a = []
sum = 0
for i in range (0,12):
    a.append(int(input()))
    sum = sum + a[i]
print(a)
mid = sum / 14
print(mid)
a[4] = mid
print(a)
