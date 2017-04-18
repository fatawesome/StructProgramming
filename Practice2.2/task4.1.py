x = int(input())
check = False
if (x < 9) & (x == 5):
    check = True
else:
    while (x > 0):
        k = x % 10
        x = x // 10
        if (k == 5):
            check = True
            break

if check:
    print("5 входит в x")
else:
    print("5 не входит в x")
