n,m = map(int,input().split())
arr = []
for i in range(n):
    k = list(map(int,input().split(" ")))
    arr.append(k)
def maxi_row(arr):
    no_of_column = len(arr[0])
for i in range(n):
    m1 = 0
    for j in range(m):
        if arr[i][j] > m1:
            m1 = arr[i][j]
    print(m1, end = " ")