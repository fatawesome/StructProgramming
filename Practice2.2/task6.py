import math

print('Give me X')
x = float(input())
print('Give me Y')
y = float(input())

c = math.sqrt(math.pow(x,2) + math.pow(y,2))

if ((x <= 1) and (y <= 1)) and (c >= 1):
    print("Good!")
else:
    print("Bad :(")
