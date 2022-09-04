n = int(input())
s = input()
c = 0
x = 0
ch = ""
for i in range(n):
    x = s.count(s[i])
    if x>c:
        c=x
        ch=s[i]
print(ch)