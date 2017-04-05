import math

print("Give me 2 numbers")
d = float(input())
y = float(input())
l = math.log(d) + (3.5 * (d ** 2) + 1)
c =  math.cos(math.radians(2*y))

# print(math.log(d) + (3,5 * (d ** 2) + 1) / math.cos(math.radians(2*y)))
print(l + c)
