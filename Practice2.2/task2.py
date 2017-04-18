print("Give me salary")
x = int(input())
print("Give me experience")
y = int(input())

if (y > 2 and y <= 5):
    x = x * 0.02
elif (y > 5 and y <= 10):
    x = x * 0.05
else: x = 0

print(x)
