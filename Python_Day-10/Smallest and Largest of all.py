n = int(input())
a = list(map(int,input().split()))
n = len(a)
a.sort()
min = a[0]
print(min)
max = a[-1]
print(max)
