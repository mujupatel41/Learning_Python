n = int(input())
x = list(map(int,input().split(" ")))
n = len(x)
x.sort()
max = x[-1]
print(max)