import math

print("Give me 2 numbers")
p = int(input())
y = int(input())
l = math.log(p ** 2 + y ** 3)
ex = math.e ** p

# print(math.log(p ** 2 + y ** 3) + math.e ** p)
print(l + ex)
