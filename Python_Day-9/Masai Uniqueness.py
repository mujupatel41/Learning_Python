s = input()
flag = 0
n = len(s)
for i in range(n-1):
    for j in range(i+1,n):
        if s[i]==s[j]:
            flag=1
            break
if flag==1:
    print("No")
else:
    print("Unique")