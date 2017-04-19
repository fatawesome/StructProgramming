import math

x = int(input())
n = int(input())
sum = 0
for i in range (1,n+1):
    sum = sum + math.cos(math.radians(i*x))/i

print(sum)
