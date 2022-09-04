n = int(input())
s = input()
n = len(s)
x = 0
y = 0
for i in range(n):
    if s[i]=="u":
        x = x+1
    elif s[i]=="d":
        x = x-1
    elif s[i]=="r":
        y = y+1
    elif s[i]=="l":
        y = y-1
print(x,y)