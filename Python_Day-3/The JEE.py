p1,c1,m1 = map(int,input().split(" "))
p2,c2,m2 = map(int,input().split(" "))
t1 = (p1+c1+m1)
t2 = (p2+c2+m2)
if t1>t2:
    print("First")
else:
    print("Second")