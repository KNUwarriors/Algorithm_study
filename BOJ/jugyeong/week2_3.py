n=int(input())
dp=[[0 for i in range(10)] for j in range(n+1)]
def dynamic(n):
    for i in range(1,n+1):
        for j in range(10):
            if i==1:
                dp[i][j]=1
            else:
                dp[i][j]=sum(dp[i-1][:j+1])
dynamic(n)
print(sum(dp[n])%10007)
