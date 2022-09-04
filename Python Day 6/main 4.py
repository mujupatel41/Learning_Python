n = int(input())
x = list(map(int,input().split()))
n = len(x)
flag = 0
for i in range(n):
    if x[i]==42:
        flag=1
        break
if flag==1:
    print("Yes")
else:
    print("No")