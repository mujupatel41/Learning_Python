N,X = map(int,input().split(" "))
sum = 1
for i in range(1,N,1):
    y = X**i
    sum = sum + y
if N<=0 or X<=0:
    print("-1")
else:
    print(sum)