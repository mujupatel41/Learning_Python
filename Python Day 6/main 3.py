n = int(input())
x = list(map(int,input().split()))
n = len(x)
sum = 0
for i in range(1,n,2):
        sum = sum + x[i]
print(sum)