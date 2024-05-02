# 백준 13398번 연속합 2

n = int(input())
a = list(map(int, input().split()))
dl = [0] * n
dr = [0] * n
dl[0] = a[0]
dr[n-1]= a[n-1]

for i in range(1, n):
    dl[i] = max(dl[i-1]+a[i], a[i])

for i in range(n-2, -1, -1):
    dr[i] = max(dr[i+1]+a[i], a[i])

max_sum = max(dl)
for i in range(1, n-1):
    max_sum = max(max_sum, dl[i-1]+dr[i+1])

print(max_sum)