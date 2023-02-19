#10844
n=int(input())

dp=[[0 for i in range(10)] for j in range(n+1)]

def dynamic(n):
    for i in range(1,10):
        dp[1][i]=1
    for j in range(2,n+1):
        for k in range(0,10):
            if k==0:
                dp[j][k]=dp[j-1][1]
            elif k==9:
                dp[j][k]=dp[j-1][8]
            else:
                dp[j][k]=dp[j-1][k-1]+dp[j-1][k+1]

    ans=0
    for i in range(0,10):
        ans+=dp[n][i]
    return ans
print(dynamic(n)%1000000000)
                
