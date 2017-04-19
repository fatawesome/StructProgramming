import math
x = int(input())
k = int(input())
t = 2
u = 1
sum = 0
for t in range(2,k):
    u = u * (t * math.pow(x,t)) / (t - 12)
for i in range(1,t):
    sum = sum + ((i - 4) / (i - 6))
u = u * sum
print(u)
