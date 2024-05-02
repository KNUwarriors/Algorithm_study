# 백준 11722번 가장 긴 감소하는 부분 수열

n = int(input())
a = list(map(int, input().split()))
d = [1] * n
ans = 1

for i in range(1, n):
    for j in range(0,i):
        if a[i] < a[j] and d[i] < d[j] +1:
            d[i] = d[j] + 1
    ans = max(ans, d[i])

print(ans)