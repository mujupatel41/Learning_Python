N,M = map(int,input().split(" "))
N = (((N*6)+7)-19)
if N>M:
    print("Greater!")
elif N==M:
    print("Equal!")
else:
    print("Lesser!")