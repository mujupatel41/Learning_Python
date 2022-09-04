t = int(input())
for i in range(t):
    s = input()
    n = len(s)
    s1 = ""
    for i in range(n-1,-1,-1):
        s1 = s1+s[i]
    print(s1)