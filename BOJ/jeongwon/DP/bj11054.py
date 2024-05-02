# 백준 11054번 가장 긴 바이토닉 부분 수열

n = int(input())
d1 = [1] * n
d2 = [1] * n
a = list(map(int, input().split()))

for i in range(1, n):
    for j in range(0, i):
        if a[i] > a[j] and d1[j] +1 > d1[i]:
            d1[i] = d1[j] +1

for i in range(n-1, 0, -1):
    for j in range(0, i):
        if a[i] < a[j] and d2[i] + 1 > d2[j]:
            d2[j] = d2[i] +1

ans = 1
for i in range(n):
    ans = max(ans, d1[i]+d2[i] -1)
print(ans)

