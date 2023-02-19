n=int(input())
temp=list(map(int,input().split()))
dp=[1 for i in range(len(temp))]

for i in range(n):
    if i==0:
        dp[i]=1
    else:
        for j in range(i):
            if temp[i]>temp[j]:
                dp[i]=max(dp[j]+1,dp[i])
print(max(dp))
