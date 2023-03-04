#평범한 배낭 BOJ 12865
#knapsack 

n, k = map(int, input().split())  # n: 물건 수, k:최대 무게

dp = [[0]*(k+1) for _ in range(n+1)]
m = [[0, 0]]
for i in range(n):
    w, v = map(int, input().split())    # w:무게, v:가치
    m.append([w, v])

for i in range(1, n+1):
    w = m[i][0]
    v = m[i][1]
    for j in range(1, k+1):
        
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w]+v, dp[i-1][j])

print(dp[n][k])
