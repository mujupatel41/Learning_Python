import math
n = int(input())
x = list(map(int,input().split()))
avg = 0
n = len(x)
sum = 0
for i in x:
    sum = sum+i
avg = sum/n
print(math.ceil(avg))