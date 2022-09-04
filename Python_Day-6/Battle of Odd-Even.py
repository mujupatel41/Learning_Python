n = int(input())
x = list(map(int,input().split()))
n = len(x)
Even = 0
Odd = 0
for i in range(n):
    if x[i]%2==0:
        Even = Even+x[i]
    else:
        Odd=Odd+x[i]
if Even>=Odd:
    print("Even")
else:
    print("Odd")