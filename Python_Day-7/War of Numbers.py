n = int(input())
arr = list(map(int,input().split()))
n = len(arr)
even = 0
odd = 0
for i in range(n):
    if arr[i]%2==0:
        even = even+arr[i]
    else:
        odd = odd+arr[i]
print(even-odd)