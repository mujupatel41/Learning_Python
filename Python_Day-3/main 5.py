L1,B1,L2,B2 = map(int,input().split(" "))

a1 = (L1*B1)
a2 = (L2*B2)

p1 = (2*(L1+B1))
p2 = (2*(L2+B2))

if a1>a2:
    print("true")
else:
    print("false")
    
if p1>p2:
    print("true")
else:
    print("false")