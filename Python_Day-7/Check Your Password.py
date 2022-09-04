t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    a = 0
    b = 0
    for i in range(n):
        if s[i].isalpha():
            a = a+1
        elif s[i].isdigit():
            b = b+1
    if n>2 and b>=1 and a>n//2:
            print("Strong")
    else:
            print("Weak")