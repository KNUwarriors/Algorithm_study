#줄세우기 BOJ 2631
#DP 존나 어렵네
#LIS 공부


n = int(input())

child = []
for _ in range(n):
    child.append(int(input()))


dp = [0 for _ in range(n)]
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if child[j] < child[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
