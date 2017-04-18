x = int(input())
a = int(input())
check = False
if (x < 9) & (x == a):
    check = True
else:
    while (x > 0):
        k = x % 10
        x = x // 10
        if (k == a):
            check = True
            break

if check:
    print("a входит в x")
else:
    print("a НЕ входит в x")
