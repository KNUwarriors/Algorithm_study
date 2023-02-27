#가장긴~4 BOJ 14002

n = int(input())

array = list(map(int, input().split()))

dp = [1]*n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

# 수열 값
x = max(dp)
result = []
for i in range(n-1, -1, -1):
    if dp[i] == x:
        result.append(array[i])
        x -= 1
result.reverse()

for j in result:
    print(j, end=' ')
