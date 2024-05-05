# 백준 2225 합분해
n, k = map(int, input().split())

d = [[0 for _ in range(n+1)] for _ in range(k+1)]

for i in range(n+1):
    d[1][i] = 1

for i in range(2, k+1):
    for j in range(0 , n+1):
        for l in range(0, n+1):
            d[i][j] += d[i-1][j-l]


print(d[k][n]%1000000000)
